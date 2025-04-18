import pytest
from television import Television

def test_init():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 1, Volume = 0"

def test_power_toggle():
    tv = Television()
    tv.power()
    assert "Power = True" in str(tv)
    tv.power()
    assert "Power = False" in str(tv)

def test_mute_behavior():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert "Power = True" in str(tv)
    tv.mute()
    assert "Power = True" in str(tv)
    
    tv.power()
    tv.mute()  
    assert "Power = False" in str(tv)

def test_channel_up_behavior():
    tv = Television()
    tv.channel_up()  
    assert str(tv) == "Power = False, Channel = 1, Volume = 0"

    tv.power()
    tv.channel_up()
    assert "Channel = 2" in str(tv)


    for _ in range(48):
        tv.channel_up()
    tv.channel_up()
    assert "Channel = 1" in str(tv)

def test_channel_down_behavior():
    tv = Television()
    tv.channel_down()  
    assert str(tv) == "Power = False, Channel = 1, Volume = 0"

    tv.power()
    tv.channel_down()
    assert "Channel = 50" in str(tv)

def test_volume_up_behavior():
    tv = Television()
    tv.volume_up()  
    assert str(tv) == "Power = False, Channel = 1, Volume = 0"

    tv.power()
    for _ in range(5):
        tv.volume_up()
    assert "Volume = 5" in str(tv)

    for _ in range(10):
        tv.volume_up()
    assert f"Volume = {Television.MAX_VOLUME}" in str(tv)

    tv.mute()
    tv.volume_up()
    assert "Volume = 10" in str(tv)  
    assert "Power = True" in str(tv)

def test_volume_down_behavior():
    tv = Television()
    tv.volume_down()  
    assert str(tv) == "Power = False, Channel = 1, Volume = 0"

    tv.power()
    for _ in range(10):  
        tv.volume_up()
    tv.volume_down()
    assert f"Volume = {Television.MAX_VOLUME - 1}" in str(tv)

    tv.mute()
    tv.volume_down()
    assert f"Volume = {Television.MAX_VOLUME - 2}" in str(tv)

    for _ in range(20):
        tv.volume_down()
    assert f"Volume = {Television.MIN_VOLUME}" in str(tv)
