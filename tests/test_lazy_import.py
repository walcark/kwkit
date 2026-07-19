"""Tests for the lazy-loading behaviour of the top-level package."""

from __future__ import annotations

import subprocess
import sys

import pytest


class TestLazyImport:
    def test_import_kwkit_does_not_import_matplotlib(self) -> None:
        """Importing kwkit must not pull the heavy viz dependency.

        Checked in a fresh subprocess so the assertion sees a clean import
        state and never mutates matplotlib for the rest of the suite.
        """
        code = (
            "import sys, kwkit; "
            "loaded = [m for m in sys.modules if m.split('.')[0] == 'matplotlib']; "
            "assert not loaded, loaded"
        )
        subprocess.run([sys.executable, "-c", code], check=True)

    def test_core_is_accessible_as_attribute(self) -> None:
        """Domain submodules resolve through the lazy __getattr__."""
        import kwkit

        assert hasattr(kwkit.core, "unit_vector")

    def test_unknown_attribute_raises(self) -> None:
        """Accessing an unknown attribute raises AttributeError."""
        import kwkit

        with pytest.raises(AttributeError):
            _ = kwkit.does_not_exist
