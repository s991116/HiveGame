import unittest
from app.HiveBoard import HiveBoard

class TestPrintBoard(unittest.TestCase):

    def test_printBoard_inline(self):
        #Arrange
        hiveBoard = HiveBoard()
        hiveBoard.setupPosition(["A0|a0|Q0"])

        #Act
        boardPrint = hiveBoard.printBoard()

        #Assert
        number_of_lines = boardPrint.count('\n')
        self.assertEqual(3, number_of_lines)

    def test_printBoard_2_lines(self):
        #Arrange
        hiveBoard = HiveBoard()
        hiveBoard.setupPosition(["A0|a0|Q0",
                                 " |  |S0"])

        #Act
        boardPrint = hiveBoard.printBoard()

        #Assert
        number_of_lines = boardPrint.count('\n')
        self.assertEqual(6, number_of_lines)



if __name__ == "__main__":
    unittest.main()
