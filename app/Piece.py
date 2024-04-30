from __future__ import annotations
from dataclasses import dataclass
from app.Creatures import Creatures

@dataclass
class Piece:
 
  firstPlayer: bool
  creature: Creatures
  index: int

  def print(self) -> str:
    if(self.firstPlayer):
      return self.creature.value.upper() + str(self.index)
    else:
      return self.creature.value.lower() + str(self.index)

  def __eq__(self, other: any): # type: ignore
    if isinstance(other, Piece):
      return self.firstPlayer == other.firstPlayer and self.creature == other.creature and self.index == other.index # type: ignore
    return False