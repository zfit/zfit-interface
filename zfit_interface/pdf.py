from zfit_interface.func import ZfitFunc
from zfit_interface.typing import ArrayLike
from zfit_interface.typing import LimitsInputType
from zfit_interface.typing import NormInputType
from zfit_interface.typing import OptionsInputType
from zfit_interface.typing import VarInputType
from zfit_interface.variables import ZfitComposedVariable
from zfit_interface.variables import ZfitSpace


class ZfitPDF(ZfitFunc):
    def pdf(
        self, var: VarInputType, norm: NormInputType = None, *, options=None
    ) -> ArrayLike:
        """Probability density of the defined function, normalized over *norm* to 1."""
        raise NotImplementedError

    def ext_pdf(
        self, var: VarInputType, norm: NormInputType = None, *, options=None
    ) -> ArrayLike:
        """Probability density of the defined function, normalized over *norm* to the yield.

        This method is only available for extended PDFs.
        """
        raise NotImplementedError

    def counts(
        self, var: VarInputType, norm: NormInputType, *, options=None
    ) -> ArrayLike:
        """Counts of a histogram, corresponds to the integral over *ext_pdf* for the bin edges.

        This method corresponds to the "frequency" of a histogram.

        This method is only available for extended PDFs.
        """
        raise NotImplementedError

    def rel_counts(
        self, var: VarInputType, norm: NormInputType, *, options=None
    ) -> ArrayLike:
        """Relative counts of a histogram, corresponds to the integral over *pdf* for the bin edges.

        This method corresponds to the "relative frequency" of a histogram.
        """
        raise NotImplementedError

    def integrate(
        self,
        limits: LimitsInputType = None,
        *,
        norm: NormInputType = None,
        var: VarInputType = None,
        options: OptionsInputType = None
    ) -> ArrayLike:
        """Integrate (analytically, otherwise numerically) over *limits*."""
        raise NotImplementedError

    def ext_integrate(self, limits=None, *, norm=None, var=None, options=None):
        raise NotImplementedError

    def sample(self, n=None, limits=None, *, var=None, options=None):
        raise NotImplementedError

    @property
    def is_extended(self) -> bool:
        raise NotImplementedError

    def get_yield(self) -> ZfitComposedVariable:
        raise NotImplementedError

    @property
    def space(self) -> ZfitSpace:
        raise NotImplementedError

    @property
    def norm(self) -> ZfitSpace:
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
