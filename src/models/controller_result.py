# src/models/controller_result.py

from dataclasses import dataclass, field
from typing import List, Optional
from src.models.analysis_result import AnalysisResult


@dataclass(frozen=True)
class ControllerResult:
    """
    Single predictable return type from the controller to the UI.

    Produced by ui/controller.py.
    Consumed by the UI to decide what to render.

    When success is True, result contains a complete AnalysisResult.
    When success is False, result is None and errors contains
    human-readable descriptions of what went wrong.

    This is the boundary between the analysis pipeline and the UI.
    The UI never sees raw exceptions or intermediate results.

    Attributes:
        success: True if the full pipeline completed without errors.
        result:  Complete AnalysisResult when successful, None otherwise.
        errors:  List of human-readable error messages.
                 Empty when the pipeline succeeded.
    """

    success: bool
    result:  Optional[AnalysisResult] = None
    errors:  List[str] = field(default_factory=list)