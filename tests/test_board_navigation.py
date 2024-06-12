import unittest
from app.Directions import Direction
from app.Coordinate import Coordinate
from app.HivePiece import HivePiece
from tests.HiveGameTestBuilder import HiveGameTestBuilder
from app.BoardPieceBuilder import BoardPieceBuilder

class TestBoardNavigation(unittest.TestCase):

    def test_upLeft_downRight_put_back_to_center(self):
        #Arrange
        startCoordinate = Coordinate(0,0)
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1,      startCoordinate.x, startCoordinate.y).\
            Build()
        coordinate_DR = hiveGame.board.navigate(Direction.DOWN_RIGHT, startCoordinate)

        #Act
        hiveGame.board.movePiece(BoardPieceBuilder().WithHivePiece(HivePiece.SoldierAnt_0_P1, coordinate_DR).Build())
        print(hiveGame.board.printBoard())

        #Assert
        coordinate_DR_UL = hiveGame.board.navigate(Direction.UP_LEFT, coordinate_DR)
        self.assertEqual(startCoordinate, coordinate_DR_UL)


if __name__ == "__main__":
    unittest.main()
