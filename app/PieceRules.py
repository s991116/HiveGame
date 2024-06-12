from __future__ import annotations

from typing import List, TYPE_CHECKING


if TYPE_CHECKING:
  from app.BoardPiece import BoardPiece
  from app.HiveBoard import HiveBoard

class PieceRules:

  def getMoves(self, boardPiece: BoardPiece, board: HiveBoard) -> List[BoardPiece]:
    return []


  