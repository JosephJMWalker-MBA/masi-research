"""One fixed WP1 experiment, not a MASI runtime. Baseline needs only stdlib."""

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
import math
import os
from pathlib import Path
import platform
import resource
import subprocess
import time
import uuid

from probe_candidates import CANDIDATES, CandidateAbstention, load_candidate

ROOT = Path(__file__).resolve().parent
EXPERIMENT = ROOT / "experiments/wp1"


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def file_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, sort_keys=True, allow_nan=False) + "\n")


def validate_fixture(fixture):
    fields = {"id", "category", "premise", "claim", "expected"}
    if not isinstance(fixture, dict) or set(fixture) != fields:
        raise ValueError("fixture must have exactly id/category/premise/claim/expected")
    if any(not isinstance(fixture[k], str) or not fixture[k].strip() for k in fields):
        raise ValueError("fixture fields must be nonempty strings")
    if any(len(fixture[k]) > 4096 for k in ("premise", "claim")):
        raise ValueError("fixture exceeds 4096 character field bound")
    if fixture["expected"] not in {"supported", "not_supported"}:
        raise ValueError("invalid reference label")


def load_fixtures(path):
    fixtures = [json.loads(line) for line in Path(path).read_text().splitlines()]
    if not fixtures:
        raise ValueError("empty fixtures")
    seen = set()
    for fixture in fixtures:
        validate_fixture(fixture)
        if fixture["id"] in seen:
            raise ValueError("duplicate fixture ID")
        seen.add(fixture["id"])
    return fixtures


def verify_freeze():
    freeze = json.loads((EXPERIMENT / "freeze.json").read_text())
    for name, expected in freeze["files"].items():
        if file_hash(ROOT / name) != expected:
            raise ValueError(f"frozen file changed: {name}")
    return freeze


def normalize(candidate_id, native):
    if candidate_id not in CANDIDATES:
        raise ValueError("unregistered candidate")
    result = {
        "status": "ok", "verdict": None, "support_score": None,
        "score_semantics": "not_available", "calibration": "not_measured",
        "evidence_refs": ["premise", "claim"], "unsupported_assumptions": [],
        "assumption_reporting": "not_available", "escalation_requested": False,
        "reason": "native_support_score",
    }
    if candidate_id == "exact-match-v1":
        if type(native.get("exact_match")) is not bool:
            raise ValueError("baseline exact_match must be boolean")
        result.update(assumption_reporting="none_reported", reason="exact_match")
        if native["exact_match"]:
            result["verdict"] = "supported"
        else:
            result.update(status="abstain", reason="no_exact_match", escalation_requested=True)
        return result
    score = native.get("support_score")
    if type(score) not in (int, float) or not math.isfinite(score) or not 0 <= score <= 1:
        raise ValueError("support_score must be finite numeric value in [0,1]")
    result.update(support_score=score, score_semantics="uncalibrated_native_support_score")
    if score == 0.5:
        result.update(status="abstain", reason="threshold_tie", escalation_requested=True)
    else:
        result["verdict"] = "supported" if score > 0.5 else "not_supported"
    return result


def unavailable(status, reason):
    return {
        "status": status, "verdict": None, "support_score": None,
        "score_semantics": "not_available", "calibration": "not_measured",
        "evidence_refs": ["premise", "claim"], "unsupported_assumptions": [],
        "assumption_reporting": "not_available", "escalation_requested": True,
        "reason": reason,
    }


def git_value(*args):
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else None


def peak_rss_bytes():
    # ru_maxrss is process lifetime high water, not an isolated per-call allocation.
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if platform.system() == "Darwin" else value * 1024)


