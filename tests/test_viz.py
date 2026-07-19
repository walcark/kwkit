"""Tests for kwkit.viz plumbing (skipped when the viz extra is absent)."""

from __future__ import annotations

from pathlib import Path

import pytest

pytest.importorskip("matplotlib")
pytest.importorskip("scienceplots")

import matplotlib  # noqa: E402

matplotlib.use("Agg")

from kwkit import viz  # noqa: E402


class TestFigure:
    def test_single_cell_returns_one_axes(self) -> None:
        fig, ax = viz.figure()
        assert ax.get_figure() is fig

    def test_grid_returns_axes_array(self) -> None:
        _, axes = viz.figure(2, 2)
        assert axes.shape == (2, 2)


class TestSave:
    def test_writes_requested_formats(self, tmp_path: Path) -> None:
        fig, ax = viz.figure()
        ax.plot([0.0, 1.0], [0.0, 1.0])
        paths = viz.save(fig, tmp_path / "out", formats=["png", "pdf"])
        assert [p.suffix for p in paths] == [".png", ".pdf"]
        assert all(p.exists() for p in paths)


class TestColorbar:
    def test_colorbar_carries_label(self) -> None:
        fig, ax = viz.figure()
        img = ax.imshow([[0.0, 1.0], [2.0, 3.0]])
        cbar = viz.colorbar(img, ax=ax, label="intensity")
        assert cbar.ax.get_ylabel() == "intensity"


class TestStyle:
    def test_style_context_resolves_without_latex(self) -> None:
        """Smoke test: the default style stack applies and restores cleanly."""
        with viz.style():
            pass
