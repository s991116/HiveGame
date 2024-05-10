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