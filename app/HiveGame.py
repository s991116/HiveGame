from typing import List
from app.HiveBoard import HiveBoard
from app.BoardPiece import BoardPiece
from app.HiveRules import HiveRules
class HiveGame:

  def __init__(self) -> None:  
    self.board = HiveBoard()
    self.rules = HiveRules(self.board)

  def playMove(self, move: BoardPiece):
    self.rules.playMove(move)

  def getValidMoves(self) -> List[BoardPiece]:
    return self.rules.getValidMoves()
  
  def getBoard(self) -> List[BoardPiece]:
    return self.board.getBoard()
  
  def setupPosition(self, boardPrint: List[str], playerOneTurn: bool):      
    self.board.setupPosition(boardPrint)
    self.rules.playerOneTurn = playerOneTurn
    self.rules.updatePosition()