def run_probe(candidate_id, output, model_root):
    if candidate_id not in CANDIDATES:
        raise ValueError("unregistered candidate")
    freeze = verify_freeze()
    protocol = json.loads((EXPERIMENT / "protocol.json").read_text())
    fixtures = load_fixtures(EXPERIMENT / "fixtures.jsonl")
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    run_id = str(uuid.uuid4())
    manifest = {
        "run_id": run_id, "started_at": datetime.now(timezone.utc).isoformat(),
        "candidate_id": candidate_id, "candidate": CANDIDATES[candidate_id],
        "protocol": protocol, "freeze": freeze,
        "git": {"branch": git_value("branch", "--show-current"),
                "commit": git_value("rev-parse", "HEAD"),
                "status_porcelain": git_value("status", "--porcelain=v1")},
        "source_sha256": {p: file_hash(ROOT / p) for p in ("probe.py", "probe_candidates.py")},
        "environment": {
            "python": platform.python_version(), "platform": platform.platform(),
            "machine": platform.machine(), "cpu_count": os.cpu_count(),
            "packages": dict(sorted((d.metadata["Name"], d.version) for d in importlib.metadata.distributions())),
            "device": "cpu", "threads": 1, "dtype": "float32", "quantization": None,
            "hardware_memory_bytes": None,
            "hardware_memory_reason": "not measured by portable runner; see handoff host preflight",
        },
        "resources": {"model_load_seconds": None, "passes_per_fixture": 1,
                      "retries": 0, "retrieval_calls": 0, "tool_calls": 0,
                      "api_cost": 0, "api_cost_currency": "USD", "api_cost_scope": "no external inference",
                      "output_tokens": None, "output_tokens_reason": "classification, not generation",
                      "rss_scope": "process lifetime high-water RSS including imports, load and inference"},
        "state": "started",
    }
    model_manifest = Path(model_root) / "manifest.json"
    write_json(output / "manifest.json", manifest)
    load_start = time.perf_counter()
    adapter, load_error = None, None
    try:
        if candidate_id != "exact-match-v1" and model_manifest.exists():
            manifest["model_artifacts"] = json.loads(model_manifest.read_text())
        adapter = load_candidate(candidate_id, Path(model_root))
        manifest["candidate"] = adapter.metadata
    except Exception as exc:
        load_error = {"type": type(exc).__name__, "message": str(exc), "stage": "load"}
    manifest["resources"]["model_load_seconds"] = time.perf_counter() - load_start
    manifest["load_error"] = load_error
    write_json(output / "manifest.json", manifest)
    counts, correct, calls, unknown_calls = Counter(), 0, 0, 0
    with (output / "raw.jsonl").open("x") as raw_file, (output / "normalized.jsonl").open("x") as normalized_file:
        for fixture in fixtures:
            start = time.perf_counter()
            raw = {"run_id": run_id, "fixture_id": fixture["id"], "candidate_id": candidate_id,
                   "native_output": None, "error": load_error}
            input_tokens, model_calls = None, 0
            if load_error:
                result = unavailable("error", "candidate_load_failed")
            else:
                try:
                    # Reference labels and categories never cross the inference boundary.
                    raw["native_output"] = adapter.infer(fixture["premise"], fixture["claim"])
                    input_tokens = raw["native_output"].get("input_tokens")
                    model_calls = raw["native_output"].get("model_calls")
                    if input_tokens is not None and (type(input_tokens) is not int or input_tokens < 0):
                        raise ValueError("invalid input token count")
                    if type(model_calls) is not int or model_calls not in (0, 1):
                        raise ValueError("invalid model call count")
                    result = normalize(candidate_id, raw["native_output"])
                    canonical(raw)  # Reject NaN/Infinity even in non-score native fields.
                except CandidateAbstention as exc:
                    raw["abstention"] = str(exc)
                    input_tokens = exc.input_tokens
                    result = unavailable("abstain", str(exc))
                except Exception as exc:
                    raw["error"] = {"type": type(exc).__name__, "message": str(exc), "stage": "infer_or_normalize"}
                    # Preserve malformed values as text rather than emit invalid JSON.
                    try:
                        canonical(raw["native_output"])
                    except (TypeError, ValueError):
                        raw["native_output_repr"] = repr(raw["native_output"])
                        raw["native_output"] = None
                    result = unavailable("error", "candidate_inference_or_normalization_failed")
                    if input_tokens is not None and (type(input_tokens) is not int or input_tokens < 0):
                        input_tokens = None
                    model_calls = None
            normalized = {
                "contract_version": protocol["contract_version"], "run_id": run_id,
                "fixture_id": fixture["id"], "candidate_id": candidate_id,
                "responsibility": protocol["responsibility"],
                "input_sha256": digest({"premise": fixture["premise"], "claim": fixture["claim"]}),
                "raw_record_sha256": digest(raw), **result,
                "resources": {
                    "wall_seconds": time.perf_counter() - start,
                    "input_tokens": input_tokens,
                    "input_tokens_reason": None if input_tokens is not None else "no tokenization result available",
                    "model_calls": model_calls,
                    "model_calls_reason": "failed invocation count unknown" if model_calls is None else None,
                    "passes": 1, "peak_process_rss_bytes": peak_rss_bytes(),
                },
            }
            raw_file.write(canonical(raw) + "\n")
            normalized_file.write(canonical(normalized) + "\n")
            raw_file.flush()
            normalized_file.flush()
            counts[result["status"]] += 1
            correct += result["status"] == "ok" and result["verdict"] == fixture["expected"]
            if model_calls is None:
                unknown_calls += 1
            else:
                calls += model_calls
    summary = {
        "run_id": run_id, "candidate_id": candidate_id, "total": len(fixtures),
        "counts": {k: counts[k] for k in ("ok", "abstain", "error")}, "correct": correct,
        "correct_denominator": len(fixtures), "coverage": counts["ok"] / len(fixtures),
        "known_model_calls": calls, "unknown_call_count_records": unknown_calls,
        "claim_scope": protocol["claim_scope"], "labels_status": protocol["dataset_status"],
    }
    write_json(output / "summary.json", summary)
    manifest["state"] = "completed_with_errors" if counts["error"] else "completed"
    manifest["finished_at"] = datetime.now(timezone.utc).isoformat()
    manifest["artifact_sha256"] = {p: file_hash(output / p) for p in ("raw.jsonl", "normalized.jsonl", "summary.json")}
    manifest["resources"]["peak_process_rss_bytes"] = peak_rss_bytes()
    write_json(output / "manifest.json", manifest)
    return 1 if counts["error"] else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", required=True, choices=tuple(CANDIDATES))
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--model-root", default=ROOT / ".models", type=Path)
    args = parser.parse_args()
    raise SystemExit(run_probe(args.candidate, args.output, args.model_root))


if __name__ == "__main__":
    main()
