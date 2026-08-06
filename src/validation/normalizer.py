# src/validation/normalizer.py

"""
Input normalization for the validation layer.

Transforms raw user input into a canonical form before boundary
checks run. Handles whitespace, casing, and weapon aliases.

Normalization never fails. If input cannot be normalized cleanly,
the original value is returned and boundary validation rejects it.
"""

from typing import Dict
from src.core.config import WEAPON_ALIASES
from src.core.logger import get_logger

logger = get_logger(__name__)


def normalize_weapon(raw: str) -> str:
    """
    Normalize a weapon name string.

    Strips leading and trailing whitespace, converts to lowercase,
    and resolves known aliases (e.g. 'ar' -> 'assault').

    Args:
        raw: Raw weapon string from user input.

    Returns:
        Canonical weapon name. If input is not a known alias,
        the cleaned (stripped and lowercased) string is returned
        as-is for boundary validation to check.
    """
    if not isinstance(raw, str):
        return ""

    cleaned = raw.strip().lower()

    if cleaned in WEAPON_ALIASES:
        canonical = WEAPON_ALIASES[cleaned]
        logger.debug("Weapon alias resolved: '%s' -> '%s'", cleaned, canonical)
        return canonical

    return cleaned


def normalize_number(raw: str) -> str:
    """
    Normalize a numeric string.

    Strips whitespace only. Does not attempt to parse or validate
    the value as a number. Parsing is the boundary layer's job.

    Args:
        raw: Raw numeric string from user input.

    Returns:
        Whitespace-stripped string. Returns empty string if input
        is not a string type.
    """
    if not isinstance(raw, str):
        return ""

    return raw.strip()


def normalize_input(
    kills: str,
    deaths: str,
    accuracy: str,
    weapon: str,
) -> Dict[str, str]:
    """
    Normalize all four input fields at once.

    Convenience wrapper that applies normalize_number and
    normalize_weapon to the appropriate fields.

    Args:
        kills:    Raw kills input string.
        deaths:   Raw deaths input string.
        accuracy: Raw accuracy input string.
        weapon:   Raw weapon input string.

    Returns:
        Dictionary with normalized values for each field.
    """
    return {
        "kills":    normalize_number(kills),
        "deaths":   normalize_number(deaths),
        "accuracy": normalize_number(accuracy),
        "weapon":   normalize_weapon(weapon),
    }