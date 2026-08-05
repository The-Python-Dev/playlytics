# src/models/validation_result.py

from dataclasses import dataclass, field
from typing import List, Optional
from src.models.player_stats import PlayerStats


@dataclass(frozen=True)
class ValidationResult:
    """
    Output of the validation layer.

    Produced by validation/validator.py.
    Consumed by the controller to decide whether to proceed with analysis.

    When is_valid is True, data contains a clean PlayerStats object.
    When is_valid is False, data is None and errors contains
    human-readable descriptions of every validation failure.

    Attributes:
        is_valid: True if all input passed validation.
        data:     Clean PlayerStats when valid, None when invalid.
        errors:   List of human-readable error messages.
                  Empty when validation succeeded.
    """

    is_valid: bool
    data:     Optional[PlayerStats] = None
    errors:   List[str] = field(default_factory=list)