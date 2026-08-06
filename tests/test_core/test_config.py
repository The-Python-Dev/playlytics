# tests/test_core/test_config.py

from src.core import config
from src.models.configuration import Configuration


def test_accuracy_thresholds_match_v29():
    assert config.LOW_ACCURACY == 20.0
    assert config.MID_ACCURACY == 40.0
    assert config.HIGH_ACCURACY == 50.0


def test_kd_thresholds_match_v29():
    assert config.WEAK_KD == 1.0
    assert config.STRONG_KD == 2.0


def test_sample_size_matches_v29():
    assert config.MIN_SAMPLE_SIZE == 5


def test_input_limits_match_v29():
    assert config.MAX_KILLS == 200
    assert config.MAX_DEATHS == 200


def test_supported_weapons_contents():
    assert "sniper" in config.SUPPORTED_WEAPONS
    assert "smg" in config.SUPPORTED_WEAPONS
    assert "assault" in config.SUPPORTED_WEAPONS
    assert "lmg" in config.SUPPORTED_WEAPONS
    assert "shotgun" in config.SUPPORTED_WEAPONS
    assert len(config.SUPPORTED_WEAPONS) == 5


def test_supported_weapons_is_tuple():
    assert isinstance(config.SUPPORTED_WEAPONS, tuple)


def test_weapon_aliases_ar_maps_to_assault():
    assert config.WEAPON_ALIASES["ar"] == "assault"


def test_get_default_configuration_returns_configuration_instance():
    cfg = config.get_default_configuration()
    assert isinstance(cfg, Configuration)


def test_get_default_configuration_values_match_constants():
    cfg = config.get_default_configuration()
    assert cfg.low_accuracy == config.LOW_ACCURACY
    assert cfg.mid_accuracy == config.MID_ACCURACY
    assert cfg.high_accuracy == config.HIGH_ACCURACY
    assert cfg.weak_kd == config.WEAK_KD
    assert cfg.strong_kd == config.STRONG_KD
    assert cfg.min_sample_size == config.MIN_SAMPLE_SIZE
    assert cfg.max_kills == config.MAX_KILLS
    assert cfg.max_deaths == config.MAX_DEATHS
    assert cfg.supported_weapons == config.SUPPORTED_WEAPONS


def test_get_default_configuration_is_frozen():
    import pytest
    from dataclasses import FrozenInstanceError

    cfg = config.get_default_configuration()
    with pytest.raises(FrozenInstanceError):
        cfg.high_accuracy = 999.0