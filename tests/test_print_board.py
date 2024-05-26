import unittest
from app.HiveGame import HiveGame
from app.HiveBoard import HiveBoard
from app.HivePieces import HivePieces
from app.Coordinate import Coordinate
from app.Directions import Direction

class TestPrintBoard(unittest.TestCase):

    def test_printBoard_inline(self):
        #Arrange
        hiveGame = HiveGame()
        pieces = HivePieces()

        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.QueenBee_P1, Coordinate(0,0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Grasshopper_0_P2, Coordinate(-1,0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Grasshopper_0_P1, Coordinate(1,0)))

        #Act
        boardPrint = hiveGame.board.printBoard()

        #Assert
        number_of_lines = boardPrint.count('\n')
        self.assertEqual(1+3, number_of_lines)

    def test_printBoard_2_lines(self):
        #Arrange
        hiveGame = HiveGame()
        pieces = HivePieces()

        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.QueenBee_P1, Coordinate(0,0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Grasshopper_0_P2, Coordinate(-1,0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Grasshopper_0_P1, Coordinate(0,1)))

        #Act
        boardPrint = hiveGame.board.printBoard()

        #Assert
        number_of_lines = boardPrint.count('\n')
        self.assertEqual(1+6, number_of_lines)

    def test_printBoard_3_lines(self):
        #Arrange
        hiveBoard = HiveBoard()
        hivePieces = HivePieces()

        centerCoordination = Coordinate(1,1)

        hiveBoard.movePiece(HivePieces.CreateCloneWithCoordinate(hivePieces.Beetle_0_P1, centerCoordination))

        hiveBoard.movePiece(HivePieces.CreateCloneWithCoordinate(hivePieces.Ant_0_P1, hiveBoard.navigate(Direction.LEFT, centerCoordination)))
        hiveBoard.movePiece(HivePieces.CreateCloneWithCoordinate(hivePieces.Ant_1_P1, hiveBoard.navigate(Direction.DOWN_LEFT, centerCoordination)))
        hiveBoard.movePiece(HivePieces.CreateCloneWithCoordinate(hivePieces.Ant_2_P1, hiveBoard.navigate(Direction.DOWN_RIGHT, centerCoordination)))

        hiveBoard.movePiece(HivePieces.CreateCloneWithCoordinate(hivePieces.Grasshopper_0_P1, hiveBoard.navigate(Direction.RIGHT, centerCoordination)))
        hiveBoard.movePiece(HivePieces.CreateCloneWithCoordinate(hivePieces.Grasshopper_0_P1, hiveBoard.navigate(Direction.UP_RIGHT, centerCoordination)))
        hiveBoard.movePiece(HivePieces.CreateCloneWithCoordinate(hivePieces.Grasshopper_0_P1, hiveBoard.navigate(Direction.UP_LEFT, centerCoordination)))

        #Act
        boardPrint = hiveBoard.printBoard()
        print(boardPrint)

        #Assert
        number_of_lines = boardPrint.count('\n')
        self.assertEqual(1+9, number_of_lines)

    def test_printBoard_empty_space_between_lines(self):
        #Arrange
        hiveBoard = HiveBoard()
        hivePieces = HivePieces()

        hiveBoard.movePiece(HivePieces.CreateCloneWithCoordinate(hivePieces.Beetle_0_P1, Coordinate(0,0)))

        hiveBoard.movePiece(HivePieces.CreateCloneWithCoordinate(hivePieces.Ant_0_P1, Coordinate(0,1)))
        hiveBoard.movePiece(HivePieces.CreateCloneWithCoordinate(hivePieces.Ant_1_P1, Coordinate(1,1)))
        hiveBoard.movePiece(HivePieces.CreateCloneWithCoordinate(hivePieces.Ant_2_P1, Coordinate(2,1)))

        hiveBoard.movePiece(HivePieces.CreateCloneWithCoordinate(hivePieces.Beetle_1_P1, Coordinate(3,0)))

        hiveBoard.movePiece(HivePieces.CreateCloneWithCoordinate(hivePieces.Grasshopper_0_P1, Coordinate(2,-1)))
        hiveBoard.movePiece(HivePieces.CreateCloneWithCoordinate(hivePieces.Grasshopper_1_P1, Coordinate(1,-1)))
        hiveBoard.movePiece(HivePieces.CreateCloneWithCoordinate(hivePieces.Grasshopper_2_P1, Coordinate(0,-1)))

        #Act
        boardPrint = hiveBoard.printBoard()
        print(boardPrint)

        #Assert
        number_of_lines = boardPrint.count('\n')
        self.assertEqual(1+9, number_of_lines)



if __name__ == "__main__":
    unittest.main()
