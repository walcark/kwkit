"""Core utilities with no heavy dependencies (numpy at most).

This is the dependency-light foundation reused across the other domains.
"""

from __future__ import annotations

from ._geometry import unit_vector

__all__ = ["unit_vector"]
