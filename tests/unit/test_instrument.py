import pytest


def test_instrument(instrument):
    assert instrument.hot_pixel_threshold is None
