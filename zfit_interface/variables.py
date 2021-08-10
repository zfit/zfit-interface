from __future__ import annotations

from collections.abc import Iterable

from zfit_interface.typing import RealScalar


class ZfitVar:
    @property
    def name(self) -> str:
        raise NotImplementedError

    @property
    def label(self) -> str:
        raise NotImplementedError


class ZfitAxis(ZfitVar):
    @property
    def lower(self) -> RealScalar:
        raise NotImplementedError

    @property
    def upper(self) -> RealScalar:
        raise NotImplementedError


class ZfitVars:
    @property
    def names(self) -> Iterable[str]:
        raise NotImplementedError

    @property
    def label(self) -> Iterable[str]:
        raise NotImplementedError


class ZfitSpace(ZfitVars):
    @property
    def lower(self) -> RealScalar:
        raise NotImplementedError

    @property
    def upper(self) -> RealScalar:
        raise NotImplementedError


class ZfitParam(ZfitVar):
    def value(self) -> RealScalar:
        raise NotImplementedError

    @property
    def limit(self) -> tuple[RealScalar, RealScalar]:
        return self.lower, self.upper

    @property
    def lower(self) -> RealScalar:
        raise NotImplementedError

    @property
    def upper(self) -> RealScalar:
        raise NotImplementedError

    @property
    def stepsize(self) -> RealScalar:
        raise NotImplementedError

    @property
    def floating(self):
        raise NotImplementedError
