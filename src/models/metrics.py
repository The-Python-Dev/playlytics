# src/models/metrics.py

from dataclasses import dataclass


@dataclass(frozen=True)
class Metrics:
    """
    Container for computed values derived from PlayerStats.

    Produced by MetricsCalculator.
    Consumed by rules, weapon analyzers, and the UI.

    This class is frozen. Analysis code must never mutate metrics.

    Attributes:
        kd_ratio:        Kills divided by deaths. If deaths is zero,
                         equals kills (matches V2.9 behavior).
        sample_size:     Total kills plus deaths.
                         Represents match activity volume.
        is_small_sample: True when sample_size is below the minimum
                         threshold required for reliable classification.
    """

    kd_ratio:        float
    sample_size:     int
    is_small_sample: bool