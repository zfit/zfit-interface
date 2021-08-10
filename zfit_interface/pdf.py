from zfit_interface.func import ZfitFunc
from zfit_interface.typing import ArrayLike
from zfit_interface.typing import NormInputType
from zfit_interface.typing import VarInputType


class ZfitPDF(ZfitFunc):
    def pdf(self, var: VarInputType, norm: NormInputType = None) -> ArrayLike:
        raise NotImplementedError

    def integrate(self, limits, *, norm=None, var=None):
        raise NotImplementedError

    def sample(self, n, limits=None, *, var):
        raise NotImplementedError

    @property
    def is_extended(self):
        raise NotImplementedError

    def get_yield(self):
        raise NotImplementedError


class Integral:
    @classmethod
    def register_integral(cls, limits, func):
        raise NotImplementedError

    @classmethod
    def register_cdf(cls, upper, func):
        raise NotImplementedError


class Sampling:
    @classmethod
    def register_inverse_integral(cls, limits, func):
        raise NotImplementedError

    @classmethod
    def register_icdf(cls, upper, func):
        raise NotImplementedError
