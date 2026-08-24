# src/rules/rules/accuracy_rule.py

"""
Accuracy evaluation rule.

Translates V2.9 accuracy diagnostics into structured RuleResults.
Evaluates accuracy percentages against config thresholds.
"""

from typing import Optional
from src.rules.base import BaseRule
from src.rules.context import RuleContext
from src.models.rule_result import RuleResult
from src.models.severity import Severity


class AccuracyRule(BaseRule):
    """Rule for evaluating player aim and accuracy performance."""

    @property
    def name(self) -> str:
        return "accuracy_rule"

    def evaluate(self, context: RuleContext) -> Optional[RuleResult]:
        acc = context.stats.accuracy
        kills = context.stats.kills
        deaths = context.stats.deaths
        config = context.config

        # 1. Low Accuracy (< 20%)
        if acc < config.low_accuracy:
            return RuleResult(
                rule_name=self.name,
                severity=Severity.WARNING,
                message="Aim needs Improvement",
                suggestion="Learn to track enemies and control recoil.",
                passed=False,
            )

        # 2. Average Accuracy (20% <= acc < 40%)
        if config.low_accuracy <= acc < config.mid_accuracy:
            return RuleResult(
                rule_name=self.name,
                severity=Severity.INFO,
                message="Average Aim. Can Improve",
                passed=True,
            )

        # 3. High Accuracy & Positive K/D (acc >= 40% and kills > deaths)
        if acc >= config.mid_accuracy and kills > deaths:
            return RuleResult(
                rule_name=self.name,
                severity=Severity.SUCCESS,
                message="Strong Performance, Keep up the Good Work",
                passed=True,
            )

        return None