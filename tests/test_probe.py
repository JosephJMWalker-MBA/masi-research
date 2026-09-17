"""Contract and evidence tests; fake classifiers never load model weights."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

import probe
import probe_candidates


def fixture(**changes):
    value = {
        "id": "example",
        "category": "literal",
        "premise": "The light is on.",
        "claim": "The light is on.",
        "expected": "supported",
    }
    value.update(changes)
    return value


class FixtureContractTests(unittest.TestCase):
    def test_accepts_bounded_inputs_without_rewriting_evidence(self):
        value = fixture(premise="  The light is on.  ", claim="x" * 4096)
        original = dict(value)
        probe.validate_fixture(value)
        self.assertEqual(value, original)

    def test_rejects_missing_extra_empty_and_nonstring_fields(self):
        for key in fixture():
            missing = fixture()
            del missing[key]
            for value in (missing, fixture(**{key: ""}), fixture(**{key: None})):
                with self.subTest(key=key, value=value):
                    with self.assertRaises(ValueError):
                        probe.validate_fixture(value)
        with self.assertRaises(ValueError):
            probe.validate_fixture(fixture(answer="leaked label"))

    def test_rejects_unusable_evidence_and_undefined_labels(self):
        for changes in (
            {"premise": " \n\t"}, {"claim": " \n\t"},
            {"premise": "x" * 4097}, {"claim": "x" * 4097},
            {"expected": "contradiction"}, {"expected": "abstain"},
        ):
            with self.subTest(changes=changes):
                with self.assertRaises(ValueError):
                    probe.validate_fixture(fixture(**changes))

    def test_load_rejects_duplicate_identity(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "fixtures.jsonl"
            path.write_text("\n".join(json.dumps(value) for value in (
                fixture(), fixture(claim="A different claim."))))
            with self.assertRaises(ValueError):
                probe.load_fixtures(path)

    def test_load_preserves_order_and_content(self):
        records = [fixture(), fixture(id="second", expected="not_supported")]
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "fixtures.jsonl"
            content = "\n".join(json.dumps(value) for value in records) + "\n"
            path.write_text(content)
            self.assertEqual(probe.load_fixtures(path), records)
            self.assertEqual(path.read_text(), content)


class NormalizationTests(unittest.TestCase):
    def test_learned_boundary_is_abstention_and_direction_is_explicit(self):
        for candidate in ("hhem-2.1", "nli-deberta-small"):
            for score, status, verdict in (
                (0.0, "ok", "not_supported"),
                (0.499999, "ok", "not_supported"),
                (0.5, "abstain", None),
                (0.500001, "ok", "supported"),
                (1.0, "ok", "supported"),
            ):
                with self.subTest(candidate=candidate, score=score):
                    native = {"support_score": score, "logits": [-1, 1],
                              "input_tokens": 12, "model_calls": 1}
                    original = json.loads(json.dumps(native))
                    normalized = probe.normalize(candidate, native)
                    self.assertEqual(normalized["status"], status)
                    self.assertEqual(normalized["verdict"], verdict)
                    self.assertEqual(normalized["support_score"], score)
                    self.assertEqual(native, original)
                    self.assertNotEqual(normalized["calibration"], "calibrated")

    def test_invalid_scores_fail_instead_of_becoming_verdicts(self):
        for score in (float("nan"), float("inf"), -float("inf"), -0.01,
                      1.01, None, "0.9", True):
            with self.subTest(score=score):
                with self.assertRaises(ValueError):
                    probe.normalize("hhem-2.1", {"support_score": score})

    def test_exact_rule_does_not_infer_negative_or_fabricate_score(self):
        for exact, status, verdict in ((True, "ok", "supported"),
                                       (False, "abstain", None)):
            with self.subTest(exact=exact):
                normalized = probe.normalize("exact-match-v1", {
                    "exact_match": exact, "input_tokens": None, "model_calls": 0})
                self.assertEqual(normalized["status"], status)
                self.assertEqual(normalized["verdict"], verdict)
                self.assertIsNone(normalized["support_score"])


class AdapterBoundaryTests(unittest.TestCase):
    def test_exact_rule_is_deterministic_and_bounded(self):
        candidate = probe_candidates.load_candidate("exact-match-v1", Path("unused"))
        self.assertEqual(candidate.infer("  THE LIGHT IS ON. ", "The light is on."),
                         {"exact_match": True, "input_tokens": None, "model_calls": 0})
        self.assertFalse(candidate.infer("Mara bought a bike.",
                                         "Mara purchased a bicycle.")["exact_match"])

    def test_unknown_candidate_is_rejected(self):
        with self.assertRaises(ValueError):
            probe_candidates.load_candidate("unregistered", Path("unused"))

    def test_missing_local_artifacts_fail_before_loading_model(self):
        with tempfile.TemporaryDirectory() as temporary:
            for candidate in ("hhem-2.1", "nli-deberta-small"):
                with self.subTest(candidate=candidate):
                    with self.assertRaises(FileNotFoundError):
                        probe_candidates.load_candidate(candidate, Path(temporary))

    def test_changed_artifacts_and_wrong_revision_are_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            spec = probe_candidates.MODEL_FILES["hhem-2.1"]
            location = root / "hhem-2.1"
            location.mkdir()
            entries = {}
            for name in spec["files"]:
                (location / name).write_bytes(b"test artifact")
                entries[name] = {"size_bytes": 13, "sha256": hashlib.sha256(b"test artifact").hexdigest()}
            record = {"repo_id": spec["repo_id"], "revision": spec["revision"], "files": entries}
            manifest = {"schema_version": 1, "snapshots": {"hhem-2.1": record}}
            path = root / "manifest.json"
            path.write_text(json.dumps(manifest))
            self.assertEqual(probe_candidates._verify_snapshot(root, "hhem-2.1"), location.resolve())
            (location / "config.json").write_bytes(b"edit artifact")
            with self.assertRaisesRegex(ValueError, "artifact changed"):
                probe_candidates._verify_snapshot(root, "hhem-2.1")
            record["revision"] = "unreviewed"
            path.write_text(json.dumps(manifest))
            with self.assertRaisesRegex(ValueError, "Unrecognized"):
                probe_candidates._verify_snapshot(root, "hhem-2.1")

    def test_over_limit_input_abstains_without_truncation_or_forward_pass(self):
        for candidate_id in ("hhem-2.1", "nli-deberta-small"):
            with self.subTest(candidate=candidate_id):
                candidate = probe_candidates.LocalClassifier.__new__(
                    probe_candidates.LocalClassifier)
                candidate.candidate_id = candidate_id
                candidate.tokenizer = Mock(return_value={
                    "input_ids": Mock(shape=(1, 513))})
                candidate.model = Mock(side_effect=AssertionError("No forward pass allowed"))
                candidate.torch = Mock()
                with self.assertRaises(probe_candidates.CandidateAbstention) as caught:
                    candidate.infer("premise", "claim")
                self.assertEqual(caught.exception.input_tokens, 513)
                self.assertEqual(caught.exception.reason, "input_token_limit_exceeded")
                self.assertIs(candidate.tokenizer.call_args.kwargs["truncation"], False)
                candidate.model.assert_not_called()
                candidate.torch.inference_mode.assert_not_called()


class FreezeIntegrityTests(unittest.TestCase):
    def test_freeze_detects_changes_before_candidate_load_or_output_creation(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            experiment = root / "experiment"
            experiment.mkdir()
            frozen = root / "contract.txt"
            frozen.write_text("frozen boundary\n")
            freeze = {"files": {"contract.txt": hashlib.sha256(frozen.read_bytes()).hexdigest()}}
            (experiment / "freeze.json").write_text(json.dumps(freeze))
            output = root / "run"
            with patch.object(probe, "ROOT", root), patch.object(probe, "EXPERIMENT", experiment):
                self.assertEqual(probe.verify_freeze(), freeze)
                frozen.write_text("changed boundary\n")
                with patch.object(probe, "load_candidate") as loader:
                    with self.assertRaisesRegex(ValueError, "frozen file changed"):
                        probe.run_probe("exact-match-v1", output, root / "models")
                    loader.assert_not_called()
                self.assertFalse(output.exists())


class RunnerEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.experiment = self.root / "experiment"
        self.experiment.mkdir()
        self.records = [fixture(id="first"), fixture(
            id="second", premise="The box is red.", claim="The box is blue.",
            expected="not_supported")]
        self.fixture_path = self.experiment / "fixtures.jsonl"
        self.fixture_bytes = ("\n".join(json.dumps(record) for record in self.records)
                              + "\n").encode()
        self.fixture_path.write_bytes(self.fixture_bytes)
        protocol = json.loads((probe.EXPERIMENT / "protocol.json").read_text())
        (self.experiment / "protocol.json").write_text(json.dumps(protocol))
        self.addCleanup(patch.stopall)
        patch.object(probe, "EXPERIMENT", self.experiment).start()
        patch.object(probe, "verify_freeze", return_value={"files": {}}).start()
        patch.object(probe, "git_value", return_value="unit-test").start()

    def tearDown(self):
        self.assertEqual(self.fixture_path.read_bytes(), self.fixture_bytes)

    def candidate(self, candidate_id="hhem-2.1", side_effect=None):
        adapter = Mock()
        adapter.metadata = dict(probe_candidates.CANDIDATES[candidate_id])
        adapter.infer.return_value = {
            "support_score": 0.9, "logits": [0, 1], "input_tokens": 12,
            "model_calls": 1}
        if side_effect is not None:
            adapter.infer.side_effect = side_effect
        return adapter

    def artifacts(self, output):
        raw = [json.loads(line) for line in (output / "raw.jsonl").read_text().splitlines()]
        normalized = [json.loads(line) for line in (output / "normalized.jsonl").read_text().splitlines()]
        manifest = json.loads((output / "manifest.json").read_text())
        summary = json.loads((output / "summary.json").read_text())
        return raw, normalized, manifest, summary

    def assert_complete_linked_evidence(self, output):
        raw, normalized, manifest, summary = self.artifacts(output)
        self.assertEqual(len(raw), len(self.records))
        self.assertEqual(len(normalized), len(self.records))
        for source, original, result in zip(self.records, raw, normalized):
            self.assertEqual(original["fixture_id"], source["id"])
            self.assertEqual(result["fixture_id"], source["id"])
            self.assertEqual(original["run_id"], manifest["run_id"])
            self.assertEqual(result["run_id"], manifest["run_id"])
            canonical = json.dumps(original, sort_keys=True, separators=(",", ":"),
                                   allow_nan=False).encode()
            self.assertEqual(result["raw_record_sha256"], hashlib.sha256(canonical).hexdigest())
            self.assertNotIn("native_output", result)
            self.assertNotIn("verdict", original)
            self.assertGreaterEqual(result["resources"]["wall_seconds"], 0)
        for name, recorded_hash in manifest["artifact_sha256"].items():
            self.assertEqual(hashlib.sha256((output / name).read_bytes()).hexdigest(), recorded_hash)
        self.assertEqual(summary["total"], len(self.records))
        self.assertEqual(summary["correct_denominator"], len(self.records))
        return raw, normalized, manifest, summary

    def test_all_candidates_share_caller_and_receive_only_two_evidence_strings(self):
        for candidate_id in ("exact-match-v1", "hhem-2.1", "nli-deberta-small"):
            with self.subTest(candidate=candidate_id):
                adapter = self.candidate(candidate_id)
                if candidate_id == "exact-match-v1":
                    adapter.infer.side_effect = probe_candidates.ExactMatch().infer
                output = self.root / candidate_id
                with patch.object(probe, "load_candidate", return_value=adapter) as loader:
                    self.assertEqual(probe.run_probe(candidate_id, output, self.root / "models"), 0)
                loader.assert_called_once_with(candidate_id, self.root / "models")
                self.assertEqual(adapter.infer.call_count, len(self.records))
                for call, source in zip(adapter.infer.call_args_list, self.records):
                    self.assertEqual(call.args, (source["premise"], source["claim"]))
                    self.assertEqual(call.kwargs, {})
                raw, normalized, manifest, summary = self.assert_complete_linked_evidence(output)
                self.assertEqual(manifest["state"], "completed")
                self.assertEqual(summary["counts"]["error"], 0)
                self.assertEqual(summary["correct"], 1)
                self.assertEqual(summary["coverage"], 0.5 if candidate_id == "exact-match-v1" else 1.0)
                if candidate_id != "exact-match-v1":
                    self.assertEqual(raw[0]["native_output"]["logits"], [0, 1])
                    self.assertEqual(normalized[0]["resources"]["input_tokens"], 12)
                    self.assertEqual(summary["known_model_calls"], 2)

    def test_existing_output_is_not_overwritten_or_loaded(self):
        output = self.root / "existing"
        output.mkdir()
        sentinel = output / "raw.jsonl"
        sentinel.write_text("preserve existing evidence\n")
        with patch.object(probe, "load_candidate") as loader:
            with self.assertRaises(FileExistsError):
                probe.run_probe("hhem-2.1", output, self.root / "models")
            loader.assert_not_called()
        self.assertEqual(sentinel.read_text(), "preserve existing evidence\n")
        self.assertEqual(list(output.iterdir()), [sentinel])

    def test_load_failure_has_complete_error_records_and_failing_exit_status(self):
        output = self.root / "load-failure"
        with patch.object(probe, "load_candidate", side_effect=FileNotFoundError("missing pinned weights")):
            self.assertEqual(probe.run_probe("hhem-2.1", output, self.root / "models"), 1)
        raw, normalized, manifest, summary = self.assert_complete_linked_evidence(output)
        self.assertEqual(manifest["state"], "completed_with_errors")
        self.assertEqual(summary["counts"], {"ok": 0, "abstain": 0, "error": 2})
        self.assertEqual(summary["correct"], 0)
        self.assertEqual(summary["coverage"], 0)
        self.assertEqual(summary["known_model_calls"], 0)
        for original, result in zip(raw, normalized):
            self.assertEqual(original["error"]["stage"], "load")
            self.assertEqual(original["error"]["message"], "missing pinned weights")
            self.assertEqual(result["status"], "error")
            self.assertIsNone(result["verdict"])
            self.assertTrue(result["escalation_requested"])

    def test_malformed_model_manifest_is_recorded_as_load_failure(self):
        models = self.root / "models"
        models.mkdir()
        (models / "manifest.json").write_text("{malformed")
        output = self.root / "manifest-failure"
        with patch.object(probe, "load_candidate") as loader:
            self.assertEqual(probe.run_probe("hhem-2.1", output, models), 1)
            loader.assert_not_called()
        raw, normalized, manifest, summary = self.assert_complete_linked_evidence(output)
        self.assertEqual(summary["counts"]["error"], 2)
        self.assertEqual(manifest["load_error"]["type"], "JSONDecodeError")

    def test_invalid_resource_values_are_preserved_as_errors(self):
        for field, value in (("input_tokens", float("nan")), ("model_calls", -1)):
            with self.subTest(field=field):
                adapter = self.candidate()
                adapter.infer.return_value[field] = value
                output = self.root / field
                with patch.object(probe, "load_candidate", return_value=adapter):
                    self.assertEqual(probe.run_probe("hhem-2.1", output, self.root / "models"), 1)
                _, records, _, summary = self.assert_complete_linked_evidence(output)
                self.assertEqual(summary["counts"]["error"], 2)
                self.assertTrue(all(r["verdict"] is None for r in records))

    def test_inference_failure_is_preserved_and_later_fixtures_still_run(self):
        output = self.root / "inference-failure"
        native = {"support_score": 0.1, "logits": [1, 0], "input_tokens": 10, "model_calls": 1}
        adapter = self.candidate(side_effect=[RuntimeError("forward pass failed"), native])
        with patch.object(probe, "load_candidate", return_value=adapter):
            self.assertEqual(probe.run_probe("hhem-2.1", output, self.root / "models"), 1)
        raw, normalized, manifest, summary = self.assert_complete_linked_evidence(output)
        self.assertEqual(raw[0]["error"]["message"], "forward pass failed")
        self.assertEqual(raw[1]["native_output"], native)
        self.assertEqual([record["status"] for record in normalized], ["error", "ok"])
        self.assertIsNone(normalized[0]["resources"]["model_calls"])
        self.assertEqual(summary["unknown_call_count_records"], 1)
        self.assertEqual(summary["known_model_calls"], 1)
        self.assertEqual(summary["correct"], 1)
        self.assertEqual(summary["coverage"], 0.5)

    def test_abstention_preserves_available_token_count_and_zero_model_calls(self):
        output = self.root / "bounded-abstention"
        adapter = self.candidate(side_effect=probe_candidates.CandidateAbstention(
            "input_token_limit_exceeded", input_tokens=513))
        with patch.object(probe, "load_candidate", return_value=adapter):
            self.assertEqual(probe.run_probe("hhem-2.1", output, self.root / "models"), 0)
        raw, normalized, manifest, summary = self.assert_complete_linked_evidence(output)
        self.assertEqual(summary["counts"], {"ok": 0, "abstain": 2, "error": 0})
        self.assertEqual(summary["coverage"], 0)
        for original, result in zip(raw, normalized):
            self.assertEqual(original["abstention"], "input_token_limit_exceeded")
            self.assertEqual(result["status"], "abstain")
            self.assertEqual(result["resources"]["input_tokens"], 513)
            self.assertEqual(result["resources"]["model_calls"], 0)
            self.assertIsNone(result["verdict"])

    def test_nonfinite_native_values_become_errors_without_invalid_json(self):
        output = self.root / "invalid-native"
        adapter = self.candidate()
        adapter.infer.return_value["logits"] = [float("nan"), 1.0]
        with patch.object(probe, "load_candidate", return_value=adapter):
            self.assertEqual(probe.run_probe("hhem-2.1", output, self.root / "models"), 1)
        raw, normalized, manifest, summary = self.assert_complete_linked_evidence(output)
        self.assertEqual(summary["counts"]["error"], len(self.records))
        for original, result in zip(raw, normalized):
            self.assertIsNone(original["native_output"])
            self.assertIn("nan", original["native_output_repr"])
            self.assertEqual(original["error"]["type"], "ValueError")
            self.assertEqual(result["status"], "error")
            self.assertIsNone(result["verdict"])


if __name__ == "__main__":
    unittest.main()
