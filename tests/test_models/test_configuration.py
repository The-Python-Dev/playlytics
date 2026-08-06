# tests/test_models/test_configuration.py

import pytest
from dataclasses import FrozenInstanceError
from src.models.configuration import Configuration


def _sample_config():
    return Configuration(
        low_accuracy=20.0,
        mid_accuracy=40.0,
        high_accuracy=50.0,
        weak_kd=1.0,
        strong_kd=2.0,
        min_sample_size=5,
        max_kills=200,
        max_deaths=200,
        supported_weapons=("sniper", "smg", "assault", "lmg", "shotgun"),
    )


def test_configuration_basic_creation():
    config = _sample_config()
    assert config.low_accuracy == 20.0
    assert config.mid_accuracy == 40.0
    assert config.high_accuracy == 50.0
    assert config.weak_kd == 1.0
    assert config.strong_kd == 2.0
    assert config.min_sample_size == 5
    assert config.max_kills == 200
    assert config.max_deaths == 200


def test_configuration_supported_weapons_is_tuple():
    config = _sample_config()
    assert isinstance(config.supported_weapons, tuple)
    assert len(config.supported_weapons) == 5
    assert "sniper" in config.supported_weapons
    assert "assault" in config.supported_weapons


def test_configuration_is_frozen():
    config = _sample_config()
    with pytest.raises(FrozenInstanceError):
        config.high_accuracy = 999.0


def test_configuration_supported_weapons_immutable():
    config = _sample_config()
    # Tuples do not have append or any mutating method
    assert not hasattr(config.supported_weapons, "append")


def test_configuration_fields_are_correct_types():
    config = _sample_config()
    assert isinstance(config.low_accuracy, float)
    assert isinstance(config.mid_accuracy, float)
    assert isinstance(config.high_accuracy, float)
    assert isinstance(config.weak_kd, float)
    assert isinstance(config.strong_kd, float)
    assert isinstance(config.min_sample_size, int)
    assert isinstance(config.max_kills, int)
    assert isinstance(config.max_deaths, int)
    assert isinstance(config.supported_weapons, tuple)


def test_configuration_equality():
    a = _sample_config()
    b = _sample_config()
    assert a == b


def test_configuration_inequality():
    a = _sample_config()
    b = Configuration(
        low_accuracy=25.0,   # different value
        mid_accuracy=40.0,
        high_accuracy=50.0,
        weak_kd=1.0,
        strong_kd=2.0,
        min_sample_size=5,
        max_kills=200,
        max_deaths=200,
        supported_weapons=("sniper", "smg", "assault", "lmg", "shotgun"),
    )
    assert a != b