import pytest
from qmap_interpolation import units


def test_units():
    assert units.nanometer == 1
    assert units.nm == 1
