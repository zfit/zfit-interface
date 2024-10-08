from __future__ import annotations

import sys
from typing import TYPE_CHECKING
from typing import Any
from typing import Iterable
from typing import Mapping
from typing import Protocol
from typing import Tuple
from typing import Union

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
LimitsInputType = Union["variables.ZfitSpace", "data.ZfitData", "variables.ZfitParam"]
PDFReturnType = TensorLike

OptionsInputType = Mapping[str, object]

Variable = Union["variables.ZfitVar", Iterable["variables.ZfitVar"]]
