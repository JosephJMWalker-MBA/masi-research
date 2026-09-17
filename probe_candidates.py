"""Three fixed Precision probes; no routing, composition, or provider calls."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path


CANDIDATES = {
    "exact-match-v1": {
        "candidate_id": "exact-match-v1",
        "source": "repository:probe_candidates.py",
        "revision": "exact-match-v1",
        "license": "Apache-2.0",
        "license_review_date": "2026-09-17",
        "model_class": "deterministic trimmed case-insensitive equality",
        "parameter_count": 0,
        "dtype": None,
    },
    "hhem-2.1": {
        "candidate_id": "hhem-2.1",
        "source": "https://huggingface.co/vectara/hallucination_evaluation_model",
        "revision": "8e4a2e6e96c708cc76c2344f7e4757df2515292c",
        "license": "Apache-2.0",
        "license_review_date": "2026-09-17",
        "model_class": "HHEMv2ForSequenceClassification / T5 encoder verifier",
        "foundation_revision": "7bcac572ce56db69c1ea7c8af255c5d7c9672fc2",
        "dtype": "float32",
    },
    "nli-deberta-small": {
        "candidate_id": "nli-deberta-small",
        "source": "https://huggingface.co/tasksource/deberta-small-long-nli",
        "revision": "9a77395d4d3751be9e2a69c4ae318491d9b3fffb",
        "license": "Apache-2.0",
        "license_review_date": "2026-09-17",
        "model_class": "DebertaV2ForSequenceClassification / DeBERTa v3 small NLI",
        "dtype": "float32",
    },
}

# Explicit file lists keep preparation bounded and exclude alternate weight formats.
MODEL_FILES = {
    "hhem-2.1": {
        "repo_id": "vectara/hallucination_evaluation_model",
        "revision": CANDIDATES["hhem-2.1"]["revision"],
        "files": ["README.md", "config.json", "configuration_hhem_v2.py",
                  "modeling_hhem_v2.py", "model.safetensors"],
    },
    "flan-t5-base": {
        "repo_id": "google/flan-t5-base",
        "revision": CANDIDATES["hhem-2.1"]["foundation_revision"],
        "files": ["README.md", "config.json", "tokenizer_config.json",
                  "special_tokens_map.json", "tokenizer.json", "spiece.model"],
    },
    "nli-deberta-small": {
        "repo_id": "tasksource/deberta-small-long-nli",
        "revision": CANDIDATES["nli-deberta-small"]["revision"],
        "files": ["README.md", "config.json", "tokenizer_config.json",
                  "special_tokens_map.json", "tokenizer.json", "spm.model",
                  "added_tokens.json", "model.safetensors"],
    },
}

MAX_MODEL_TOKENS = 512
HHEM_PROMPT = (
    "<pad> Determine if the hypothesis is true given the premise?\n\n"
    "Premise: {text1}\n\nHypothesis: {text2}"
)


class CandidateAbstention(Exception):
    """A bounded input cannot be evaluated without changing its evidence."""

    def __init__(self, reason: str, input_tokens: int | None = None):
        super().__init__(reason)
        self.reason = reason
        self.input_tokens = input_tokens


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _verify_snapshot(model_root: Path, snapshot_id: str) -> Path:
    """Catch missing or changed local artifacts before any custom code loads."""
    manifest = json.loads((model_root / "manifest.json").read_text())
    expected = MODEL_FILES[snapshot_id]
    recorded = manifest["snapshots"][snapshot_id]
    if (manifest["schema_version"] != 1
            or recorded["repo_id"] != expected["repo_id"]
            or recorded["revision"] != expected["revision"]
            or set(recorded["files"]) != set(expected["files"])):
        raise ValueError(f"Unrecognized local model manifest: {snapshot_id}")
    location = (model_root / snapshot_id).resolve()
    for filename in expected["files"]:
        path = location / filename
        item = recorded["files"][filename]
        if path.stat().st_size != item["size_bytes"] or file_sha256(path) != item["sha256"]:
            raise ValueError(f"Local model artifact changed: {snapshot_id}/{filename}")
    return location


class ExactMatch:
    def __init__(self):
        self.metadata = dict(CANDIDATES["exact-match-v1"])

    def infer(self, premise: str, claim: str) -> dict:
        return {
            "exact_match": premise.strip().casefold() == claim.strip().casefold(),
            "input_tokens": None,
            "model_calls": 0,
        }


class LocalClassifier:
    """Only the two explicitly frozen model paths share this small adapter."""

    def __init__(self, candidate_id: str, model_root: Path):
        location = _verify_snapshot(model_root, candidate_id)
        foundation = (_verify_snapshot(model_root, "flan-t5-base")
                      if candidate_id == "hhem-2.1" else None)
        # Each from_pretrained also uses local_files_only. The upstream HHEM
        # constructor receives a local foundation path, never a floating Hub ID.
        os.environ["HF_HUB_OFFLINE"] = "1"
        os.environ["TRANSFORMERS_OFFLINE"] = "1"
        os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"
        os.environ["HF_MODULES_CACHE"] = str((model_root / ".hf_modules").resolve())
        import torch
        from transformers import AutoConfig, AutoModelForSequenceClassification, AutoTokenizer

        torch.set_num_threads(1)
        if torch.get_num_interop_threads() != 1:
            torch.set_num_interop_threads(1)
        torch.manual_seed(0)
        torch.use_deterministic_algorithms(True)
        self.torch = torch
        self.candidate_id = candidate_id
        if candidate_id == "hhem-2.1":
            config = AutoConfig.from_pretrained(
                location, local_files_only=True, trust_remote_code=True)
            config.foundation = str(foundation)
            if config.prompt != HHEM_PROMPT:
                raise ValueError("Unexpected HHEM prompt")
            self.model = AutoModelForSequenceClassification.from_pretrained(
                location, config=config, local_files_only=True,
                trust_remote_code=True, use_safetensors=True,
                torch_dtype=torch.float32)
            # Upstream deliberately exposes this misspelled attribute.
            self.tokenizer = self.model.tokenzier
            self.labels = {0: "hallucinated", 1: "consistent"}
            self.support_index = 1
        else:
            self.tokenizer = AutoTokenizer.from_pretrained(
                location, local_files_only=True, trust_remote_code=False)
            self.model = AutoModelForSequenceClassification.from_pretrained(
                location, local_files_only=True, trust_remote_code=False,
                use_safetensors=True, torch_dtype=torch.float32)
            self.labels = {0: "entailment", 1: "neutral", 2: "contradiction"}
            self.support_index = 0
        if self.model.config.id2label != self.labels:
            raise ValueError(f"Unexpected label mapping: {candidate_id}")
        self.model.to(device="cpu", dtype=torch.float32).eval()
        self.metadata = dict(CANDIDATES[candidate_id])
        self.metadata["parameter_count"] = sum(p.numel() for p in self.model.parameters())

    def infer(self, premise: str, claim: str) -> dict:
        if self.candidate_id == "hhem-2.1":
            encoded = self.tokenizer(
                HHEM_PROMPT.format(text1=premise, text2=claim),
                truncation=False, return_tensors="pt")
        else:
            encoded = self.tokenizer(
                premise, text_pair=claim, truncation=False, return_tensors="pt")
        input_tokens = int(encoded["input_ids"].shape[-1])
        if input_tokens > MAX_MODEL_TOKENS:
            raise CandidateAbstention("input_token_limit_exceeded", input_tokens)
        with self.torch.inference_mode():
            logits = self.model(**encoded).logits[0]
            scores = self.torch.softmax(logits, dim=-1)
        return {
            "logits": logits.tolist(),
            "scores": {label: float(scores[index]) for index, label in self.labels.items()},
            "support_score": float(scores[self.support_index]),
            "input_tokens": input_tokens,
            "model_calls": 1,
        }


def load_candidate(candidate_id: str, model_root: Path):
    """Select a frozen implementation without changing the calling experiment."""
    if candidate_id not in CANDIDATES:
        raise ValueError(f"Unknown candidate: {candidate_id}")
    if candidate_id == "exact-match-v1":
        return ExactMatch()
    return LocalClassifier(candidate_id, Path(model_root))
