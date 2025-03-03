from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
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
