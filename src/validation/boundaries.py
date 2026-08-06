# src/validation/boundaries.py

"""
Boundary checks for normalized input.

Parses normalized string values into numbers and verifies they
fall within acceptable ranges. Returns human-readable error
messages instead of raising exceptions, so multiple errors can
be collected and shown to the user at once.

Boundaries never mutate input. They only inspect and report.
"""

from typing import Dict, List, Optional
from src.models.configuration import Configuration
from src.core.logger import get_logger

logger = get_logger(__name__)


# ---------------------------------------------------------------------
# Individual checks
# ---------------------------------------------------------------------

def check_kills(raw: str, config: Configuration) -> Optional[str]:
    """
    Validate the kills field.

    Args:
        raw:    Normalized kills string.
        config: Configuration with max_kills limit.

    Returns:
        Error message string if invalid, None if valid.
    """
    if raw == "":
        return "Kills is required."

    try:
        value = int(raw)
    except ValueError:
        return "Kills must be a whole number."

    if value < 0:
        return "Kills cannot be negative."

    if value > config.max_kills:
        return f"Kills cannot exceed {config.max_kills}."

    return None


def check_deaths(raw: str, config: Configuration) -> Optional[str]:
    """
    Validate the deaths field.

    Args:
        raw:    Normalized deaths string.
        config: Configuration with max_deaths limit.

    Returns:
        Error message string if invalid, None if valid.
    """
    if raw == "":
        return "Deaths is required."

    try:
        value = int(raw)
    except ValueError:
        return "Deaths must be a whole number."

    if value < 0:
        return "Deaths cannot be negative."

    if value > config.max_deaths:
        return f"Deaths cannot exceed {config.max_deaths}."

    return None


def check_accuracy(raw: str, config: Configuration) -> Optional[str]:
    """
    Validate the accuracy field.

    Args:
        raw:    Normalized accuracy string.
        config: Configuration (unused, present for API consistency).

    Returns:
        Error message string if invalid, None if valid.
    """
    if raw == "":
        return "Accuracy is required."

    try:
        value = float(raw)
    except ValueError:
        return "Accuracy must be a number."

    if value < 0.0:
        return "Accuracy cannot be negative."

    if value > 100.0:
        return "Accuracy cannot exceed 100."

    return None


def check_weapon(raw: str, config: Configuration) -> Optional[str]:
    """
    Validate the weapon field.

    Args:
        raw:    Normalized weapon string (already lowercased and aliased).
        config: Configuration with supported_weapons list.

    Returns:
        Error message string if invalid, None if valid.
    """
    if raw == "":
        return "Weapon is required."

    if raw not in config.supported_weapons:
        supported = ", ".join(config.supported_weapons)
        return f"Unknown weapon: '{raw}'. Supported: {supported}."

    return None


# ---------------------------------------------------------------------
# Combined check
# ---------------------------------------------------------------------

def check_all(
    normalized_input: Dict[str, str],
    config: Configuration,
) -> List[str]:
    """
    Run every boundary check and return all error messages.

    Args:
        normalized_input: Dict with keys 'kills', 'deaths', 'accuracy',
                          'weapon' as normalized strings.
        config:           Configuration with limits and supported weapons.

    Returns:
        List of error messages. Empty list if all checks passed.
    """
    errors: List[str] = []

    kills_error = check_kills(normalized_input.get("kills", ""), config)
    if kills_error:
        errors.append(kills_error)

    deaths_error = check_deaths(normalized_input.get("deaths", ""), config)
    if deaths_error:
        errors.append(deaths_error)

    accuracy_error = check_accuracy(normalized_input.get("accuracy", ""), config)
    if accuracy_error:
        errors.append(accuracy_error)

    weapon_error = check_weapon(normalized_input.get("weapon", ""), config)
    if weapon_error:
        errors.append(weapon_error)

    if errors:
        logger.debug("Boundary check failed with %d error(s)", len(errors))

    return errors