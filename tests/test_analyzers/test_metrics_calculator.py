# tests/test_analyzers/test_metrics_calculator.py

import pytest
from src.models.player_stats import PlayerStats
from src.models.metrics import Metrics
from src.analyzers.metrics_calculator import calculate_metrics
from src.core.config import get_default_configuration


@pytest.fixture
def config():
    return get_default_configuration()


def test_calculate_metrics_standard_case(config):
    stats = PlayerStats(kills=10, deaths=5, accuracy=45.0, weapon="assault")
    metrics = calculate_metrics(stats, config)

    assert isinstance(metrics, Metrics)
    assert metrics.kd_ratio == 2.0
    assert metrics.sample_size == 15
    assert metrics.is_small_sample is False


def test_calculate_metrics_zero_deaths_returns_kills(config):
    # V2.9 Boundary Test B1: 4 kills, 0 deaths -> K/D = 4.0
    stats = PlayerStats(kills=4, deaths=0, accuracy=20.0, weapon="assault")
    metrics = calculate_metrics(stats, config)

    assert metrics.kd_ratio == 4.0
    assert metrics.sample_size == 4
    assert metrics.is_small_sample is True  # 4 < 5


def test_calculate_metrics_zero_kills_zero_deaths(config):
    stats = PlayerStats(kills=0, deaths=0, accuracy=0.0, weapon="sniper")
    metrics = calculate_metrics(stats, config)

    assert metrics.kd_ratio == 0.0
    assert metrics.sample_size == 0
    assert metrics.is_small_sample is True


def test_calculate_metrics_rounding_to_two_decimal_places(config):
    stats = PlayerStats(kills=10, deaths=3, accuracy=50.0, weapon="smg")
    metrics = calculate_metrics(stats, config)

    # 10 / 3 = 3.33333... -> 3.33
    assert metrics.kd_ratio == 3.33


def test_calculate_metrics_boundary_sample_size_four(config):
    # Kills + deaths = 4 -> small sample
    stats = PlayerStats(kills=3, deaths=1, accuracy=30.0, weapon="lmg")
    metrics = calculate_metrics(stats, config)

    assert metrics.sample_size == 4
    assert metrics.is_small_sample is True


def test_calculate_metrics_boundary_sample_size_five(config):
    # Kills + deaths = 5 -> NOT small sample
    stats = PlayerStats(kills=4, deaths=1, accuracy=90.0, weapon="sniper")
    metrics = calculate_metrics(stats, config)

    assert metrics.sample_size == 5
    assert metrics.is_small_sample is False


def test_calculate_metrics_uses_default_config_if_none_provided():
    stats = PlayerStats(kills=10, deaths=2, accuracy=40.0, weapon="assault")
    metrics = calculate_metrics(stats)

    assert metrics.kd_ratio == 5.0
    assert metrics.sample_size == 12
    assert metrics.is_small_sample is False