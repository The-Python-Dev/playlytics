# src/models/configuration.py

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class Configuration:
    """
    Immutable configuration container for the analyzer.

    Defines all runtime thresholds, limits, and supported values.
    Passed as a dependency into rules, weapon analyzers, and validators.

    Actual values are defined in core/config.py.
    This class defines only the shape and enforces immutability.

    Attributes:
        low_accuracy:      Threshold below which aim is considered weak.
        mid_accuracy:      Threshold above which aim is considered strong.
        high_accuracy:     Threshold for exceptional aim performance.
        weak_kd:           Threshold below which K/D indicates poor survival.
        strong_kd:         Threshold above which K/D indicates strong combat.
        min_sample_size:   Minimum kills + deaths for reliable analysis.
        max_kills:         Upper limit for plausible kill count.
        max_deaths:        Upper limit for plausible death count.
        supported_weapons: Tuple of canonical weapon names accepted
                           by the analyzer.
    """

    low_accuracy:  float
    mid_accuracy:  float
    high_accuracy: float

    weak_kd:   float
    strong_kd: float

    min_sample_size: int

    max_kills:  int
    max_deaths: int

    supported_weapons: Tuple[str, ...]