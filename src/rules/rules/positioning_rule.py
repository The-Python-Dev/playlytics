# src/rules/rules/positioning_rule.py

"""
Positioning evaluation rule.

Translates V2.9 positioning diagnostics into structured RuleResults.
Evaluates relationship between accuracy, deaths, kills, and K/D.
"""

from typing import Optional
from src.rules.base import BaseRule
from src.rules.context import RuleContext
from src.models.rule_result import RuleResult
from src.models.severity import Severity


class PositioningRule(BaseRule):
    """Rule for evaluating player positioning and tactical movement."""

    @property
    def name(self) -> str:
        return "positioning_rule"

    def evaluate(self, context: RuleContext) -> Optional[RuleResult]:
        acc = context.stats.accuracy
        kills = context.stats.kills
        deaths = context.stats.deaths
        kd = context.metrics.kd_ratio
        is_small = context.metrics.is_small_sample
        config = context.config

        # 1. Aim is good, but positioning/survival is dragging K/D down
        if acc > config.mid_accuracy and kd < config.weak_kd:
            return RuleResult(
                rule_name=self.name,
                severity=Severity.WARNING,
                message="Aim is NOICE, Positioning is the issue",
                passed=False,
            )

        # 2. Passive positioning (Lower accuracy, but high K/D & valid sample)
        if not is_small and acc < config.mid_accuracy and kd >= config.strong_kd:
            return RuleResult(
                rule_name=self.name,
                severity=Severity.INFO,
                message="Possible passive positioning tendency detected.",
                passed=True,
            )

        # 3. General Weak Positioning (Deaths > Kills)
        if deaths > kills:
            return RuleResult(
                rule_name=self.name,
                severity=Severity.WARNING,
                message="Positioning may be weak",
                passed=False,
            )

        return None