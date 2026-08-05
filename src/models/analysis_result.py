# src/models/analysis_result.py

from dataclasses import dataclass, field
from typing import List
from src.models.player_stats import PlayerStats
from src.models.metrics import Metrics
from src.models.rule_result import RuleResult


@dataclass(frozen=True)
class AnalysisResult:
    """
    Complete output of the analysis pipeline.

    Produced by the analyzer engine.
    Wrapped by the controller into a ControllerResult.
    Consumed by the UI renderer to display the full analysis.

    Attributes:
        stats:        Original validated player input.
        metrics:      Computed values (K/D, sample size, small sample flag).
        rule_results: All rule outputs from general and weapon analysis,
                      in a single flat list.
        summary:      One-line human-readable overview of the analysis.
    """

    stats:        PlayerStats
    metrics:      Metrics
    rule_results: List[RuleResult] = field(default_factory=list)
    summary:      str = ""