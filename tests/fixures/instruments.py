import pytest
from qmap_interpolation import Instrument, Size, angstrom, mm, BeamCenter


@pytest.fixture()
def instrument():
    beam_center = BeamCenter(0, 0)
    size = Size(100, 200)
    wavelength = 10 * angstrom
    pixel_size = 7 * mm
    return Instrument(wavelength, size, pixel_size)
