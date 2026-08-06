# tests/test_core/test_exceptions.py

import pytest
from src.core.exceptions import (
    PlaylyticsError,
    ValidationError,
    AnalysisError,
    WeaponNotSupportedError,
)


def test_playlytics_error_is_exception():
    assert issubclass(PlaylyticsError, Exception)


def test_validation_error_inherits_from_playlytics_error():
    assert issubclass(ValidationError, PlaylyticsError)


def test_analysis_error_inherits_from_playlytics_error():
    assert issubclass(AnalysisError, PlaylyticsError)


def test_weapon_not_supported_error_inherits_from_playlytics_error():
    assert issubclass(WeaponNotSupportedError, PlaylyticsError)


def test_playlytics_error_can_be_raised_and_caught():
    with pytest.raises(PlaylyticsError):
        raise PlaylyticsError("test")


def test_validation_error_caught_as_playlytics_error():
    with pytest.raises(PlaylyticsError):
        raise ValidationError("bad input")


def test_analysis_error_caught_as_playlytics_error():
    with pytest.raises(PlaylyticsError):
        raise AnalysisError("rule crashed")


def test_weapon_not_supported_caught_as_playlytics_error():
    with pytest.raises(PlaylyticsError):
        raise WeaponNotSupportedError("unknown weapon: rocketbanana")


def test_exceptions_preserve_message():
    try:
        raise ValidationError("kills must be non-negative")
    except ValidationError as e:
        assert str(e) == "kills must be non-negative"


def test_specific_exceptions_are_distinct():
    # ValidationError should NOT be caught by AnalysisError handler
    with pytest.raises(ValidationError):
        try:
            raise ValidationError("test")
        except AnalysisError:
            pytest.fail("ValidationError was caught by AnalysisError handler")