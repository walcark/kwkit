"""Reproducible figure export."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Sequence

    from matplotlib.figure import Figure


def save(
    fig: Figure,
    path: str | Path,
    *,
    formats: Sequence[str] | None = None,
    dpi: int = 300,
    **kwargs: Any,
) -> list[Path]:
    """Save *fig* reproducibly, optionally to several formats.

    Uses a tight bounding box and a fixed dpi. When *formats* is given, *path*
    is treated as a stem and one file is written per format.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Figure to save.
    path : str or pathlib.Path
        Output path, or stem when *formats* is given.
    formats : sequence of str, optional
        Extensions to write, e.g. ``("png", "pdf")``.
    dpi : int, default 300
        Output resolution.
    **kwargs
        Forwarded to ``Figure.savefig``.

    Returns
    -------
    list of pathlib.Path
        The written files.
    """
    base = Path(path)
    if formats:
        targets = [base.with_suffix(f".{fmt.lstrip('.')}") for fmt in formats]
    else:
        targets = [base]
    saved: list[Path] = []
    for target in targets:
        target.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(target, dpi=dpi, bbox_inches="tight", **kwargs)
        saved.append(target)
    return saved
