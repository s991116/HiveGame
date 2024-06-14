from typing import List
from app.HiveBoard import HiveBoard
from app.HiveRules import HiveRules
from app.GameResult import GameResult
from app.BoardPiece import BoardPiece

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
  
  def getGameState(self) -> GameResult:
    return self.rules.gameResult