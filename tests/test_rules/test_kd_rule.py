# tests/test_rules/test_kd_rule.py

import pytest
from src.rules.rules.kd_rule import KDRule
from src.rules.context import RuleContext
from src.models.player_stats import PlayerStats
from src.models.metrics import Metrics
from src.models.severity import Severity
from src.core.config import get_default_configuration


@pytest.fixture
def rule():
    return KDRule()


@pytest.fixture
def config():
    return get_default_configuration()


def test_kd_rule_name(rule):
    assert rule.name == "kd_rule"


def test_kd_rule_weak_kd_warning(rule, config):
    # K/D = 0.5 (< 1.0)
    stats = PlayerStats(kills=5, deaths=10, accuracy=30.0, weapon="assault")
    metrics = Metrics(kd_ratio=0.5, sample_size=15, is_small_sample=False)
    ctx = RuleContext(stats=stats, metrics=metrics, config=config)

    res = rule.evaluate(ctx)
    assert res is not None
    assert res.severity == Severity.WARNING
    assert res.message == "Survival Needs Work"
    assert "Shadows" in res.suggestion
    assert res.passed is False


def test_kd_rule_strong_kd_success(rule, config):
    # K/D = 2.5 (>= 2.0)
    stats = PlayerStats(kills=10, deaths=4, accuracy=35.0, weapon="assault")
    metrics = Metrics(kd_ratio=2.5, sample_size=14, is_small_sample=False)
    ctx = RuleContext(stats=stats, metrics=metrics, config=config)

    res = rule.evaluate(ctx)
    assert res is not None
    assert res.severity == Severity.SUCCESS
    assert res.message == "Strong Combat Efficiency, My Man That's good"
    assert res.passed is True


def test_kd_rule_average_kd_returns_none(rule, config):
    # K/D = 1.5 (1.0 <= K/D < 2.0)
    stats = PlayerStats(kills=6, deaths=4, accuracy=30.0, weapon="assault")
    metrics = Metrics(kd_ratio=1.5, sample_size=10, is_small_sample=False)
    ctx = RuleContext(stats=stats, metrics=metrics, config=config)

    res = rule.evaluate(ctx)
    assert res is None