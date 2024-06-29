import unittest
from app.Coordinate import Coordinate
from app.HivePiece import HivePiece
from tests.HiveGameTestBuilder import HiveGameTestBuilder
from app.BoardPieceBuilder import BoardPieceBuilder
from app.PieceBuilder import PieceBuilder

param_list = [('a', 'a'), ('a', 'b'), ('b', 'b')]

class TestMovmentSpider(unittest.TestCase):

    def test_movement_spider(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1,      0, 0).\
            Play(HivePiece.Ant_0_P2, -1, 0).\
            Play(HivePiece.Spider_0_P1, 1, 0).\
            Play(HivePiece.Ant_1_P2, -2, 0).\
            Build()

        #Act
        spiderPiece = PieceBuilder().Spider_0_P1().Build()
        s = hiveGame.board.findPiece(spiderPiece)
        if s is not None:
            spiderMoves = s.getMoves(hiveGame.board)
        else:
            spiderMoves = []

        print(hiveGame.board.printBoard())

        #Assert
        expectedMove1 = BoardPieceBuilder().WithPiece(spiderPiece).WithCoordinate(Coordinate(-2,1)).Build()
        self.assertIn(expectedMove1, spiderMoves)
        expectedMove2 = BoardPieceBuilder().WithPiece(spiderPiece).WithCoordinate(Coordinate(-2,-1)).Build()
        self.assertIn(expectedMove2, spiderMoves)



if __name__ == "__main__":
    unittest.main()
