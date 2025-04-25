import pytest
from television import Television

def test_init() -> None:
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power() -> None:
    tv = Television()
    tv.power()
    assert "Power = True" in str(tv)
    tv.power()
    assert "Power = False" in str(tv)

def test_mute() -> None:
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert "Volume = 0" in str(tv)
    tv.mute()
    assert "Volume = 1" in str(tv)
    tv.power()
    tv.mute()
    assert "Volume = 0" in str(tv)

def test_channel_up() -> None:
    tv = Television()
    tv.channel_up()
    assert "Channel = 0" in str(tv) # tv is off
    tv.power()
    for _ in range(5):
        tv.channel_up()
    assert "Channel = 1" in str(tv) # Wrapped: 0 -> 1 -> 2 -> 3 -> 0 -> 1

def test_channel_down() -> None:
    tv = Television()
    tv.channel_down()
    assert "Channel = 0" in str(tv) # tv is off
    tv.power()
    tv.channel_down()
    assert "Channel = 3" in str(tv)
    tv.channel_down()
    assert "Channel = 2" in str(tv)

def test_volume_up() -> None:
    tv = Television()
    tv.volume_up()
    assert "Volume = 0" in str(tv) # tv is off
    tv.power()
    tv.volume_up()
    assert "Volume = 1" in str(tv)
    tv.mute()
    tv.volume_up()
    assert "Volume = 2" in str(tv)
    tv.volume_up()
    assert "Volume = 2" in str(tv) # max volume cap

def test_volume_down() -> None:
    tv = Television()
    tv.volume_down()
    assert "Volume = 0" in str(tv) # tv is off
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert "Volume = 1" in str(tv)
    tv.mute()
    tv.volume_down()
    assert "Volume = 0" in str(tv)
    tv.volume_down()
    assert "Volume = 0" in str(tv) # min volume cap