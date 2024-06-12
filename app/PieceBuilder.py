from app.Creatures import Creatures
from app.Piece import Piece

class PieceBuilder:
  def __init__(self) -> None:
    self._firstPlayer = True
    self._creature = Creatures.Grasshopper
    self._index = 0

  def QueenBee_P1(self):
    self.With(Creatures.QueenBee, 0, True)
    return self

  def QueenBee_P2(self):
    self.With(Creatures.QueenBee, 0, False)
    return self
  
  def Beetle_0_P1(self):
    self.With(Creatures.Beetle, 0, True)
    return self

  def Beetle_0_P2(self):
    self.With(Creatures.Beetle, 0, False)
    return self

  def Beetle_1_P1(self):
    self.With(Creatures.Beetle, 1, True)
    return self

  def Beetle_1_P2(self):
    self.With(Creatures.Beetle, 1, False)
    return self

  def Grasshopper_0_P1(self): 
    self.With(Creatures.Grasshopper, 0, True)
    return self

  def Grasshopper_0_P2(self): 
    self.With(Creatures.Grasshopper, 0, False)
    return self

  def Grasshopper_1_P1(self): 
    self.With(Creatures.Grasshopper, 1, True)
    return self

  def Grasshopper_1_P2(self): 
    self.With(Creatures.Grasshopper, 1, False)
    return self

  def Grasshopper_2_P1(self): 
    self.With(Creatures.Grasshopper, 2, True)
    return self

  def Grasshopper_2_P2(self): 
    self.With(Creatures.Grasshopper, 2, False)
    return self

  def SoldierAnt_0_P1(self): 
    self.With(Creatures.SoldierAnt, 0, True)
    return self

  def SoldierAnt_0_P2(self): 
    self.With(Creatures.SoldierAnt, 0, False)
    return self

  def SoldierAnt_1_P1(self): 
    self.With(Creatures.SoldierAnt, 1, True)
    return self

  def SoldierAnt_1_P2(self): 
    self.With(Creatures.SoldierAnt, 1, False)
    return self

  def SoldierAnt_2_P1(self): 
    self.With(Creatures.SoldierAnt, 2, True)
    return self

  def SoldierAnt_2_P2(self): 
    self.With(Creatures.SoldierAnt, 2, False)
    return self

  def Spider_0_P1(self): 
    self.With(Creatures.Spider, 0, True)
    return self

  def Spider_0_P2(self): 
    self.With(Creatures.Spider, 0, False)
    return self

  def Spider_1_P1(self): 
    self.With(Creatures.Spider, 1, True)
    return self

  def Spider_1_P2(self): 
    self.With(Creatures.Spider, 1, False)
    return self

  def With(self, creature: Creatures, index: int, firstPlayer: bool):
    self._creature = creature
    self._index= index
    self._firstPlayer = firstPlayer
    return self

  def Build(self):
    return Piece(self._firstPlayer, self._creature, self._index)