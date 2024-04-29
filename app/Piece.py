from __future__ import annotations
from app.Creatues import Creatues

class Piece:

    def __init__(self, firstPlayer: bool, creature: Creatues, index: int) -> None:
        self.firstPlayer = firstPlayer
        self.creature = creature
        self.index = index

    def print(self) -> str:
        if(self.firstPlayer):
            return self.creature.value.upper() + str(self.index)
        else:
            return self.creature.value.lower() + str(self.index)

    def __eq__(self, other: any): # type: ignore
        if isinstance(other, Piece):
            return self.firstPlayer == other.firstPlayer and self.creature == other.creature and self.index == other.index # type: ignore
        return False