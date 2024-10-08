from __future__ import annotations

from abc import abstractmethod


class ZfitParameterValue:
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def floating(self) -> bool:
        raise NotImplementedError

    @floating.setter
    @abstractmethod
    def floating(self, value: bool):
        raise NotImplementedError

    @abstractmethod
    def value(self) -> float:
        raise NotImplementedError


class ZfitParameter(ZfitParameterValue):
    @abstractmethod
    def set_value(self, value):
        """Set the :py:class:`~zfit.Parameter` to `value` (temporarily if used in a context manager).

        This operation won't, compared to the assign, return the read value but an object that *can* act as a context
        manager.

        Args:
            value: The value the parameter will take on.
        """
        raise NotImplementedError

    # @property
    # @abstractmethod
    # def has_limits(self) -> bool:
    #     """If the parameter has limits set or not."""
    #     raise NotImplementedError

    @property
    @abstractmethod()
    def step_size(self) -> float:
        """Step size of the parameter, the estimated order of magnitude of the uncertainty.

        This can be crucial to tune for the minimization. A too large `step_size` can produce NaNs, a too small won't
        converge.

        Returns:
            The step size
        """
        raise NotImplementedError
