from __future__ import annotations

from abc import abstractmethod

import numpy as np


class ZfitData:
    @abstractmethod
    def value(self, obs: list[str] = None) -> np.typ:
        raise NotImplementedError

    @abstractmethod
    def sort_by_obs(self, obs, allow_superset: bool = True):
        raise NotImplementedError

    @abstractmethod
    def sort_by_axes(self, axes, allow_superset: bool = True):
        raise NotImplementedError

    @property
    @abstractmethod
    def weights(self):
        raise NotImplementedError
