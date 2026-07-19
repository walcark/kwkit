"""Plotting helpers. Requires the ``viz`` extra (``pip install kwkit[viz]``).

Built as a thin ergonomic layer over matplotlib and SciencePlots: every helper
takes an optional ``ax`` and returns it, none call ``show``/``savefig`` behind
your back (except the explicit ``save``), and styling is scoped through the
``style`` context manager. Importing this module pulls matplotlib and
scienceplots, hence the lazy loading at package level: ``import kwkit`` never
imports them on its own.
"""

from __future__ import annotations

from ._io import save
from ._layout import colorbar, figure
from ._style import style

__all__ = ["colorbar", "figure", "save", "style"]
