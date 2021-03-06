import numpy as np

from .typed_tuple import TypedTuple
from .utils import lazy_property


class QMap(TypedTuple):
    qxy_start: float
    qxy_end: float
    qxy_num: int
    qz_start: float
    qz_end: float
    qz_num: int

    def __init__(self, *args, **kwargs):
        super().__init__()
        assert self.qz_num > 0, f'Qz axis size should be a positive integer, provided {self.qz_num} instead.'
        assert self.qxy_num > 0, f'Qxy axis size should be a positive integer, provided {self.qxy_num} instead.'
        assert self.qxy_start < self.qxy_end, f'qxy_start should be smaller that qxy_end.'
        assert self.qz_start < self.qz_end, f'qz_start should be smaller that qz_end.'

    @classmethod
    def from_step(cls, qxy_end: float, qz_end: float, q_resolution: float):
        qxy_start = 0
        qz_start = 0
        qxy_num = int(qxy_end / q_resolution)
        qz_num = int(qz_end / q_resolution)
        return cls(qxy_start, qxy_end, qxy_num, qz_start, qz_end, qz_num)

    @lazy_property
    def qxy_step(self):
        return (self.qxy_end - self.qxy_start) / self.qxy_num

    @lazy_property
    def qz_step(self):
        return (self.qz_end - self.qz_start) / self.qz_num

    @lazy_property
    def qxy(self) -> np.ndarray:
        return np.linspace(self.qxy_start, self.qxy_end, self.qxy_num)

    @lazy_property
    def qz(self) -> np.ndarray:
        return np.linspace(self.qz_start, self.qz_end, self.qz_num)

    @lazy_property
    def q_vector(self) -> np.ndarray:
        return np.stack([self.qxy, self.qz])
