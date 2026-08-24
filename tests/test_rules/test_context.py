# tests/test_rules/test_context.py

import pytest
from dataclasses import FrozenInstanceError
from src.rules.context import RuleContext
from src.models.player_stats import PlayerStats
from src.models.metrics import Metrics
from src.core.config import get_default_configuration


def test_rule_context_creation():
    stats = PlayerStats(kills=10, deaths=5, accuracy=45.0, weapon="assault")
    metrics = Metrics(kd_ratio=2.0, sample_size=15, is_small_sample=False)
    config = get_default_configuration()

    ctx = RuleContext(stats=stats, metrics=metrics, config=config)

    assert ctx.stats == stats
    assert ctx.metrics == metrics
    assert ctx.config == config


def test_rule_context_is_frozen():
    stats = PlayerStats(kills=10, deaths=5, accuracy=45.0, weapon="assault")
    metrics = Metrics(kd_ratio=2.0, sample_size=15, is_small_sample=False)
    config = get_default_configuration()

    ctx = RuleContext(stats=stats, metrics=metrics, config=config)

    with pytest.raises(FrozenInstanceError):
        ctx.stats = None