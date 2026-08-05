# tests/test_models/test_player_stats.py

import pytest
from dataclasses import FrozenInstanceError
from src.models.player_stats import PlayerStats


def test_player_stats_basic_creation():
    stats = PlayerStats(
        kills=10,
        deaths=5,
        accuracy=45.5,
        weapon="assault",
    )
    assert stats.kills == 10
    assert stats.deaths == 5
    assert stats.accuracy == 45.5
    assert stats.weapon == "assault"


def test_player_stats_zero_deaths():
    stats = PlayerStats(kills=4, deaths=0, accuracy=20.0, weapon="ar")
    assert stats.deaths == 0


def test_player_stats_zero_kills():
    stats = PlayerStats(kills=0, deaths=3, accuracy=15.0, weapon="smg")
    assert stats.kills == 0


def test_player_stats_is_frozen():
    stats = PlayerStats(kills=5, deaths=2, accuracy=30.0, weapon="lmg")
    with pytest.raises(FrozenInstanceError):
        stats.kills = 999


def test_player_stats_fields_are_correct_types():
    stats = PlayerStats(kills=10, deaths=5, accuracy=50.0, weapon="sniper")
    assert isinstance(stats.kills, int)
    assert isinstance(stats.deaths, int)
    assert isinstance(stats.accuracy, float)
    assert isinstance(stats.weapon, str)


def test_player_stats_equality():
    a = PlayerStats(kills=5, deaths=2, accuracy=30.0, weapon="ar")
    b = PlayerStats(kills=5, deaths=2, accuracy=30.0, weapon="ar")
    assert a == b


def test_player_stats_inequality():
    a = PlayerStats(kills=5, deaths=2, accuracy=30.0, weapon="ar")
    b = PlayerStats(kills=5, deaths=2, accuracy=30.0, weapon="smg")
    assert a != b