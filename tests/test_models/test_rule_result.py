# tests/test_models/test_rule_result.py

from src.models.rule_result import RuleResult
from src.models.severity import Severity


def test_rule_result_basic_creation():
    result = RuleResult(
        rule_name="accuracy_rule",
        severity=Severity.WARNING,
        message="Aim needs improvement.",
    )
    assert result.rule_name == "accuracy_rule"
    assert result.severity == Severity.WARNING
    assert result.message == "Aim needs improvement."
    assert result.suggestion is None
    assert result.passed is True


def test_rule_result_with_suggestion():
    result = RuleResult(
        rule_name="kd_rule",
        severity=Severity.WARNING,
        message="Survival needs work.",
        suggestion="Avoid open areas and use cover.",
    )
    assert result.suggestion == "Avoid open areas and use cover."


def test_rule_result_passed_false():
    result = RuleResult(
        rule_name="positioning_rule",
        severity=Severity.WARNING,
        message="Positioning may be weak.",
        passed=False,
    )
    assert result.passed is False


def test_rule_result_success_severity():
    result = RuleResult(
        rule_name="survival_rule",
        severity=Severity.SUCCESS,
        message="Perfect survival.",
    )
    assert result.severity == Severity.SUCCESS


def test_rule_result_error_severity():
    result = RuleResult(
        rule_name="validation",
        severity=Severity.ERROR,
        message="Invalid input detected.",
        passed=False,
    )
    assert result.severity == Severity.ERROR


def test_rule_result_fields_are_correct_types():
    result = RuleResult(
        rule_name="kd_rule",
        severity=Severity.INFO,
        message="Average performance.",
    )
    assert isinstance(result.rule_name, str)
    assert isinstance(result.severity, Severity)
    assert isinstance(result.message, str)
    assert isinstance(result.passed, bool)