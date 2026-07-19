"""Small vector-geometry helpers shared by optics and Monte-Carlo code."""

from __future__ import annotations

import numpy as np
import numpy.typing as npt


def unit_vector(vectors: npt.ArrayLike, axis: int = -1) -> npt.NDArray[np.float64]:
    """Return *vectors* scaled to unit L2 norm along *axis*.

    Parameters
    ----------
    vectors : array_like
        Input vectors, e.g. ray directions of shape ``(..., 3)``.
    axis : int, default -1
        Axis along which each vector is normalised.

    Returns
    -------
    numpy.ndarray
        Float array with the same shape as *vectors*, unit norm along *axis*.

    Raises
    ------
    ValueError
        If any vector has a zero norm and cannot be normalised.
    """
    array = np.asarray(vectors, dtype=np.float64)
    norm = np.linalg.norm(array, axis=axis, keepdims=True)
    if np.any(norm == 0.0):
        raise ValueError("cannot normalise a zero-norm vector")
    return array / norm
