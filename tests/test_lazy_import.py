"""Tests for the lazy-loading behaviour of the top-level package."""

from __future__ import annotations

import sys

import pytest


class TestLazyImport:
    def test_import_kwkit_does_not_import_matplotlib(self) -> None:
        """Importing kwkit must not pull the heavy viz dependency."""
        for name in list(sys.modules):
            if name == "matplotlib" or name.startswith("matplotlib."):
                del sys.modules[name]
        import kwkit  # noqa: F401

        assert "matplotlib" not in sys.modules

    def test_core_is_accessible_as_attribute(self) -> None:
        """Domain submodules resolve through the lazy __getattr__."""
        import kwkit

        assert hasattr(kwkit.core, "unit_vector")

    def test_unknown_attribute_raises(self) -> None:
        """Accessing an unknown attribute raises AttributeError."""
        import kwkit

        with pytest.raises(AttributeError):
            _ = kwkit.does_not_exist
