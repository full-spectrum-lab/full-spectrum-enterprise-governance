#!/usr/bin/env python3
"""Validate public synthetic case packages without claiming runtime execution."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / "cases" / "industrial-tightening-evidence-gap"
NAMES = ("synthetic-input.json", "subject-manifest.json", "profile.json", "expected-observation.json", "evidence-manifest.json")


def report(errors: list[str]) -> int:
    for error in errors:
        print(f"[FAIL] {error}")
    return 1


def main() -> int:
    errors: list[str] = []
    documents: dict[str, dict] = {}
    for name in NAMES:
        path = CASE / name
        if not path.is_file():
            errors.append(f"missing {path.relative_to(ROOT)}")
            continue
        try:
            documents[name] = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"invalid JSON {name}: {exc}")
    for name in ("README.md", "human-review.md"):
        if not (CASE / name).is_file():
            errors.append(f"missing cases/industrial-tightening-evidence-gap/{name}")
    if errors:
        return report(errors)

    raw = documents["synthetic-input.json"]
    subjects = documents["subject-manifest.json"]
    profile = documents["profile.json"]
    observation = documents["expected-observation.json"]
    evidence = documents["evidence-manifest.json"]
    boundary = profile.get("execution_boundary", {})
    versions = evidence.get("version_refs", {})

    checks = [
        (raw.get("classification") == "SYNTHETIC_DESIGNED_CASE", "input classification drifted"),
        (raw.get("collection_mode") == "AUTHORIZED_READ_ONLY", "input must remain authorized read-only"),
        (raw.get("customer_data") is False, "fixture must not claim customer data"),
        (boundary.get("observation_only") is True, "profile must remain observation-only"),
        (boundary.get("automatic_business_action") is False, "automatic business action must remain off"),
        (boundary.get("production_writeback") is False, "production writeback must remain off"),
        (observation.get("state") == "ACTION_PROPOSED", "expected state must stop before RESOLVED/CLOSED"),
        (observation.get("automatic_action") is None, "expected observation must not contain an automatic action"),
        (evidence.get("production_evidence") is False, "fixture must not claim production evidence"),
        (versions.get("adapter") == "NOT_IMPLEMENTED", "adapter status must remain explicit"),
        (versions.get("engine") == "NOT_EXECUTED", "engine execution must not be implied"),
        (versions.get("observer") == "NOT_EXECUTED", "Observer execution must not be implied"),
    ]
    errors.extend(message for passed, message in checks if not passed)

    prohibited: set[str] = set()
    for subject in subjects.get("subjects", []):
        prohibited.update(subject.get("prohibited_capabilities", []))
    for capability in ("write_mes", "write_qms", "control_plc", "stop_line", "release_quality"):
        if capability not in prohibited:
            errors.append(f"missing prohibited capability: {capability}")

    for source in evidence.get("source_refs", []):
        path_part = source.get("fact_path", "").split("#", 1)[0]
        if not path_part or not (CASE / path_part).is_file():
            errors.append(f"unresolvable evidence source: {source}")

    if errors:
        return report(errors)
    print("[PASS] industrial-tightening-evidence-gap: designed fixture and safety boundary validated")
    print("[INFO] this gate does not claim Adapter, Engine, Observer, pilot, or production validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
