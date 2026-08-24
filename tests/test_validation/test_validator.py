# tests/test_validation/test_validator.py

import pytest
from src.validation.validator import validate_input
from src.models.player_stats import PlayerStats
from src.models.validation_result import ValidationResult
from src.core.config import get_default_configuration


@pytest.fixture
def config():
    return get_default_configuration()


# ---------------------------------------------------------------------
# Valid cases
# ---------------------------------------------------------------------

def test_validate_input_valid_data():
    result = validate_input("10", "5", "45.5", "assault")
    assert result.is_valid is True
    assert isinstance(result.data, PlayerStats)
    assert result.data.kills == 10
    assert result.data.deaths == 5
    assert result.data.accuracy == 45.5
    assert result.data.weapon == "assault"
    assert result.errors == []


def test_validate_input_normalization_applied():
    # Whitespace + uppercase + alias "AR" -> "assault"
    result = validate_input("  10  ", "  5  ", "  50  ", "  AR  ")
    assert result.is_valid is True
    assert result.data.weapon == "assault"
    assert result.data.kills == 10


def test_validate_input_zero_values_valid():
    result = validate_input("0", "0", "0.0", "sniper")
    assert result.is_valid is True
    assert result.data.kills == 0
    assert result.data.deaths == 0
    assert result.data.accuracy == 0.0


def test_validate_input_boundary_max_kills(config):
    result = validate_input("200", "10", "50", "sniper", config=config)
    assert result.is_valid is True
    assert result.data.kills == 200


# ---------------------------------------------------------------------
# Invalid cases
# ---------------------------------------------------------------------

def test_validate_input_negative_kills():
    result = validate_input("-5", "5", "45.5", "assault")
    assert result.is_valid is False
    assert result.data is None
    assert len(result.errors) == 1
    assert "Kills cannot be negative" in result.errors[0]


def test_validate_input_unrealistic_kills(config):
    result = validate_input("201", "5", "45.5", "assault", config=config)
    assert result.is_valid is False
    assert any("cannot exceed 200" in e for e in result.errors)


def test_validate_input_invalid_accuracy_over_100():
    result = validate_input("10", "5", "140", "assault")
    assert result.is_valid is False
    assert any("Accuracy cannot exceed 100" in e for e in result.errors)


def test_validate_input_unknown_weapon():
    result = validate_input("10", "5", "45.5", "banana_gun")
    assert result.is_valid is False
    assert any("Unknown weapon" in e for e in result.errors)


def test_validate_input_multiple_errors_collected():
    result = validate_input("-10", "-5", "200", "banana_gun")
    assert result.is_valid is False
    assert len(result.errors) == 4


def test_validate_input_non_numeric_strings():
    result = validate_input("abc", "def", "xyz", "assault")
    assert result.is_valid is False
    assert len(result.errors) == 3


def test_validate_input_empty_strings():
    result = validate_input("", "", "", "")
    assert result.is_valid is False
    assert len(result.errors) == 4


# ---------------------------------------------------------------------
# V2.9 Test Case Integrations
# ---------------------------------------------------------------------

def test_v29_case_n3_trailing_space_alias():
    # V2.9 N3: "AR " -> normalized to "assault"
    result = validate_input("10", "5", "40", "AR ")
    assert result.is_valid is True
    assert result.data.weapon == "assault"


def test_v29_case_n4_absurd_inputs_rejected():
    # V2.9 N4: 10000 kills, 3000 deaths -> rejected
    result = validate_input("10000", "3000", "70", "sniper")
    assert result.is_valid is False
    assert len(result.errors) >= 2