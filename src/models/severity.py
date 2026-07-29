# src/models/severity.py

from enum import Enum


class Severity(Enum):
    """
    Classification levels for all analysis and validation results.

    Used by RuleResult, ValidationResult, and ControllerResult
    to communicate meaning to the UI layer without string matching.

    Levels:
        SUCCESS: Positive outcome. Player performed well in this area.
        INFO:    Neutral observation. No problem detected.
        WARNING: Area needs improvement. Not a critical failure.
        ERROR:   Invalid input, unsupported value, or unexpected failure.
    """

    SUCCESS = "success"
    INFO    = "info"
    WARNING = "warning"
    ERROR   = "error"