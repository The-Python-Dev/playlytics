# src/analyzers/metrics_calculator.py

"""
Metrics calculator for Playlytics V3.

Computes derived statistics (K/D ratio, total sample size,
and small sample flag) from validated PlayerStats.

All calculation logic matches V2.9 behavior exactly.
"""

from typing import Optional
from src.models.player_stats import PlayerStats
from src.models.metrics import Metrics
from src.models.configuration import Configuration
from src.core.config import get_default_configuration
from src.core.logger import get_logger

logger = get_logger(__name__)


def calculate_metrics(
    stats: PlayerStats,
    config: Optional[Configuration] = None,
) -> Metrics:
    """
    Calculate derived performance metrics from validated player stats.

    Args:
        stats:  Validated PlayerStats object.
        config: Optional Configuration instance. Defaults to default config.

    Returns:
        Metrics object containing kd_ratio, sample_size, and is_small_sample flag.
    """
    active_config = config or get_default_configuration()

    # 1. K/D Ratio calculation (zero deaths protection)
    if stats.deaths == 0:
        kd = float(stats.kills)
    else:
        kd = round(stats.kills / stats.deaths, 2)

    # 2. Sample size
    sample_size = stats.kills + stats.deaths

    # 3. Small sample detection
    is_small = sample_size < active_config.min_sample_size

    logger.debug(
        "Computed metrics: K/D=%.2f, Sample Size=%d, Small Sample=%s",
        kd,
        sample_size,
        is_small,
    )

    return Metrics(
        kd_ratio=kd,
        sample_size=sample_size,
        is_small_sample=is_small,
    )