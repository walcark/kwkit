"""kwkit: personal reusable toolbox, organised by domain.

Submodules are imported lazily (PEP 562): ``import kwkit`` stays instant and
free of heavy dependencies. A domain module (and its optional dependencies) is
only loaded the first time it is accessed, e.g. ``kwkit.viz`` imports
matplotlib only then. If the matching extra is missing, the ``ImportError`` is
raised at use time, not at startup.
"""

from __future__ import annotations

import importlib
from typing import TYPE_CHECKING, Any

__version__ = "0.1.0"

# Domain submodules exposed via lazy loading. Add a name here after creating the
# matching subpackage under ``src/kwkit/``.
_SUBMODULES = frozenset(
    {
        "core",
        "optics",
        "montecarlo",
        "atmo",
        "viz",
    }
)

__all__ = sorted(_SUBMODULES)

if TYPE_CHECKING:  # help IDEs and mypy resolve attribute access statically
    from kwkit import atmo, core, montecarlo, optics, viz  # noqa: F401


def __getattr__(name: str) -> Any:
    """Import a domain submodule lazily on first access."""
    if name in _SUBMODULES:
        module = importlib.import_module(f".{name}", __name__)
        globals()[name] = module  # cache so the import happens once
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    """List public attributes, including the lazy submodules."""
    return sorted(set(globals()) | _SUBMODULES)
