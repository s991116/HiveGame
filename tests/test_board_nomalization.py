import unittest
from app.HiveBoard import HiveBoard
from app.Creatures import Creatures
from app.Coordinate import Coordinate
from app.HivePieces import HivePieces

class TestBoardNomalization(unittest.TestCase):

    def test_center_P1_QueenBee(self):
        #Arrange
        hiveBoard = HiveBoard()
        pieces = hiveBoard.pieces

        #Act
        hiveBoard.movePiece(HivePieces.CreateCloneWithCoordinate(pieces.Spider_0_P1, Coordinate(0,0)))
        hiveBoard.movePiece(HivePieces.CreateCloneWithCoordinate(pieces.Spider_0_P2, Coordinate(-1,0)))
        hiveBoard.movePiece(HivePieces.CreateCloneWithCoordinate(pieces.QueenBee_P1, Coordinate(+1,0)))

        #Assert
        board = hiveBoard.getBoard()
        
        self.assertEqual(len(board), 3)
        for boardPiece in board:
            if(boardPiece.piece.creature == Creatures.QueenBee and boardPiece.piece.firstPlayer):
                self.assertEqual(boardPiece.coordinate, Coordinate(0,0))
        
    def test_center_P1_QueenBee_PlacedFirst(self):
        #Arrange
        hiveBoard = HiveBoard()
        pieces = hiveBoard.pieces

        #Act
        hiveBoard.movePiece(HivePieces.CreateCloneWithCoordinate(pieces.QueenBee_P1, Coordinate(0,0)))
        hiveBoard.movePiece(HivePieces.CreateCloneWithCoordinate(pieces.Spider_0_P2, Coordinate(-1,0)))
        hiveBoard.movePiece(HivePieces.CreateCloneWithCoordinate(pieces.Spider_0_P1, Coordinate(+1,0)))

        #Assert
        board = hiveBoard.getBoard()
        
        self.assertEqual(len(board), 3)
        for boardPiece in board:
            if(boardPiece.piece.creature == Creatures.QueenBee and boardPiece.piece.firstPlayer):
                self.assertEqual(boardPiece.coordinate, Coordinate(0,0))

if __name__ == "__main__":
    unittest.main()
