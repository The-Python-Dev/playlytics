# src/models/rule_result.py

from dataclasses import dataclass
from typing import Optional
from src.models.severity import Severity


@dataclass
class RuleResult:
    """
    Represents the output of a single rule evaluation.

    Produced by every rule in the system.
    Consumed by the UI renderer to display result cards.

    Attributes:
        rule_name:  Identifier for the rule that produced this result.
        severity:   Classification level (SUCCESS, INFO, WARNING, ERROR).
        message:    Plain language result message shown to the user.
        suggestion: Optional corrective suggestion shown below the message.
        passed:     Whether the rule condition was met positively.
    """

    rule_name:  str
    severity:   Severity
    message:    str
    suggestion: Optional[str] = None
    passed:     bool = True