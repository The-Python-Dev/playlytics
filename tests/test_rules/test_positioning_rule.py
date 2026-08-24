# tests/test_rules/test_positioning_rule.py

import pytest
from src.rules.rules.positioning_rule import PositioningRule
from src.rules.context import RuleContext
from src.models.player_stats import PlayerStats
from src.models.metrics import Metrics
from src.models.severity import Severity
from src.core.config import get_default_configuration


@pytest.fixture
def rule():
    return PositioningRule()


@pytest.fixture
def config():
    return get_default_configuration()


def test_positioning_rule_name(rule):
    assert rule.name == "positioning_rule"


def test_positioning_aim_good_positioning_issue(rule, config):
    # Acc = 50% (> 40%), K/D = 0.5 (< 1.0)
    stats = PlayerStats(kills=5, deaths=10, accuracy=50.0, weapon="assault")
    metrics = Metrics(kd_ratio=0.5, sample_size=15, is_small_sample=False)
    ctx = RuleContext(stats=stats, metrics=metrics, config=config)

    res = rule.evaluate(ctx)
    assert res is not None
    assert res.severity == Severity.WARNING
    assert res.message == "Aim is NOICE, Positioning is the issue"
    assert res.passed is False


def test_positioning_passive_tendency(rule, config):
    # V2.9 Test P1: Acc = 30% (< 40%), K/D = 2.5 (>= 2.0), sample >= 5
    stats = PlayerStats(kills=10, deaths=4, accuracy=30.0, weapon="assault")
    metrics = Metrics(kd_ratio=2.5, sample_size=14, is_small_sample=False)
    ctx = RuleContext(stats=stats, metrics=metrics, config=config)

    res = rule.evaluate(ctx)
    assert res is not None
    assert res.severity == Severity.INFO
    assert res.message == "Possible passive positioning tendency detected."
    assert res.passed is True


def test_positioning_weak_positioning_deaths_exceed_kills(rule, config):
    # Deaths (10) > Kills (5), Acc = 30% (< 40%)
    stats = PlayerStats(kills=5, deaths=10, accuracy=30.0, weapon="assault")
    metrics = Metrics(kd_ratio=0.5, sample_size=15, is_small_sample=False)
    ctx = RuleContext(stats=stats, metrics=metrics, config=config)

    res = rule.evaluate(ctx)
    assert res is not None
    assert res.severity == Severity.WARNING
    assert "Positioning" in res.message


def test_positioning_good_match_returns_none(rule, config):
    # Kills = 10, Deaths = 5, Acc = 45% -> No positioning issues
    stats = PlayerStats(kills=10, deaths=5, accuracy=45.0, weapon="assault")
    metrics = Metrics(kd_ratio=2.0, sample_size=15, is_small_sample=False)
    ctx = RuleContext(stats=stats, metrics=metrics, config=config)

    res = rule.evaluate(ctx)
    assert res is None