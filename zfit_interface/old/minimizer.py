from __future__ import annotations

from abc import abstractmethod
from collections.abc import Iterable

from zfit_interface.old.loss import ZfitMinimalLoss
from zfit_interface.old.param import ZfitParameter
from zfit_interface.old.result import ZfitMinimalResult


class ZfitMinimizer:
    """Define the minimizer interface."""

    @abstractmethod
    def minimize(
        self, loss: ZfitMinimalLoss, params: Iterable[ZfitParameter] = None
    ) -> ZfitMinimalResult:
        raise NotImplementedError

    @property
    @abstractmethod
    def tolerance(self):
        raise NotImplementedError
