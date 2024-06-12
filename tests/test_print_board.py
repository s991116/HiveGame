import unittest
from app.HivePiece import HivePiece
from tests.HiveGameTestBuilder import HiveGameTestBuilder


class TestPrintBoard(unittest.TestCase):

    def test_printBoard_inline(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1,      0, 0).\
            Play(HivePiece.Grasshopper_0_P2,-1, 0).\
            Play(HivePiece.Grasshopper_0_P1, 1, 0).\
            Build()

        #Act
        boardPrint = hiveGame.board.printBoard()

        #Assert
        number_of_lines = boardPrint.count('\n')
        self.assertEqual(1+3, number_of_lines)

    def test_printBoard_2_lines(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1,      0, 0).\
            Play(HivePiece.Grasshopper_0_P2,-1, 0).\
            Play(HivePiece.Grasshopper_0_P1, 0, 1).\
            Build()

        #Act
        boardPrint = hiveGame.board.printBoard()

        #Assert
        number_of_lines = boardPrint.count('\n')
        self.assertEqual(1+6, number_of_lines)

    def test_printBoard_3_lines(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1,      0, 0).\
            Play(HivePiece.Grasshopper_0_P2,-1, 0).\
            Play(HivePiece.Grasshopper_0_P1, 1, 0).\
            Play(HivePiece.Grasshopper_1_P2,-1,-1).\
            Play(HivePiece.Grasshopper_1_P1, 1, 1).\
            Build()

        #Act
        boardPrint = hiveGame.board.printBoard()
        print(boardPrint)

        #Assert
        number_of_lines = boardPrint.count('\n')
        self.assertEqual(1+9, number_of_lines)

    def test_printBoard_empty_space_between_lines(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1,      0, 0).\
            Play(HivePiece.QueenBee_P2,     -1, 0).\
            Play(HivePiece.Grasshopper_0_P1, 1, 0).\
            Play(HivePiece.Grasshopper_0_P2,-2,-1).\
            Play(HivePiece.Grasshopper_1_P1, 1,-1).\
            Play(HivePiece.Grasshopper_1_P2,-1,-2).\
            Play(HivePiece.Grasshopper_2_P1, 1,-2).\
            Play(HivePiece.Grasshopper_2_P2, 0,-2).\
            Build()

        #Act
        boardPrint = hiveGame.board.printBoard()
        print(boardPrint)

        #Assert
        number_of_lines = boardPrint.count('\n')
        self.assertEqual(1+9, number_of_lines)


if __name__ == "__main__":
    unittest.main()
