import unittest

from app.HivePiece import HivePiece
from app.Coordinate import Coordinate
from app.HivePieceBuilder import HivePieceBuilder
from tests.HiveGameTestBuilder import HiveGameTestBuilder

class TestBoardNomalization(unittest.TestCase):

    def test_center_P1_QueenBee(self):
        #Arrange
        #Act
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.Spider_0_P1, 0, 0).\
            Play(HivePiece.Spider_0_P2,-1, 0).\
            Play(HivePiece.QueenBee_P1,+1, 0).\
            Build()

        #Assert
        board = hiveGame.board.getBoard()
        
        self.assertEqual(len(board), 3)
        self.assertIn(HivePieceBuilder().Build(HivePiece.QueenBee_P1, Coordinate(0,0)), board)
        
    def test_center_P1_QueenBee_PlacedFirst(self):
        #Arrange
        #Act
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1, 0, 0).\
            Play(HivePiece.Spider_0_P2,-1, 0).\
            Play(HivePiece.Spider_0_P1,+1, 0).\
            Build()

        #Assert
        board = hiveGame.board.getBoard()
        
        self.assertEqual(len(board), 3)
        self.assertIn(HivePieceBuilder().Build(HivePiece.QueenBee_P1, Coordinate(0,0)), board)        

if __name__ == "__main__":
    unittest.main()
