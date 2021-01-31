from abc import abstractmethod
from typing import Union, Iterable

from zfit_interface.loss import ZfitMinimalLoss
from zfit_interface.param import ZfitParameter
from zfit_interface.result import ZfitMinimalResult


class ZfitMinimizer:
    """Define the minimizer interface."""

    @abstractmethod
    def minimize(self, loss: ZfitMinimalLoss, params: Iterable[ZfitParameter] = None) -> ZfitMinimalResult:
        raise NotImplementedError

    @property
    @abstractmethod
    def tolerance(self):
        raise NotImplementedError
