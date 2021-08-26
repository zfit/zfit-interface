from __future__ import annotations

from collections.abc import Mapping

from zfit_interface.typing import ArrayLike
from zfit_interface.typing import VarInputType
from zfit_interface.variables import ZfitVar


class ZfitFunc:
    @property
    def variables(self) -> Mapping[str, ZfitVar]:
        raise NotImplementedError

    def __call__(self, var=None):
        raise NotImplementedError

    @property
    def output_variables(self) -> Mapping[str, ZfitVar]:
        raise NotImplementedError


class ZfitScalarFunc:
    def values(self, var: VarInputType = None, *, options=None) -> ArrayLike:
        """Values of a histogram, corresponds to the integral over *func* for the bin edges."""
        raise NotImplementedError
