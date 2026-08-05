# tests/test_models/test_metrics.py

import pytest
from dataclasses import FrozenInstanceError
from src.models.metrics import Metrics


def test_metrics_basic_creation():
    metrics = Metrics(
        kd_ratio=2.5,
        sample_size=15,
        is_small_sample=False,
    )
    assert metrics.kd_ratio == 2.5
    assert metrics.sample_size == 15
    assert metrics.is_small_sample is False


def test_metrics_small_sample_true():
    metrics = Metrics(
        kd_ratio=1.0,
        sample_size=3,
        is_small_sample=True,
    )
    assert metrics.is_small_sample is True


def test_metrics_zero_sample_size():
    metrics = Metrics(
        kd_ratio=0.0,
        sample_size=0,
        is_small_sample=True,
    )
    assert metrics.sample_size == 0


def test_metrics_is_frozen():
    metrics = Metrics(kd_ratio=1.0, sample_size=10, is_small_sample=False)
    with pytest.raises(FrozenInstanceError):
        metrics.kd_ratio = 999.0


def test_metrics_fields_are_correct_types():
    metrics = Metrics(kd_ratio=1.5, sample_size=10, is_small_sample=False)
    assert isinstance(metrics.kd_ratio, float)
    assert isinstance(metrics.sample_size, int)
    assert isinstance(metrics.is_small_sample, bool)


def test_metrics_equality():
    a = Metrics(kd_ratio=2.0, sample_size=10, is_small_sample=False)
    b = Metrics(kd_ratio=2.0, sample_size=10, is_small_sample=False)
    assert a == b


def test_metrics_inequality():
    a = Metrics(kd_ratio=2.0, sample_size=10, is_small_sample=False)
    b = Metrics(kd_ratio=2.0, sample_size=10, is_small_sample=True)
    assert a != b