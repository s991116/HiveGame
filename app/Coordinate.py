from __future__ import annotations
from dataclasses import dataclass
from app.Directions import Direction

@dataclass
class Coordinate:
  x: int
  y: int

  def NeighbourCoordinate(self, direction: Direction) -> Coordinate:
  
    if(direction == Direction.LEFT):
      return Coordinate(self.x-1, self.y)
    elif(direction == Direction.RIGHT):
      return Coordinate(self.x+1, self.y)
    elif(direction == Direction.UP_LEFT):
      return Coordinate(self.x+1, self.y+1)
    elif(direction == Direction.UP_RIGHT):
      return Coordinate(self.x, self.y+1)
    elif(direction == Direction.DOWN_LEFT):  
      return Coordinate(self.x-1, self.y-1)
    elif(direction == Direction.DOWN_RIGHT): 
      return Coordinate(self.x,self.y-1)
    
    raise Exception("Unknown Direction")