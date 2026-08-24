# src/rules/base.py

"""
Abstract Base Class for all gameplay rules.

Defines the contract that all concrete rules must implement.
Ensures consistency and type safety across the Rule Engine.
"""

from abc import ABC, abstractmethod
from typing import Optional
from src.rules.context import RuleContext
from src.models.rule_result import RuleResult


class BaseRule(ABC):
    """
    Abstract Base Class for analysis rules.

    Every concrete rule evaluates a RuleContext and returns either
    a RuleResult (if triggered) or None (if not applicable).
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Unique name/identifier for the rule.

        Returns:
            String name (e.g., 'accuracy_rule', 'kd_rule').
        """
        pass

    @abstractmethod
    def evaluate(self, context: RuleContext) -> Optional[RuleResult]:
        """
        Evaluate rule condition against player context.

        Args:
            context: RuleContext holding stats, metrics, and config.

        Returns:
            RuleResult if rule triggers, or None if not applicable.
        """
        pass