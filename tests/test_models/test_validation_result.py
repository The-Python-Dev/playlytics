# tests/test_models/test_validation_result.py

import pytest
from dataclasses import FrozenInstanceError
from src.models.validation_result import ValidationResult
from src.models.player_stats import PlayerStats


def _sample_stats():
    return PlayerStats(kills=10, deaths=4, accuracy=45.0, weapon="assault")


def test_validation_result_valid_case():
    result = ValidationResult(
        is_valid=True,
        data=_sample_stats(),
    )
    assert result.is_valid is True
    assert result.data is not None
    assert result.data.kills == 10
    assert result.errors == []


def test_validation_result_invalid_case():
    result = ValidationResult(
        is_valid=False,
        errors=["Kills cannot be negative."],
    )
    assert result.is_valid is False
    assert result.data is None
    assert len(result.errors) == 1


def test_validation_result_multiple_errors():
    result = ValidationResult(
        is_valid=False,
        errors=[
            "Kills cannot be negative.",
            "Accuracy must be between 0 and 100.",
            "Unknown weapon: rocketbanana.",
        ],
    )
    assert result.is_valid is False
    assert len(result.errors) == 3
    assert "rocketbanana" in result.errors[2]


def test_validation_result_defaults():
    result = ValidationResult(is_valid=True)
    assert result.data is None
    assert result.errors == []


def test_validation_result_is_frozen():
    result = ValidationResult(is_valid=True, data=_sample_stats())
    with pytest.raises(FrozenInstanceError):
        result.is_valid = False


def test_validation_result_default_factory_isolation():
    # Two separate instances should not share the same errors list
    a = ValidationResult(is_valid=False)
    b = ValidationResult(is_valid=False)
    a.errors.append("Error A")
    assert len(b.errors) == 0


def test_validation_result_fields_are_correct_types():
    result = ValidationResult(
        is_valid=True,
        data=_sample_stats(),
        errors=[],
    )
    assert isinstance(result.is_valid, bool)
    assert isinstance(result.data, PlayerStats)
    assert isinstance(result.errors, list)