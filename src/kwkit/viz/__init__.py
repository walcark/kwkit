"""Plotting helpers. Requires the ``viz`` extra (``pip install kwkit[viz]``).

Importing this module pulls matplotlib, hence the lazy loading at package
level: ``import kwkit`` never imports matplotlib on its own.
"""

from __future__ import annotations

import matplotlib.pyplot as plt  # noqa: F401  (imported to fail fast if missing)

__all__: list[str] = []
