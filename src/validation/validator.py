# src/validation/validator.py

"""
Validation orchestrator and boundary gate.

Combines normalization and boundary checks into a single clean call.
Converts raw string input into a typed, validated PlayerStats object.

This is the main entry point for the validation layer.
Never raises exceptions. Always returns a ValidationResult.
"""

from typing import Optional
from src.models.configuration import Configuration
from src.models.player_stats import PlayerStats
from src.models.validation_result import ValidationResult
from src.core.config import get_default_configuration
from src.core.logger import get_logger
from src.validation.normalizer import normalize_input
from src.validation.boundaries import check_all

logger = get_logger(__name__)


def validate_input(
    kills_raw: str,
    deaths_raw: str,
    accuracy_raw: str,
    weapon_raw: str,
    config: Optional[Configuration] = None,
) -> ValidationResult:
    """
    Validate raw match input from the user.

    1. Applies default configuration if none provided.
    2. Normalizes all input strings (strip, lowercase, alias resolution).
    3. Runs boundary checks against ranges and limits.
    4. Constructs a clean PlayerStats object if valid.
    5. Returns a ValidationResult container.

    Args:
        kills_raw:    Raw kills input string.
        deaths_raw:   Raw deaths input string.
        accuracy_raw: Raw accuracy percentage input string.
        weapon_raw:   Raw weapon name string.
        config:       Optional Configuration instance. Defaults to app config.

    Returns:
        ValidationResult with is_valid=True and data=PlayerStats if valid,
        or is_valid=False and errors list if invalid.
    """
    active_config = config or get_default_configuration()

    logger.debug(
        "Validating raw input: kills='%s', deaths='%s', accuracy='%s', weapon='%s'",
        kills_raw,
        deaths_raw,
        accuracy_raw,
        weapon_raw,
    )

    # 1. Normalize
    normalized = normalize_input(
        kills=kills_raw,
        deaths=deaths_raw,
        accuracy=accuracy_raw,
        weapon=weapon_raw,
    )

    # 2. Check Boundaries
    errors = check_all(normalized, active_config)

    if errors:
        logger.info("Validation failed with %d error(s)", len(errors))
        return ValidationResult(
            is_valid=False,
            data=None,
            errors=errors,
        )

    # 3. Build clean PlayerStats object (safe to parse now)
    stats = PlayerStats(
        kills=int(normalized["kills"]),
        deaths=int(normalized["deaths"]),
        accuracy=float(normalized["accuracy"]),
        weapon=normalized["weapon"],
    )

    logger.info(
        "Validation successful for weapon '%s' (K: %d, D: %d, Acc: %.1f%%)",
        stats.weapon,
        stats.kills,
        stats.deaths,
        stats.accuracy,
    )

    return ValidationResult(
        is_valid=True,
        data=stats,
        errors=[],
    )