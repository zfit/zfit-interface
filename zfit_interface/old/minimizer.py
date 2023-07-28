from __future__ import annotations

from collections.abc import Iterable
from typing import Protocol

from zfit_interface.old.loss import ZfitMinimalLoss
from zfit_interface.old.param import ZfitParameter
from zfit_interface.old.result import ZfitMinimalResult


class ZfitMinimizer(Protocol):
    """Define the minimizer interface."""

    def minimize(
        self, loss: ZfitMinimalLoss, params: Iterable[ZfitParameter] = None
    ) -> ZfitMinimalResult:
        raise NotImplementedError
