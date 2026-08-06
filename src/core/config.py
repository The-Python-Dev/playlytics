# src/core/config.py

"""
Single source of truth for all analyzer constants.

This module defines:
- Accuracy thresholds
- K/D thresholds
- Sample size minimum
- Input limits (max kills, max deaths)
- Supported weapon list
- Weapon name aliases (e.g. 'ar' -> 'assault')

All values match V2.9 behavior exactly.
Any threshold or limit change must be made here.
"""

from typing import Dict, Tuple
from src.models.configuration import Configuration


# ---------------------------------------------------------------------
# Accuracy thresholds
# ---------------------------------------------------------------------

LOW_ACCURACY:  float = 20.0
MID_ACCURACY:  float = 40.0
HIGH_ACCURACY: float = 50.0


# ---------------------------------------------------------------------
# K/D thresholds
# ---------------------------------------------------------------------

WEAK_KD:   float = 1.0
STRONG_KD: float = 2.0


# ---------------------------------------------------------------------
# Sample size
# ---------------------------------------------------------------------

MIN_SAMPLE_SIZE: int = 5


# ---------------------------------------------------------------------
# Input limits
# ---------------------------------------------------------------------

MAX_KILLS:  int = 200
MAX_DEATHS: int = 200


# ---------------------------------------------------------------------
# Weapons
# ---------------------------------------------------------------------

SUPPORTED_WEAPONS: Tuple[str, ...] = (
    "sniper",
    "smg",
    "assault",
    "lmg",
    "shotgun",
)

WEAPON_ALIASES: Dict[str, str] = {
    "ar": "assault",
}


# ---------------------------------------------------------------------
# Factory
# ---------------------------------------------------------------------

def get_default_configuration() -> Configuration:
    """
    Build the default Configuration object used by the analyzer.

    Returns:
        Configuration populated with the constants defined in this module.
    """
    return Configuration(
        low_accuracy=LOW_ACCURACY,
        mid_accuracy=MID_ACCURACY,
        high_accuracy=HIGH_ACCURACY,
        weak_kd=WEAK_KD,
        strong_kd=STRONG_KD,
        min_sample_size=MIN_SAMPLE_SIZE,
        max_kills=MAX_KILLS,
        max_deaths=MAX_DEATHS,
        supported_weapons=SUPPORTED_WEAPONS,
    )