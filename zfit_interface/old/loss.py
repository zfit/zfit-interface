from abc import abstractmethod


class ZfitMinimalLoss:
    @abstractmethod
    def gradients(self, params: ztyping.ParamTypeInput = None) -> List[float]:
        raise NotImplementedError

    @abstractmethod
    def value(self) -> ztyping.NumericalTypeReturn:
        raise NotImplementedError

    @property
    @abstractmethod
    def errordef(self) -> float:
        raise NotImplementedError
