from __future__ import annotations

from dataclasses import dataclass

@dataclass(unsafe_hash=True)
class Coordinate:
  x: int
  y: int