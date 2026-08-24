# src/rules/context.py

"""
Evaluation context passed to all analysis rules.

Bundles validated player stats, computed metrics, and system configuration
into a single immutable container.
"""

from dataclasses import dataclass
from src.models.player_stats import PlayerStats
from src.models.metrics import Metrics
from src.models.configuration import Configuration


@dataclass(frozen=True)
class RuleContext:
    """
    Immutable evaluation context passed to rules and weapon analyzers.

    Attributes:
        stats:   Validated PlayerStats from input.
        metrics: Computed Metrics (K/D, sample size, small sample flag).
        config:  System Configuration thresholds and limits.
    """

    stats:   PlayerStats
    metrics: Metrics
    config:  Configuration