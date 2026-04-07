"""
Governance Metrics Calculator - GAIF-4 metric collection and reporting
Calculates T1PR, CFR, and basic GDR from pipeline logs.
"""

import json
from dataclasses import dataclass
from pathlib import Path
from datetime import datetime, timezone


THRESHOLDS = {
    "t1pr": {"safe": 0.05, "critical": 0.15},
    "cfr": {"safe": 0.00, "critical": 0.01},
    "emr": {"safe": 0.05, "critical": 0.15},
    "gdr": {"safe": 0.03, "critical": 0.05},
}


@dataclass
class GovernanceReport:
    t1pr: float
    cfr: float
    total_safety_events: int
    total_compliance_events: int
    safety_failures: int
    compliance_failures: int
    period_start: str
    period_end: str

    def summary(self) -> str:
        lines = [
            "=" * 50,
            "GAIF-4 GOVERNANCE HEALTH REPORT",
            "=" * 50,
            f"Period: {self.period_start} to {self.period_end}",
            "",
            f"T1PR (Type-1 Pass Rate):     {self.t1pr:.4f}  {self._status('t1pr', self.t1pr)}",
            f"  Total evaluated:           {self.total_safety_events}",
            f"  Failed checks:             {self.safety_failures}",
            "",
            f"CFR (Compliance Failure Rate): {self.cfr:.4f}  {self._status('cfr', self.cfr)}",
            f"  Total routed:              {self.total_compliance_events}",
            f"  Compliance violations:     {self.compliance_failures}",
            "",
            "=" * 50,
        ]
        return "\n".join(lines)

    def _status(self, metric: str, value: float) -> str:
        t = THRESHOLDS[metric]
        if value <= t["safe"]:
            return "[SAFE]"
        elif value <= t["critical"]:
            return "[WARNING]"
        else:
            return "[CRITICAL]"

    def to_dict(self) -> dict:
        return {
            "t1pr": self.t1pr,
            "cfr": self.cfr,
            "t1pr_status": self._status("t1pr", self.t1pr),
            "cfr_status": self._status("cfr", self.cfr),
            "total_safety_events": self.total_safety_events,
            "total_compliance_events": self.total_compliance_events,
            "safety_failures": self.safety_failures,
            "compliance_failures": self.compliance_failures,
            "period_start": self.period_start,
            "period_end": self.period_end,
        }


class GovernanceMetrics:
    def __init__(self, safety_log_path: str = None, compliance_log_path: str = None):
        self.safety_log_path = safety_log_path
        self.compliance_log_path = compliance_log_path

    def calculate(self) -> GovernanceReport:
        safety_events = self._read_log(self.safety_log_path) if self.safety_log_path else []
        compliance_events = self._read_log(self.compliance_log_path) if self.compliance_log_path else []

        # T1PR: proportion of events where bad outputs passed through
        total_safety = len(safety_events)
        safety_failures = sum(1 for e in safety_events if e.get("t1pr_increment", False))
        t1pr = safety_failures / total_safety if total_safety > 0 else 0.0

        # CFR: proportion of compliance violations
        total_compliance = len(compliance_events)
        compliance_failures = sum(1 for e in compliance_events if e.get("violation", False))
        cfr = compliance_failures / total_compliance if total_compliance > 0 else 0.0

        # Period
        all_events = safety_events + compliance_events
        timestamps = [e.get("timestamp", "") for e in all_events if e.get("timestamp")]
        period_start = min(timestamps) if timestamps else "N/A"
        period_end = max(timestamps) if timestamps else "N/A"

        return GovernanceReport(
            t1pr=t1pr,
            cfr=cfr,
            total_safety_events=total_safety,
            total_compliance_events=total_compliance,
            safety_failures=safety_failures,
            compliance_failures=compliance_failures,
            period_start=period_start,
            period_end=period_end,
        )

    def calculate_gdr(self, current: GovernanceReport, baseline: GovernanceReport) -> float:
        """Compare current metrics against a baseline to detect governance decay."""
        if baseline.t1pr == 0 and baseline.cfr == 0:
            return 0.0

        t1pr_drift = max(0, current.t1pr - baseline.t1pr)
        cfr_drift = max(0, current.cfr - baseline.cfr)

        # GDR is the average drift across metrics
        # Weight CFR higher since any compliance failure is critical
        gdr = (t1pr_drift + cfr_drift * 2) / 2
        return gdr

    def _read_log(self, path: str) -> list:
        log_path = Path(path)
        if not log_path.exists():
            return []
        events = []
        with open(log_path) as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        events.append(json.loads(line))
                    except json.JSONDecodeError:
                        continue
        return events


if __name__ == "__main__":
    # Demo with sample data
    sample_safety_log = Path("./logs/demo_safety.jsonl")
    sample_safety_log.parent.mkdir(parents=True, exist_ok=True)

    now = datetime.now(timezone.utc).isoformat()
    sample_events = [
        {"timestamp": now, "gate_id": "gate-1", "passed": True, "failed_checks": [], "t1pr_increment": False},
        {"timestamp": now, "gate_id": "gate-1", "passed": True, "failed_checks": [], "t1pr_increment": False},
        {"timestamp": now, "gate_id": "gate-1", "passed": False, "failed_checks": ["phi_detection"], "t1pr_increment": True},
        {"timestamp": now, "gate_id": "gate-1", "passed": True, "failed_checks": [], "t1pr_increment": False},
        {"timestamp": now, "gate_id": "gate-1", "passed": True, "failed_checks": [], "t1pr_increment": False},
    ]

    with open(sample_safety_log, "w") as f:
        for event in sample_events:
            f.write(json.dumps(event) + "\n")

    metrics = GovernanceMetrics(safety_log_path=str(sample_safety_log))
    report = metrics.calculate()
    print(report.summary())
