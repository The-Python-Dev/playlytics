# tests/test_core/test_logger.py

import logging
from pathlib import Path
from src.core.logger import configure_logging, get_logger


def test_get_logger_returns_logger_instance():
    logger = get_logger("test.module")
    assert isinstance(logger, logging.Logger)


def test_get_logger_returns_same_logger_for_same_name():
    a = get_logger("test.same")
    b = get_logger("test.same")
    assert a is b


def test_get_logger_returns_different_loggers_for_different_names():
    a = get_logger("test.one")
    b = get_logger("test.two")
    assert a is not b


def test_configure_logging_sets_root_level_to_info_by_default():
    configure_logging()
    assert logging.getLogger().level == logging.INFO


def test_configure_logging_can_set_debug_level():
    configure_logging(level=logging.DEBUG)
    assert logging.getLogger().level == logging.DEBUG


def test_configure_logging_adds_console_handler():
    configure_logging()
    root = logging.getLogger()
    assert len(root.handlers) >= 1
    assert any(isinstance(h, logging.StreamHandler) for h in root.handlers)


def test_configure_logging_clears_existing_handlers_on_reconfigure():
    configure_logging()
    initial_count = len(logging.getLogger().handlers)
    configure_logging()
    # Should not accumulate handlers on repeated calls
    assert len(logging.getLogger().handlers) == initial_count


def test_configure_logging_adds_file_handler_when_enabled(tmp_path):
    log_path = tmp_path / "test.log"
    configure_logging(log_to_file=True, log_file_path=log_path)
    root = logging.getLogger()
    assert any(isinstance(h, logging.FileHandler) for h in root.handlers)


def test_configure_logging_writes_to_file(tmp_path):
    log_path = tmp_path / "test.log"
    configure_logging(log_to_file=True, log_file_path=log_path)
    logger = get_logger("test.writes")
    logger.info("hello from test")

    # Ensure file was written
    for handler in logging.getLogger().handlers:
        handler.flush()

    assert log_path.exists()
    content = log_path.read_text(encoding="utf-8")
    assert "hello from test" in content
    assert "INFO" in content
    assert "test.writes" in content


def test_configure_logging_no_file_handler_by_default():
    configure_logging()
    root = logging.getLogger()
    assert not any(isinstance(h, logging.FileHandler) for h in root.handlers)