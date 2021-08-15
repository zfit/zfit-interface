from __future__ import annotations

import sys
from typing import TYPE_CHECKING
from typing import Any
from typing import Iterable
from typing import Tuple
from typing import Union

if sys.version_info < (3, 8):
    from typing_extensions import Protocol
else:
    from typing import Protocol

import zfit_interface.data as data
import zfit_interface.variables as variables

if TYPE_CHECKING:
    from builtins import ellipsis

    import tensorflow as tf
    from numpy.typing import ArrayLike

    TensorLike = Union[tf.python.types.core.Tensor, tf.python.types.core.TensorProtocol]

else:
    ArrayLike = Any
    TensorLike = Any

RealScalar = Union[float, int, ArrayLike, TensorLike]
VarInputType = Union["variables.ZfitSpace", "data.ZfitData", "variables.ZfitParam"]
NormInputType = Union["variables.ZfitSpace", "data.ZfitData", "variables.ZfitParam"]
PDFReturnType = TensorLike

Variable = Union["variables.ZfitVar", Iterable["variables.ZfitVar"]]
