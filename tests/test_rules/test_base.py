# tests/test_rules/test_base.py

import pytest
from typing import Optional
from src.rules.base import BaseRule
from src.rules.context import RuleContext
from src.models.rule_result import RuleResult
from src.models.severity import Severity
from src.models.player_stats import PlayerStats
from src.models.metrics import Metrics
from src.core.config import get_default_configuration


class DummyRule(BaseRule):
    """Concrete implementation for testing BaseRule interface."""

    @property
    def name(self) -> str:
        return "dummy_rule"

    def evaluate(self, context: RuleContext) -> Optional[RuleResult]:
        if context.stats.kills > 5:
            return RuleResult(
                rule_name=self.name,
                severity=Severity.INFO,
                message="Kills > 5",
            )
        return None


def test_cannot_instantiate_abstract_base_rule():
    with pytest.raises(TypeError):
        BaseRule()  # Can't instantiate abstract class


def test_concrete_rule_implementation():
    rule = DummyRule()
    assert rule.name == "dummy_rule"

    stats_high = PlayerStats(kills=10, deaths=2, accuracy=50.0, weapon="assault")
    metrics_high = Metrics(kd_ratio=5.0, sample_size=12, is_small_sample=False)
    config = get_default_configuration()
    ctx_high = RuleContext(stats=stats_high, metrics=metrics_high, config=config)

    res = rule.evaluate(ctx_high)
    assert res is not None
    assert res.rule_name == "dummy_rule"
    assert res.message == "Kills > 5"


def test_concrete_rule_returns_none_when_not_applicable():
    rule = DummyRule()
    stats_low = PlayerStats(kills=2, deaths=2, accuracy=50.0, weapon="assault")
    metrics_low = Metrics(kd_ratio=1.0, sample_size=4, is_small_sample=True)
    config = get_default_configuration()
    ctx_low = RuleContext(stats=stats_low, metrics=metrics_low, config=config)

    res = rule.evaluate(ctx_low)
    assert res is None