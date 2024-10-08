from __future__ import annotations


class ZfitData:
    def values(self):
        raise NotImplementedError

    @property
    def axes(self):
        raise NotImplementedError

    @property
    def is_binned(self):
        raise NotImplementedError

    @property
    def is_unbinned(self):
        raise NotImplementedError


class ZfitHistData(ZfitData):
    def variances(self):
        raise NotImplementedError

    # @property
    # def axes(self):
    #     raise NotImplementedError

    def counts(self):
        raise NotImplementedError


class ZfitMixedData(ZfitData):
    @property
    def weights(self):
        raise NotImplementedError
