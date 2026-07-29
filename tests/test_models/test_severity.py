# tests/test_models/test_severity.py

from src.models.severity import Severity


def test_severity_members_exist():
    assert Severity.SUCCESS
    assert Severity.INFO
    assert Severity.WARNING
    assert Severity.ERROR


def test_severity_values():
    assert Severity.SUCCESS.value == "success"
    assert Severity.INFO.value    == "info"
    assert Severity.WARNING.value == "warning"
    assert Severity.ERROR.value   == "error"


def test_severity_is_enum():
    assert isinstance(Severity.SUCCESS, Severity)


def test_severity_identity_comparison():
    assert Severity.SUCCESS is Severity.SUCCESS
    assert Severity.SUCCESS is not Severity.WARNING


def test_severity_not_equal_to_plain_string():
    assert Severity.SUCCESS != "success"