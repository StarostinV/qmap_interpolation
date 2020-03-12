import pytest
from qmap_interpolation import units as uq
from qmap_interpolation import Instrument, Size


@pytest.fixture()
def instrument():
    size = Size(100, 200)
    wavelength = 10 * uq.angstrom
    pixel_size = 7 * uq.mm
    return Instrument(wavelength, size, pixel_size)
