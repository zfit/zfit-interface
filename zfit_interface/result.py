from abc import abstractmethod
from typing import Mapping, Union

from zfit_interface.loss import ZfitMinimalLoss
from zfit_interface.minimizer import ZfitMinimizer
from zfit_interface.param import ZfitParameter


class ZfitMinimalResult:

    @property
    @abstractmethod
    def minimizer(self) -> ZfitMinimizer:
        raise NotImplementedError

    @property
    @abstractmethod
    def params(self) -> Mapping[Union[ZfitParameter], Mapping[str, object]]:
        raise NotImplementedError

    @property
    @abstractmethod
    def fmin(self) -> float:
        raise NotImplementedError

    @property
    @abstractmethod
    def valid(self) -> bool:
        raise NotImplementedError

    @property
    @abstractmethod
    def loss(self) -> ZfitMinimalLoss:
        raise NotImplementedError


class ZfitResult:
    @abstractmethod
    def hesse(self, params, method):
        """Calculate for `params` the symmetric error using the Hessian matrix.

        Args:
            params: The parameters  to calculate the
                Hessian symmetric error. If None, use all parameters.
            method: the method to calculate the hessian. Can be {'minuit'} or a callable.

        Returns:
            Result of the hessian (symmetric) error as dict with each parameter holding
                the error dict {'error': sym_error}.

                So given param_a (from zfit.Parameter(.))
                `error_a = result.hesse(params=param_a)[param_a]['error']`
                error_a is the hessian error.
        """
        raise NotImplementedError

    @abstractmethod
    def errors(self, params, method, sigma):
        """Calculate and set for `params` the asymmetric error using the set error method.

            Args:
                params: The parameters or their names to calculate the
                     errors. If `params` is `None`, use all *floating* parameters.
                method: The method to use to calculate the errors. Valid choices are
                    {'minuit_minos'} or a Callable.

            Returns:
                A `OrderedDict` containing as keys the parameter names and as value a `dict` which
                    contains (next to probably more things) two keys 'lower' and 'upper',
                    holding the calculated errors.
                    Example: result['par1']['upper'] -> the asymmetric upper error of 'par1'
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def edm(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def converged(self):
        raise NotImplementedError
