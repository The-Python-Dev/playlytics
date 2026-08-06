# src/core/logger.py

"""
Application-wide logging configuration.

Every module in Playlytics uses logging.getLogger(__name__)
to obtain its own logger. This module configures the root logger
once at application startup, ensuring all loggers share the same
format and handlers.

Usage:
    In run.py at startup:
        from src.core.logger import configure_logging
        configure_logging()

    In any module:
        import logging
        logger = logging.getLogger(__name__)
        logger.info("Something happened")
"""

import logging
import sys
from pathlib import Path
from typing import Optional


# ---------------------------------------------------------------------
# Default log format
# ---------------------------------------------------------------------

LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


# ---------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------

def configure_logging(
    level: int = logging.INFO,
    log_to_file: bool = False,
    log_file_path: Optional[Path] = None,
) -> None:
    """
    Configure the root logger for the entire application.

    Should be called exactly once at application startup.
    Subsequent calls reset the configuration.

    Args:
        level:         Minimum log level. Defaults to INFO.
        log_to_file:   If True, also write logs to a file.
        log_file_path: Path to the log file. Defaults to 'playlytics.log'
                       in the current working directory.
    """
    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    # Clear any existing handlers to avoid duplicates on reconfigure
    root_logger.handlers.clear()

    formatter = logging.Formatter(fmt=LOG_FORMAT, datefmt=DATE_FORMAT)

    # Console handler (always active)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)
    root_logger.addHandler(console_handler)

    # File handler (opt-in)
    if log_to_file:
        path = log_file_path or Path("playlytics.log")
        file_handler = logging.FileHandler(path, encoding="utf-8")
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level)
        root_logger.addHandler(file_handler)


# ---------------------------------------------------------------------
# Convenience getter
# ---------------------------------------------------------------------

def get_logger(name: str) -> logging.Logger:
    """
    Return a logger for the given module name.

    Convenience wrapper around logging.getLogger. Allows the logging
    strategy to change centrally without touching every module.

    Args:
        name: Logger name, typically __name__ of the calling module.

    Returns:
        Configured logger instance.
    """
    return logging.getLogger(name)