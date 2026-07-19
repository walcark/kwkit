"""Scoped matplotlib styling built on SciencePlots."""

from __future__ import annotations

from contextlib import contextmanager
from importlib import resources
from typing import TYPE_CHECKING

import matplotlib.pyplot as plt
import scienceplots  # noqa: F401  (import registers the "science" styles)

if TYPE_CHECKING:
    from collections.abc import Iterator

_OVERLAY = "kwkit.mplstyle"


@contextmanager
def style(*extra: str, latex: bool = False, overlay: bool = True) -> Iterator[None]:
    """Apply the kwkit plotting style within a scoped context.

    Stacks, in order, the SciencePlots ``science`` base, any *extra* SciencePlots
    presets, ``no-latex`` (unless *latex* is set), and finally the personal
    ``kwkit.mplstyle`` overlay so that local tweaks win.

    Parameters
    ----------
    *extra : str
        Extra SciencePlots preset names to stack, e.g. ``"ieee"`` or ``"grid"``.
    latex : bool, default False
        Render text with LaTeX. Off by default to keep environments portable
        (no system LaTeX required); turn on for publication figures.
    overlay : bool, default True
        Stack the personal ``kwkit.mplstyle`` overlay on top.

    Yields
    ------
    None
        Control within the styled context.
    """
    presets: list[str] = ["science", *extra]
    if not latex:
        presets.append("no-latex")
    with _overlay_path(overlay) as path:
        styles = [*presets, path] if path is not None else presets
        with plt.style.context(styles):
            yield


@contextmanager
def _overlay_path(enabled: bool) -> Iterator[str | None]:
    """Yield the on-disk path to the overlay, or None when disabled."""
    if not enabled:
        yield None
        return
    ref = resources.files(__package__) / _OVERLAY
    with resources.as_file(ref) as path:
        yield str(path)
