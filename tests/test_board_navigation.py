import unittest
from app.HiveBoard import HiveBoard
from app.Directions import Direction
from app.Coordinate import Coordinate
from app.HivePieces import HivePieces

class TestBoardNavigation(unittest.TestCase):

    def test_upLeft_downRight_put_back_to_center(self):
        #Arrange
        hiveBoard = HiveBoard()
        hivePieces = HivePieces()
        startCoordinate = Coordinate(0,0)

        hiveBoard.movePiece(HivePieces.CreateCloneWithCoordinate(hivePieces.QueenBee_P1, startCoordinate))

        #Act
        coordinate_DR = hiveBoard.navigate(Direction.DOWN_RIGHT, startCoordinate)
        hiveBoard.movePiece(HivePieces.CreateCloneWithCoordinate(hivePieces.Ant_0_P1, coordinate_DR))

        coordinate_DR_UL = hiveBoard.navigate(Direction.UP_LEFT, coordinate_DR)

        print(hiveBoard.printBoard())

        #Assert
        self.assertEqual(startCoordinate, coordinate_DR_UL)


if __name__ == "__main__":
    unittest.main()
