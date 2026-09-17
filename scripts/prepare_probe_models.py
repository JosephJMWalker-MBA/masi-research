#!/usr/bin/env python3
"""Fetch only the three pinned snapshots needed by the WP1 local probes."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from probe_candidates import MODEL_FILES, file_sha256


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model-root", type=Path, default=Path(".models"))
    args = parser.parse_args()
    model_root = args.model_root.resolve()
    os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"
    os.environ["HF_HOME"] = str(model_root / ".hf_home")
    from huggingface_hub import snapshot_download

    manifest = {
        "schema_version": 1,
        "prepared_at_utc": datetime.now(timezone.utc).isoformat(),
        "snapshots": {},
    }
    for snapshot_id, spec in MODEL_FILES.items():
        destination = model_root / snapshot_id
        snapshot_download(
            repo_id=spec["repo_id"], revision=spec["revision"],
            allow_patterns=spec["files"], local_dir=destination,
            max_workers=2,
        )
        files = {}
        for filename in spec["files"]:
            path = destination / filename
            files[filename] = {
                "sha256": file_sha256(path),
                "size_bytes": path.stat().st_size,
            }
        manifest["snapshots"][snapshot_id] = {
            "repo_id": spec["repo_id"],
            "revision": spec["revision"],
            "files": files,
        }
        print(f"Prepared {snapshot_id} at {spec['revision']}", flush=True)
    temporary = model_root / "manifest.json.tmp"
    temporary.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    temporary.replace(model_root / "manifest.json")
    print(f"Manifest: {model_root / 'manifest.json'}", flush=True)


if __name__ == "__main__":
    main()
