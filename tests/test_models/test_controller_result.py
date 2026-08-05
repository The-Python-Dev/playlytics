# tests/test_models/test_controller_result.py

import pytest
from dataclasses import FrozenInstanceError
from src.models.controller_result import ControllerResult
from src.models.analysis_result import AnalysisResult
from src.models.player_stats import PlayerStats
from src.models.metrics import Metrics
from src.models.rule_result import RuleResult
from src.models.severity import Severity


def _sample_analysis_result():
    return AnalysisResult(
        stats=PlayerStats(kills=10, deaths=4, accuracy=45.0, weapon="assault"),
        metrics=Metrics(kd_ratio=2.5, sample_size=14, is_small_sample=False),
        rule_results=[
            RuleResult("kd_rule", Severity.SUCCESS, "Strong efficiency."),
        ],
        summary="Strong performance overall.",
    )


def test_controller_result_success_case():
    result = ControllerResult(
        success=True,
        result=_sample_analysis_result(),
    )
    assert result.success is True
    assert result.result is not None
    assert result.result.summary == "Strong performance overall."
    assert result.errors == []


def test_controller_result_failure_case():
    result = ControllerResult(
        success=False,
        errors=["Kills cannot be negative."],
    )
    assert result.success is False
    assert result.result is None
    assert len(result.errors) == 1


def test_controller_result_multiple_errors():
    result = ControllerResult(
        success=False,
        errors=[
            "Kills cannot be negative.",
            "Accuracy must be between 0 and 100.",
        ],
    )
    assert result.success is False
    assert len(result.errors) == 2


def test_controller_result_defaults():
    result = ControllerResult(success=True)
    assert result.result is None
    assert result.errors == []


def test_controller_result_is_frozen():
    result = ControllerResult(success=True, result=_sample_analysis_result())
    with pytest.raises(FrozenInstanceError):
        result.success = False


def test_controller_result_default_factory_isolation():
    a = ControllerResult(success=False)
    b = ControllerResult(success=False)
    a.errors.append("Error A")
    assert len(b.errors) == 0


def test_controller_result_fields_are_correct_types():
    result = ControllerResult(
        success=True,
        result=_sample_analysis_result(),
        errors=[],
    )
    assert isinstance(result.success, bool)
    assert isinstance(result.result, AnalysisResult)
    assert isinstance(result.errors, list)