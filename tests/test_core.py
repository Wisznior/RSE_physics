import pytest
from RSE_physics.core import calc_speed

def test_calc_speed():
    res = calc_speed("100m", "10s")
    assert "36.0" in res
    assert "kilometer / hour" in res

def test_units():
    res = calc_speed("60 mile", "1 hour")
    assert "96.56" in res