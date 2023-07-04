from __future__ import annotations

from abc import abstractmethod

import zfit_interface.typing as ztyping


class ZfitMinimalLoss:
    @abstractmethod
    def gradients(self, params: ztyping.ParamTypeInput = None) -> list[float]:
        raise NotImplementedError

    @abstractmethod
    def value(self) -> ztyping.NumericalTypeReturn:
        raise NotImplementedError

    @property
    @abstractmethod
    def errordef(self) -> float:
        raise NotImplementedError
