from __future__ import annotations

from dataclasses import dataclass
from app.Species import Species

@dataclass
class Piece:
 
  firstPlayer: bool
  creature: Species
  index: int

  def print(self) -> str:
    if(self.firstPlayer):
      return self.creature.value.upper() + str(self.index)
    else:
      return self.creature.value.lower() + str(self.index)