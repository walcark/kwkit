"""Figure and colorbar plumbing with sane defaults."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import matplotlib.pyplot as plt

if TYPE_CHECKING:
    from matplotlib.cm import ScalarMappable
    from matplotlib.colorbar import Colorbar
    from matplotlib.figure import Figure


def figure(
    nrows: int = 1,
    ncols: int = 1,
    *,
    figsize: tuple[float, float] | None = None,
    constrained: bool = True,
    **kwargs: Any,
) -> tuple[Figure, Any]:
    """Create a figure and its axes with kwkit defaults.

    Thin wrapper over ``plt.subplots`` that enables constrained layout by
    default. The second element is a single ``Axes`` for a 1x1 grid, otherwise
    an array of axes, exactly like ``plt.subplots``.

    Parameters
    ----------
    nrows, ncols : int, default 1
        Grid shape of the subplots.
    figsize : tuple of float, optional
        Figure size in inches; defaults to the active style.
    constrained : bool, default True
        Use matplotlib constrained layout for automatic spacing.
    **kwargs
        Forwarded to ``plt.subplots``.

    Returns
    -------
    tuple
        The figure and its axes (single ``Axes`` or an array).
    """
    layout = "constrained" if constrained else None
    return plt.subplots(nrows, ncols, figsize=figsize, layout=layout, **kwargs)


def colorbar(
    mappable: ScalarMappable,
    ax: Any = None,
    *,
    label: str | None = None,
    **kwargs: Any,
) -> Colorbar:
    """Attach a well-aligned colorbar to *ax* (or the current axes).

    Parameters
    ----------
    mappable : matplotlib.cm.ScalarMappable
        The mappable to describe, e.g. the return of ``imshow`` or ``pcolormesh``.
    ax : matplotlib.axes.Axes, optional
        Axes to steal space from; defaults to the current axes.
    label : str, optional
        Colorbar label.
    **kwargs
        Forwarded to ``Figure.colorbar``.

    Returns
    -------
    matplotlib.colorbar.Colorbar
        The created colorbar.
    """
    target = plt.gca() if ax is None else ax
    fig = target.get_figure()
    if fig is None:  # pragma: no cover - an Axes always has a figure
        raise RuntimeError("axes is not attached to a figure")
    cbar = fig.colorbar(mappable, ax=target, **kwargs)
    if label is not None:
        cbar.set_label(label)
    return cbar
