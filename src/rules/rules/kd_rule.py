# src/rules/rules/kd_rule.py

"""
K/D ratio evaluation rule.

Translates V2.9 combat efficiency diagnostics into structured RuleResults.
Evaluates kd_ratio against config thresholds.
"""

from typing import Optional
from src.rules.base import BaseRule
from src.rules.context import RuleContext
from src.models.rule_result import RuleResult
from src.models.severity import Severity


class KDRule(BaseRule):
    """Rule for evaluating player combat efficiency and K/D performance."""

    @property
    def name(self) -> str:
        return "kd_rule"

    def evaluate(self, context: RuleContext) -> Optional[RuleResult]:
        kd = context.metrics.kd_ratio
        config = context.config

        # 1. Weak K/D (< 1.0)
        if kd < config.weak_kd:
            return RuleResult(
                rule_name=self.name,
                severity=Severity.WARNING,
                message="Survival Needs Work",
                suggestion=(
                    "My man sometimes u gotta get in the Shadows in order to "
                    "defeat enemies. Avoid open areas man."
                ),
                passed=False,
            )

        # 2. Strong K/D (>= 2.0)
        if kd >= config.strong_kd:
            return RuleResult(
                rule_name=self.name,
                severity=Severity.SUCCESS,
                message="Strong Combat Efficiency, My Man That's good",
                passed=True,
            )

        return None