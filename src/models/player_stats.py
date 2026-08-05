# src/models/player_stats.py

from dataclasses import dataclass


@dataclass(frozen=True)
class PlayerStats:
    """
    Container for validated raw player input from a single match.

    Holds only what the user provided. No computed values.
    Derived values such as K/D ratio live in the Metrics model.

    This class is frozen. Analysis code must never mutate input data.

    Attributes:
        kills:    Number of kills in the match. Non-negative integer.
        deaths:   Number of deaths in the match. Non-negative integer.
        accuracy: Accuracy percentage. Float between 0.0 and 100.0.
        weapon:   Canonical weapon name (e.g. 'sniper', 'assault').
    """

    kills:    int
    deaths:   int
    accuracy: float
    weapon:   str