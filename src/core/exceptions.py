# src/core/exceptions.py

"""
Custom exception classes for internal use within the analyzer.

These exceptions are never shown to the end user.
The controller catches them and translates them into safe,
human-readable error messages returned via ControllerResult.

Hierarchy:
    PlaylyticsError                (base)
    ├── ValidationError            (invalid input reached internal code)
    ├── AnalysisError              (rule or analyzer failure)
    └── WeaponNotSupportedError    (unknown weapon at router level)
"""


class PlaylyticsError(Exception):
    """
    Base exception for all Playlytics-specific errors.

    Catch this in the controller to handle any expected
    application-level failure. Never let it bubble up to the UI.
    """
    pass


class ValidationError(PlaylyticsError):
    """
    Raised when invalid data reaches code that expected valid input.

    This should be rare in practice. Validation happens at the boundary
    (validation/validator.py) and returns a ValidationResult. If this
    exception fires, it indicates a bug in the validation layer.
    """
    pass


class AnalysisError(PlaylyticsError):
    """
    Raised when a rule or weapon analyzer fails unexpectedly.

    Indicates a bug in analysis logic. Caught by the controller,
    logged, and returned as a generic error to the user.
    """
    pass


class WeaponNotSupportedError(PlaylyticsError):
    """
    Raised by the router when asked to analyze an unknown weapon.

    Normally caught by validation before reaching the router.
    If this fires, it indicates validation and router weapon lists
    are out of sync.
    """
    pass