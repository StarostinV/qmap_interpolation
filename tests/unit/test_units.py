import pytest
from qmap_interpolation import nm, mm


def test_units():
    assert mm == 1.e+6
    assert nm == 1
