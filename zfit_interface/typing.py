from __future__ import annotations

import sys
from typing import TYPE_CHECKING
from typing import Any
from typing import Tuple
from typing import Union

from zfit_interface.variables import ZfitParam
from zfit_interface.variables import ZfitSpace

if sys.version_info < (3, 8):
    from typing_extensions import Protocol
else:
    from typing import Protocol

if TYPE_CHECKING:
    from builtins import ellipsis

    import tensorflow as tf
    from numpy.typing import ArrayLike

    TensorLike = tf.python.types.core.Tensor | tf.python.types.core.TensorProtocol

else:
    ArrayLike = Any
    TensorLike = Any

RealScalar = Union[float, int, ArrayLike, TensorLike]
VarInputType = Union[ZfitSpace, ZfitData, ZfitParam]
NormInputType = Union[ZfitSpace, ZfitData, ZfitParam]
