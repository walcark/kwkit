"""Tests for kwkit.core helpers."""

from __future__ import annotations

import numpy as np
import pytest

from kwkit.core import unit_vector


class TestUnitVector:
    def test_single_vector_has_unit_norm(self) -> None:
        result = unit_vector([3.0, 4.0])
        np.testing.assert_allclose(result, [0.6, 0.8])

    def test_batch_normalised_along_last_axis(self) -> None:
        vectors = np.array([[3.0, 4.0], [0.0, 2.0]])
        result = unit_vector(vectors)
        norms = np.linalg.norm(result, axis=-1)
        np.testing.assert_allclose(norms, [1.0, 1.0])

    def test_zero_norm_raises(self) -> None:
        with pytest.raises(ValueError, match="zero-norm"):
            unit_vector([0.0, 0.0])
