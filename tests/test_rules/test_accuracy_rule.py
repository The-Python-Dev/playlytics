# tests/test_rules/test_accuracy_rule.py

import pytest
from src.rules.rules.accuracy_rule import AccuracyRule
from src.rules.context import RuleContext
from src.models.player_stats import PlayerStats
from src.models.metrics import Metrics
from src.models.severity import Severity
from src.core.config import get_default_configuration


@pytest.fixture
def rule():
    return AccuracyRule()


@pytest.fixture
def config():
    return get_default_configuration()


def test_accuracy_rule_name(rule):
    assert rule.name == "accuracy_rule"


def test_accuracy_rule_low_accuracy_warning(rule, config):
    # Acc = 15% (< 20%)
    stats = PlayerStats(kills=5, deaths=5, accuracy=15.0, weapon="assault")
    metrics = Metrics(kd_ratio=1.0, sample_size=10, is_small_sample=False)
    ctx = RuleContext(stats=stats, metrics=metrics, config=config)

    res = rule.evaluate(ctx)
    assert res is not None
    assert res.severity == Severity.WARNING
    assert res.message == "Aim needs Improvement"
    assert "recoil" in res.suggestion
    assert res.passed is False


def test_accuracy_rule_boundary_twenty_percent(rule, config):
    # V2.9 Test P3-A: Acc = 20% -> Average Aim (not Low)
    stats = PlayerStats(kills=5, deaths=5, accuracy=20.0, weapon="assault")
    metrics = Metrics(kd_ratio=1.0, sample_size=10, is_small_sample=False)
    ctx = RuleContext(stats=stats, metrics=metrics, config=config)

    res = rule.evaluate(ctx)
    assert res is not None
    assert res.severity == Severity.INFO
    assert res.message == "Average Aim. Can Improve"


def test_accuracy_rule_average_accuracy(rule, config):
    # Acc = 35% (20% <= acc < 40%)
    stats = PlayerStats(kills=5, deaths=5, accuracy=35.0, weapon="assault")
    metrics = Metrics(kd_ratio=1.0, sample_size=10, is_small_sample=False)
    ctx = RuleContext(stats=stats, metrics=metrics, config=config)

    res = rule.evaluate(ctx)
    assert res is not None
    assert res.severity == Severity.INFO
    assert res.message == "Average Aim. Can Improve"


def test_accuracy_rule_strong_performance(rule, config):
    # V2.9 Test P3-B: Acc = 40% & kills > deaths -> Strong Performance
    stats = PlayerStats(kills=5, deaths=4, accuracy=40.0, weapon="assault")
    metrics = Metrics(kd_ratio=1.25, sample_size=9, is_small_sample=False)
    ctx = RuleContext(stats=stats, metrics=metrics, config=config)

    res = rule.evaluate(ctx)
    assert res is not None
    assert res.severity == Severity.SUCCESS
    assert res.message == "Strong Performance, Keep up the Good Work"


def test_accuracy_rule_high_accuracy_but_negative_kd_returns_none(rule, config):
    # Acc = 45%, but kills <= deaths -> No accuracy rule triggered
    stats = PlayerStats(kills=4, deaths=5, accuracy=45.0, weapon="assault")
    metrics = Metrics(kd_ratio=0.8, sample_size=9, is_small_sample=False)
    ctx = RuleContext(stats=stats, metrics=metrics, config=config)

    res = rule.evaluate(ctx)
    assert res is None