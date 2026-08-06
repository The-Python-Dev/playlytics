# tests/test_validation/test_boundaries.py

import pytest
from src.validation.boundaries import (
    check_kills,
    check_deaths,
    check_accuracy,
    check_weapon,
    check_all,
)
from src.core.config import get_default_configuration


@pytest.fixture
def config():
    return get_default_configuration()


# ---------------------------------------------------------------------
# check_kills
# ---------------------------------------------------------------------

def test_check_kills_valid_returns_none(config):
    assert check_kills("10", config) is None


def test_check_kills_zero_is_valid(config):
    assert check_kills("0", config) is None


def test_check_kills_at_max_is_valid(config):
    assert check_kills("200", config) is None


def test_check_kills_empty_returns_error(config):
    assert check_kills("", config) == "Kills is required."


def test_check_kills_non_numeric_returns_error(config):
    assert check_kills("abc", config) == "Kills must be a whole number."


def test_check_kills_negative_returns_error(config):
    assert check_kills("-5", config) == "Kills cannot be negative."


def test_check_kills_above_max_returns_error(config):
    assert check_kills("201", config) == "Kills cannot exceed 200."


def test_check_kills_extreme_value_returns_error(config):
    assert check_kills("10000", config) == "Kills cannot exceed 200."


def test_check_kills_float_input_returns_error(config):
    # float strings are not valid for kills (integers only)
    assert check_kills("5.5", config) == "Kills must be a whole number."


# ---------------------------------------------------------------------
# check_deaths
# ---------------------------------------------------------------------

def test_check_deaths_valid_returns_none(config):
    assert check_deaths("5", config) is None


def test_check_deaths_zero_is_valid(config):
    assert check_deaths("0", config) is None


def test_check_deaths_empty_returns_error(config):
    assert check_deaths("", config) == "Deaths is required."


def test_check_deaths_negative_returns_error(config):
    assert check_deaths("-3", config) == "Deaths cannot be negative."


def test_check_deaths_above_max_returns_error(config):
    assert check_deaths("300", config) == "Deaths cannot exceed 200."


# ---------------------------------------------------------------------
# check_accuracy
# ---------------------------------------------------------------------

def test_check_accuracy_valid_returns_none(config):
    assert check_accuracy("45.5", config) is None


def test_check_accuracy_zero_is_valid(config):
    assert check_accuracy("0", config) is None


def test_check_accuracy_max_is_valid(config):
    assert check_accuracy("100", config) is None


def test_check_accuracy_empty_returns_error(config):
    assert check_accuracy("", config) == "Accuracy is required."


def test_check_accuracy_non_numeric_returns_error(config):
    assert check_accuracy("abc", config) == "Accuracy must be a number."


def test_check_accuracy_negative_returns_error(config):
    assert check_accuracy("-1", config) == "Accuracy cannot be negative."


def test_check_accuracy_above_100_returns_error(config):
    assert check_accuracy("140", config) == "Accuracy cannot exceed 100."


def test_check_accuracy_integer_input_is_valid(config):
    assert check_accuracy("50", config) is None


# ---------------------------------------------------------------------
# check_weapon
# ---------------------------------------------------------------------

def test_check_weapon_sniper_is_valid(config):
    assert check_weapon("sniper", config) is None


def test_check_weapon_assault_is_valid(config):
    assert check_weapon("assault", config) is None


def test_check_weapon_smg_is_valid(config):
    assert check_weapon("smg", config) is None


def test_check_weapon_lmg_is_valid(config):
    assert check_weapon("lmg", config) is None


def test_check_weapon_shotgun_is_valid(config):
    assert check_weapon("shotgun", config) is None


def test_check_weapon_empty_returns_error(config):
    assert check_weapon("", config) == "Weapon is required."


def test_check_weapon_unknown_returns_error(config):
    result = check_weapon("rocketbanana", config)
    assert "Unknown weapon" in result
    assert "rocketbanana" in result


def test_check_weapon_lists_supported_in_error(config):
    result = check_weapon("bazooka", config)
    assert "sniper" in result
    assert "assault" in result


# ---------------------------------------------------------------------
# check_all
# ---------------------------------------------------------------------

def test_check_all_valid_input_returns_empty_list(config):
    normalized = {
        "kills":    "10",
        "deaths":   "5",
        "accuracy": "45.5",
        "weapon":   "assault",
    }
    assert check_all(normalized, config) == []


def test_check_all_collects_multiple_errors(config):
    normalized = {
        "kills":    "-5",
        "deaths":   "300",
        "accuracy": "150",
        "weapon":   "rocketbanana",
    }
    errors = check_all(normalized, config)
    assert len(errors) == 4


def test_check_all_missing_fields_returns_errors(config):
    normalized = {
        "kills":    "",
        "deaths":   "",
        "accuracy": "",
        "weapon":   "",
    }
    errors = check_all(normalized, config)
    assert len(errors) == 4
    assert any("Kills" in e for e in errors)
    assert any("Deaths" in e for e in errors)
    assert any("Accuracy" in e for e in errors)
    assert any("Weapon" in e for e in errors)


def test_check_all_partial_failure(config):
    normalized = {
        "kills":    "10",
        "deaths":   "-3",
        "accuracy": "45.5",
        "weapon":   "assault",
    }
    errors = check_all(normalized, config)
    assert len(errors) == 1
    assert "Deaths cannot be negative" in errors[0]


# ---------------------------------------------------------------------
# V2.9 regression cases
# ---------------------------------------------------------------------

def test_v29_case_b4_valid_max_kills(config):
    # V2.9 case B4: 200 kills should be valid
    assert check_kills("200", config) is None


def test_v29_case_b5_over_max_kills(config):
    # V2.9 case B5: 201 kills should be rejected
    assert check_kills("201", config) is not None


def test_v29_case_n1_negative_kills(config):
    # V2.9 case N1
    assert check_kills("-3", config) is not None


def test_v29_case_n2_accuracy_above_100(config):
    # V2.9 case N2
    assert check_accuracy("140", config) is not None


def test_v29_case_n4_extreme_values(config):
    # V2.9 case N4
    assert check_kills("10000", config) is not None
    assert check_deaths("3000", config) is not None