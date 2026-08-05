# tests/test_models/test_analysis_result.py

import pytest
from dataclasses import FrozenInstanceError
from src.models.analysis_result import AnalysisResult
from src.models.player_stats import PlayerStats
from src.models.metrics import Metrics
from src.models.rule_result import RuleResult
from src.models.severity import Severity


def _sample_stats():
    return PlayerStats(kills=10, deaths=4, accuracy=45.0, weapon="assault")


def _sample_metrics():
    return Metrics(kd_ratio=2.5, sample_size=14, is_small_sample=False)


def _sample_rule_result():
    return RuleResult(
        rule_name="kd_rule",
        severity=Severity.SUCCESS,
        message="Strong combat efficiency.",
    )


def test_analysis_result_basic_creation():
    result = AnalysisResult(
        stats=_sample_stats(),
        metrics=_sample_metrics(),
        rule_results=[_sample_rule_result()],
        summary="Strong performance overall.",
    )
    assert result.stats.kills == 10
    assert result.metrics.kd_ratio == 2.5
    assert len(result.rule_results) == 1
    assert result.summary == "Strong performance overall."


def test_analysis_result_empty_rule_results_default():
    result = AnalysisResult(
        stats=_sample_stats(),
        metrics=_sample_metrics(),
    )
    assert result.rule_results == []
    assert result.summary == ""


def test_analysis_result_multiple_rule_results():
    r1 = RuleResult("rule_a", Severity.SUCCESS, "A message")
    r2 = RuleResult("rule_b", Severity.WARNING, "B message")
    r3 = RuleResult("rule_c", Severity.INFO, "C message")
    result = AnalysisResult(
        stats=_sample_stats(),
        metrics=_sample_metrics(),
        rule_results=[r1, r2, r3],
    )
    assert len(result.rule_results) == 3
    assert result.rule_results[1].severity == Severity.WARNING


def test_analysis_result_is_frozen():
    result = AnalysisResult(
        stats=_sample_stats(),
        metrics=_sample_metrics(),
    )
    with pytest.raises(FrozenInstanceError):
        result.summary = "changed"


def test_analysis_result_fields_are_correct_types():
    result = AnalysisResult(
        stats=_sample_stats(),
        metrics=_sample_metrics(),
        rule_results=[_sample_rule_result()],
        summary="Summary text",
    )
    assert isinstance(result.stats, PlayerStats)
    assert isinstance(result.metrics, Metrics)
    assert isinstance(result.rule_results, list)
    assert isinstance(result.rule_results[0], RuleResult)
    assert isinstance(result.summary, str)


def test_analysis_result_default_factory_isolation():
    # Two separate instances should not share the same list
    a = AnalysisResult(stats=_sample_stats(), metrics=_sample_metrics())
    b = AnalysisResult(stats=_sample_stats(), metrics=_sample_metrics())
    a.rule_results.append(_sample_rule_result())
    assert len(b.rule_results) == 0