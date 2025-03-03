from __future__ import annotations

import typing
from collections.abc import Iterable
from typing import T

import zfit_interface.typing as ztyping

# from uhi.typing.plottable import PlottableTraits


class ZfitVar:
    @property
    def name(self) -> str:
        raise NotImplementedError

    @property
    def label(self) -> str:
        raise NotImplementedError

    @property
    def binning(self):
        raise NotImplementedError

    @property
    def is_binned(self):
        raise NotImplementedError


class ZfitBinning:
    @property
    def traits(self) -> PlottableTraits: ...

    def __getitem__(self, index: int) -> T:
        """Get the pair of edges (not discrete) or bin label (discrete)."""

    def __len__(self) -> int:
        """Return the number of bins (not counting flow bins, which are ignored for this Protocol currently)."""

    def __eq__(self, other: typing.Any) -> bool:
        """Required to be sequence-like."""

    def __iter__(self) -> typing.Iterator[T]:
        """Useful element of a Sequence to include."""


class PlottableTraits:
    __slots__ = ["_circular", "_discrete"]

    def __init__(self, circular: bool | None = None, discrete: bool | None = None):
        self._circular = False if circular is None else circular
        self._discrete = False if discrete is None else discrete

    @property
    def circular(self) -> bool:
        """True if the axis "wraps around"."""
        return self._circular

    @property
    def discrete(self) -> bool:
        """
        True if each bin is discrete - Integer, Boolean, or Category, for example
        """
        return self._discrete

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, PlottableTraits):
            return NotImplemented
        return not (self.circular ^ o.circular or self.discrete ^ o.discrete)


continuous_trait = PlottableTraits(circular=False, discrete=False)


class BaseBinning(ZfitBinning):
    def __init__(self, traits: PlottableTraits = None, **kwargs) -> None:
        super().__init__(**kwargs)
        traits._traits = traits if traits is not None else continuous_trait

    @property
    def traits(self) -> PlottableTraits:
        return self._traits


class BaseVar(ZfitVar):
    def __init__(self, name: str, binning: ZfitBinning = None, label: str | None = None):
        self._name = name
        self._label = label
        self._binning = self._check_input_init_binning(binning)

    @property
    def name(self) -> str:
        return self._name

    @property
    def label(self) -> str:
        return self._label or self.name

    @property
    def is_binned(self):
        return self.binning is not None

    @property
    def binning(self):
        return self._binning

    def __repr__(self) -> str:
        return f"<Var {self.label}, binned={self.binning}>"

    def _check_input_init_binning(self, binning):
        return binning


class ZfitVars:
    @property
    def names(self) -> Iterable[str]:
        raise NotImplementedError

    @property
    def labels(self) -> Iterable[str]:
        raise NotImplementedError

    @property
    def binnings(self):
        raise NotImplementedError


class ZfitAxis(ZfitVar):
    @property
    def lower(self) -> ztyping.RealScalar:
        raise NotImplementedError

    @property
    def upper(self) -> ztyping.RealScalar:
        raise NotImplementedError


class ZfitSpace(ZfitVar):  # TODO: how to name things?
    @property
    def lower(self) -> ztyping.RealScalar:
        raise NotImplementedError

    @property
    def upper(self) -> ztyping.RealScalar:
        raise NotImplementedError


class ZfitParam(ZfitVar):
    """A parameter is primarily used to communicate intentions in two cases:

    1. for a minimizer. It tells the minimizer what the initial value is, what the limits are
    and the stepsize; also whether it is considered to be floating in the fit or fixed.
    2. for a model. It is an unbinned variable that should be regarded, in the default case,
    as
    """

    def value(self) -> ztyping.RealScalar:
        raise NotImplementedError

    @property
    def limit(self) -> tuple[ztyping.RealScalar, ztyping.RealScalar]:
        return self.lower, self.upper

    # @property
    # def lower(self) -> ztyping.RealScalar:
    #     raise NotImplementedError
    #
    # @property
    # def upper(self) -> ztyping.RealScalar:
    #     raise NotImplementedError

    @property
    def stepsize(self) -> ztyping.RealScalar:
        raise NotImplementedError

    @property
    def floating(self) -> bool:
        raise NotImplementedError


class ZfitParams(ZfitVars):
    def values(self) -> Iterable[ztyping.ArrayLike]:
        raise NotImplementedError

    @property
    def limits(self) -> tuple[ztyping.ArrayLike, ztyping.ArrayLike]:
        return self.lower, self.upper

    # @property
    # def lower(self) -> ztyping.RealScalar:
    #     raise NotImplementedError
    #
    # @property
    # def upper(self) -> ztyping.RealScalar:
    #     raise NotImplementedError

    @property
    def stepsizes(self) -> ztyping.ArrayLike:
        raise NotImplementedError

    @property
    def floating(self) -> ztyping.ArrayLike:
        raise NotImplementedError


class ZfitComposedVariable(ZfitVar):
    pass
