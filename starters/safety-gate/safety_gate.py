"""
Safety Gate - Lightweight inter-agent safety checkpoint
Pattern 03: Multi-Agent Safety Gates

Place between any two agents in a pipeline to catch contamination at point of origin.
"""

import re
import json
import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path


@dataclass
class SafetyConfig:
    gate_id: str
    checks: list = field(default_factory=lambda: ["phi_detection", "toxicity_keywords", "confidence_floor"])
    action_on_fail: str = "block"
    confidence_threshold: float = 0.3
    log_path: str = "./logs/safety_gate.jsonl"


@dataclass
class GateResult:
    passed: bool
    content: str
    failed_checks: list
    gate_id: str
    timestamp: str


PHI_PATTERNS = [
    r'\b\d{3}-\d{2}-\d{4}\b',                    # SSN
    r'\b\d{3}\s\d{2}\s\d{4}\b',                   # SSN with spaces
    r'\b[A-Z]{2,3}\d{6,10}\b',                    # MRN
    r'\b\d{2}/\d{2}/\d{4}\b',                     # DOB
    r'\b\d{10}\b',                                 # Phone (10 digits)
    r'\b\(\d{3}\)\s?\d{3}-\d{4}\b',              # Phone (xxx) xxx-xxxx
    r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',  # Email
]

TOXICITY_KEYWORDS = [
    "kill", "harm", "abuse", "attack", "exploit",
    "illegal", "smuggle", "launder",
]


class SafetyGate:
    def __init__(self, config: SafetyConfig):
        self.config = config
        self.gate_id = config.gate_id
        self.total_evaluated = 0
        self.total_failed = 0
        self.total_passed_with_flags = 0

        Path(config.log_path).parent.mkdir(parents=True, exist_ok=True)
        self.logger = logging.getLogger(f"safety_gate.{config.gate_id}")

    def evaluate(self, content: str, metadata: dict = None) -> GateResult:
        failed_checks = []

        for check_name in self.config.checks:
            check_fn = getattr(self, f"_check_{check_name}", None)
            if check_fn and not check_fn(content):
                failed_checks.append(check_name)

        passed = len(failed_checks) == 0
        self.total_evaluated += 1

        if not passed:
            if self.config.action_on_fail == "block":
                self.total_failed += 1
            else:
                self.total_passed_with_flags += 1

        result = GateResult(
            passed=passed if self.config.action_on_fail == "block" else True,
            content=content if passed or self.config.action_on_fail == "flag" else "",
            failed_checks=failed_checks,
            gate_id=self.gate_id,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )

        self._log_decision(result, metadata)
        return result

    def _check_phi_detection(self, content: str) -> bool:
        for pattern in PHI_PATTERNS:
            if re.search(pattern, content):
                return False
        return True

    def _check_toxicity_keywords(self, content: str) -> bool:
        content_lower = content.lower()
        for keyword in TOXICITY_KEYWORDS:
            if keyword in content_lower:
                return False
        return True

    def _check_confidence_floor(self, content: str) -> bool:
        confidence_markers = ["i'm not sure", "i think maybe", "this might be wrong",
                              "i cannot verify", "uncertain", "possibly incorrect"]
        content_lower = content.lower()
        matches = sum(1 for m in confidence_markers if m in content_lower)
        return matches < 2

    def _check_length_anomaly(self, content: str) -> bool:
        word_count = len(content.split())
        return 5 < word_count < 5000

    def _check_contradiction_check(self, content: str) -> bool:
        contradiction_pairs = [
            ("is safe", "is dangerous"),
            ("no interaction", "severe interaction"),
            ("recommended", "contraindicated"),
        ]
        content_lower = content.lower()
        for a, b in contradiction_pairs:
            if a in content_lower and b in content_lower:
                return False
        return True

    def _log_decision(self, result: GateResult, metadata: dict = None):
        log_entry = {
            "timestamp": result.timestamp,
            "gate_id": result.gate_id,
            "passed": result.passed,
            "failed_checks": result.failed_checks,
            "action": self.config.action_on_fail,
            "t1pr_increment": not result.passed or len(result.failed_checks) > 0,
        }
        if metadata:
            log_entry["metadata"] = metadata

        with open(self.config.log_path, "a") as f:
            f.write(json.dumps(log_entry) + "\n")

    @property
    def t1pr(self) -> float:
        if self.total_evaluated == 0:
            return 0.0
        return self.total_passed_with_flags / self.total_evaluated


if __name__ == "__main__":
    config = SafetyConfig(
        gate_id="demo-gate",
        checks=["phi_detection", "toxicity_keywords", "confidence_floor"],
        action_on_fail="block",
    )
    gate = SafetyGate(config)

    # Test with clean input
    result = gate.evaluate("The patient should take 500mg of acetaminophen twice daily.")
    print(f"Clean input - Passed: {result.passed}")

    # Test with PHI
    result = gate.evaluate("Patient John Smith, SSN 123-45-6789, should take medication.")
    print(f"PHI input - Passed: {result.passed}, Failed: {result.failed_checks}")

    # Test with contradiction
    config2 = SafetyConfig(
        gate_id="demo-gate-2",
        checks=["contradiction_check"],
        action_on_fail="block",
    )
    gate2 = SafetyGate(config2)
    result = gate2.evaluate("This drug is safe for the patient. However, this drug is dangerous.")
    print(f"Contradiction - Passed: {result.passed}, Failed: {result.failed_checks}")

    print(f"\nGate T1PR: {gate.t1pr:.4f}")
