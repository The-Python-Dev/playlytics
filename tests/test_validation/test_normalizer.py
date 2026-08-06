# tests/test_validation/test_normalizer.py

from src.validation.normalizer import (
    normalize_weapon,
    normalize_number,
    normalize_input,
)


# ---------------------------------------------------------------------
# normalize_weapon
# ---------------------------------------------------------------------

def test_normalize_weapon_lowercases():
    assert normalize_weapon("SNIPER") == "sniper"


def test_normalize_weapon_strips_whitespace():
    assert normalize_weapon("  sniper  ") == "sniper"


def test_normalize_weapon_handles_mixed_case_and_whitespace():
    assert normalize_weapon("  Sniper  ") == "sniper"


def test_normalize_weapon_resolves_ar_alias():
    assert normalize_weapon("ar") == "assault"


def test_normalize_weapon_resolves_uppercase_ar_alias():
    assert normalize_weapon("AR") == "assault"


def test_normalize_weapon_resolves_padded_ar_alias():
    assert normalize_weapon(" AR ") == "assault"


def test_normalize_weapon_preserves_unknown_input():
    # Not an alias, not a known weapon. Return as-is for boundary check.
    assert normalize_weapon("rocketbanana") == "rocketbanana"


def test_normalize_weapon_handles_empty_string():
    assert normalize_weapon("") == ""


def test_normalize_weapon_handles_only_whitespace():
    assert normalize_weapon("     ") == ""


def test_normalize_weapon_handles_non_string_input():
    assert normalize_weapon(None) == ""
    assert normalize_weapon(123) == ""


# ---------------------------------------------------------------------
# normalize_number
# ---------------------------------------------------------------------

def test_normalize_number_strips_whitespace():
    assert normalize_number("  5  ") == "5"


def test_normalize_number_preserves_negative_signs():
    assert normalize_number("-3") == "-3"


def test_normalize_number_preserves_decimal_points():
    assert normalize_number("45.5") == "45.5"


def test_normalize_number_preserves_non_numeric():
    # Parsing is not this function's job. Return as-is.
    assert normalize_number("abc") == "abc"


def test_normalize_number_handles_empty_string():
    assert normalize_number("") == ""


def test_normalize_number_handles_only_whitespace():
    assert normalize_number("     ") == ""


def test_normalize_number_handles_non_string_input():
    assert normalize_number(None) == ""
    assert normalize_number(5) == ""


# ---------------------------------------------------------------------
# normalize_input
# ---------------------------------------------------------------------

def test_normalize_input_returns_dict_with_all_fields():
    result = normalize_input("10", "5", "45.5", "AR")
    assert result == {
        "kills":    "10",
        "deaths":   "5",
        "accuracy": "45.5",
        "weapon":   "assault",
    }


def test_normalize_input_strips_all_whitespace():
    result = normalize_input("  10  ", "  5  ", "  45.5  ", "  sniper  ")
    assert result["kills"] == "10"
    assert result["deaths"] == "5"
    assert result["accuracy"] == "45.5"
    assert result["weapon"] == "sniper"


def test_normalize_input_handles_empty_fields():
    result = normalize_input("", "", "", "")
    assert result == {
        "kills":    "",
        "deaths":   "",
        "accuracy": "",
        "weapon":   "",
    }