#!/usr/bin/env python3
"""Verify the six fixed WP1 runs and the frozen 1e-6 repeat tolerance."""

import argparse
import json
import math
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from probe import EXPERIMENT, digest, file_hash, load_fixtures, normalize, verify_freeze


def require(condition, message):
    if not condition:
        raise ValueError(message)


def compare_native(left, right):
    """Return maximum absolute numerical difference; structure must match."""
    if type(left) in (int, float) and type(right) in (int, float):
        require(math.isfinite(left) and math.isfinite(right), "non-finite native output")
        delta = abs(left - right)
        require(delta <= 1e-6, "repeat exceeds frozen tolerance")
        return delta
    if isinstance(left, dict) and isinstance(right, dict):
        require(left.keys() == right.keys(), "native output keys differ")
        return max((compare_native(left[k], right[k]) for k in left), default=0)
    if isinstance(left, list) and isinstance(right, list):
        require(len(left) == len(right), "native output dimensions differ")
        return max((compare_native(a, b) for a, b in zip(left, right)), default=0)
    require(type(left) is type(right) and left == right, "native output values differ")
    return 0


def verify(evidence):
    freeze = verify_freeze()
    fixtures = load_fixtures(EXPERIMENT / "fixtures.jsonl")
    report = {"freeze_id": freeze["freeze_id"], "result": "pass", "pairs": []}
    source_identity = None
    run_ids = set()
    for prefix, candidate in (("baseline", "exact-match-v1"), ("hhem", "hhem-2.1"),
                              ("nli", "nli-deberta-small")):
        runs = []
        manifests = []
        for index in (1, 2):
            location = Path(evidence) / f"{prefix}-{index}"
            manifest = json.loads((location / "manifest.json").read_text())
            summary = json.loads((location / "summary.json").read_text())
            raw = [json.loads(s) for s in (location / "raw.jsonl").read_text().splitlines()]
            normalized = [json.loads(s) for s in (location / "normalized.jsonl").read_text().splitlines()]
            require(manifest["state"] == "completed", f"incomplete run: {location}")
            require(manifest["freeze"] == freeze, "freeze differs")
            require(manifest["candidate_id"] == candidate, "wrong candidate")
            require(manifest["run_id"] not in run_ids, "duplicate run ID")
            run_ids.add(manifest["run_id"])
            if source_identity is None:
                source_identity = manifest["source_sha256"]
            require(source_identity == manifest["source_sha256"], "caller or adapter source changed")
            for name, expected in manifest["artifact_sha256"].items():
                require(file_hash(location / name) == expected, f"artifact changed: {location/name}")
            require(len(raw) == len(normalized) == len(fixtures), "incomplete fixture records")
            correct = 0
            for fixture, native, result in zip(fixtures, raw, normalized):
                require(native["fixture_id"] == result["fixture_id"] == fixture["id"], "fixture order differs")
                require(native["candidate_id"] == result["candidate_id"] == candidate, "record candidate differs")
                require(native["run_id"] == result["run_id"] == manifest["run_id"], "run linkage differs")
                require(result["raw_record_sha256"] == digest(native), "raw record linkage differs")
                require(result["input_sha256"] == digest({k: fixture[k] for k in ("premise", "claim")}), "input differs")
                require(native["error"] is None and native["native_output"] is not None, "missing real output")
                expected = normalize(candidate, native["native_output"])
                require(all(result[k] == v for k, v in expected.items()), "normalization differs")
                require(result["resources"]["model_calls"] == (0 if prefix == "baseline" else 1), "call accounting differs")
                if prefix != "baseline":
                    require(0 < result["resources"]["input_tokens"] <= 512, "input token bound differs")
                correct += result["status"] == "ok" and result["verdict"] == fixture["expected"]
            require(summary["correct"] == correct and summary["correct_denominator"] == len(fixtures), "summary denominator differs")
            require(summary["counts"]["error"] == 0, "error records present")
            runs.append((raw, normalized))
            manifests.append(manifest)
        require(manifests[0]["candidate"] == manifests[1]["candidate"], "candidate metadata changed")
        require(manifests[0]["environment"] == manifests[1]["environment"], "environment changed")
        require(manifests[0].get("model_artifacts") == manifests[1].get("model_artifacts"), "weights changed")
        delta = 0
        for (a, x), (b, y) in zip(zip(*runs[0]), zip(*runs[1])):
            delta = max(delta, compare_native(a["native_output"], b["native_output"]))
            for key in ("status", "verdict", "reason", "escalation_requested", "input_sha256"):
                require(x[key] == y[key], "normalized decisions differ")
        report["pairs"].append({"candidate_id": candidate, "fixtures_per_run": len(fixtures),
                                "max_absolute_native_difference": delta,
                                "normalized_decisions_identical": True})
    report["run_count"] = len(run_ids)
    report["source_sha256"] = source_identity
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence", type=Path, default=EXPERIMENT / "evidence")
    args = parser.parse_args()
    print(json.dumps(verify(args.evidence), indent=2, sort_keys=True))
