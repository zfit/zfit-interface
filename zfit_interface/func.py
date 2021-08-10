from __future__ import annotations

from collections.abc import Mapping

from zfit_interface.variables import ZfitVar


class ZfitFunc:
    @property
    def variables(self) -> Mapping[str, ZfitVar]:
        raise NotImplementedError

    def __call__(self, var):
        raise NotImplementedError

    @property
    def output_variables(self) -> Mapping[str, ZfitVar]:
        raise NotImplementedError

    def integrate(self, limits, *, var=None):
        raise NotImplementedError
