from __future__ import annotations

from abc import abstractmethod
from collections.abc import Callable
from typing import List
from typing import Union

import zfit_interface.typing as ztyping
from zfit_interface.old.param import ZfitParameter


class ZfitModel:
    @abstractmethod
    def update_integration_options(
        self, *args, **kwargs
    ):  # TODO: handling integration properly
        raise NotImplementedError

    @abstractmethod
    def integrate(
        self,
        limits: ztyping.LimitsType,
        norm_range: ztyping.LimitsType = None,
        name: str = "integrate",
    ) -> ztyping.XType:
        """Integrate the function over `limits` (normalized over `norm_range` if not False).

        Args:
            limits: the limits to integrate over
            norm_range: the limits to normalize over or False to integrate the
                unnormalized probability
            name:

        Returns:
            The integral value
        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def register_analytic_integral(
        cls,
        func: Callable,
        limits: ztyping.LimitsType = None,
        priority: int = 50,
        *,
        supports_norm_range: bool = False,
        supports_multiple_limits: bool = False,
    ):
        """Register an analytic integral with the class.

        Args:
            func:
            limits: |limits_arg_descr|
            priority:
            supports_multiple_limits:
            supports_norm_range:

        Returns:
        """
        raise NotImplementedError

    @abstractmethod
    def partial_integrate(
        self,
        x: ztyping.XType,
        limits: ztyping.LimitsType,
        norm_range: ztyping.LimitsType = None,
    ) -> ztyping.XType:
        """Partially integrate the function over the `limits` and evaluate it at `x`.

        Dimension of `limits` and `x` have to add up to the full dimension and be therefore equal
        to the dimensions of `norm_range` (if not False)

        Args:
            x: The value at which the partially integrated function will be evaluated
            limits: the limits to integrate over. Can contain only some axes
            norm_range: the limits to normalize over. Has to have all axes

        Returns:
            The value of the partially integrated function evaluated at `x`.
        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def register_inverse_analytic_integral(cls, func: Callable):
        """Register an inverse analytical integral, the inverse (unnormalized) cdf.

        Args:
            func:
        """
        raise NotImplementedError

    @abstractmethod
    def sample(self, n: int, limits: ztyping.LimitsType = None) -> ztyping.XType:
        """Sample `n` points within `limits` from the model.

        Args:
            n: The number of samples to be generated
            limits: In which region to sample in
            name:

        Returns:
            Tensor(n_obs, n_samples)
        """
        raise NotImplementedError


class ZfitFunc(ZfitModel):
    @abstractmethod
    def func(self, x: ztyping.XType, name: str = "value") -> ztyping.XType:
        raise NotImplementedError

    @abstractmethod
    def as_pdf(self):
        raise NotImplementedError


class ZfitPDF(ZfitModel):
    @abstractmethod
    def pdf(
        self, x: ztyping.XType, norm_range: ztyping.LimitsType = None
    ) -> ztyping.XType:
        raise NotImplementedError

    @property
    @abstractmethod
    def is_extended(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def set_norm_range(self):
        raise NotImplementedError

    @abstractmethod
    def create_extended(self, yield_: ztyping.ParamTypeInput) -> ZfitPDF:
        raise NotImplementedError

    @abstractmethod
    def get_yield(self) -> ZfitParameter | None:
        raise NotImplementedError

    @abstractmethod
    def normalization(self, limits: ztyping.LimitsType) -> ztyping.NumericalTypeReturn:
        raise NotImplementedError

    @abstractmethod
    def as_func(self, norm_range: ztyping.LimitsType = False):
        raise NotImplementedError


class ZfitFunctorMixin:
    @property
    @abstractmethod
    def models(self) -> dict[float | int | str, ZfitModel]:
        raise NotImplementedError

    @abstractmethod
    def get_models(self) -> list[ZfitModel]:
        raise NotImplementedError
