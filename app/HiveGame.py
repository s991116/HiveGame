from typing import List
from app.Piece import Piece
from app.HiveBoard import HiveBoard
from app.HiveRules import HiveRules
class HiveGame:

  def __init__(self) -> None:  
    self.board = HiveBoard()
    self.rules = HiveRules(self.board)

  def playMove(self, move: Piece):
    self.rules.playMove(move)

  def getValidMoves(self) -> List[Piece]:
    return self.rules.getValidMoves()
  
  def getBoard(self) -> List[Piece]:
    return self.board.getBoard()
  
  def setupPosition(self, boardPrint: str, playerOneTurn: bool):      
    self.board.setupPosition(boardPrint)
    self.rules.playerOneTurn = playerOneTurn
    self.rules.updatePosition()