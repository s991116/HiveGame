# test_my_module.py

import unittest
from HiveBoard import HiveBoard

class TestPrint(unittest.TestCase):

    def test_print_empty_board(self):
        #Arrange
        hiveGame = HiveBoard()

        #Act
        boardPrint = hiveGame.printBoard()

        #Assert
        self.assertEqual(boardPrint, "")
        
    def test_print_board_with_one_piece(self):
        #Arrange
        hiveBoard = HiveBoard()
        hiveBoard.setPosition("Q")

        #Act
        boardPrint = hiveBoard.printBoard()

        #Assert
        self.assertEqual(boardPrint, "Q")

    def test_print_board_with_two_pieces(self):
        #Arrange
        hiveBoard = HiveBoard()
        hiveBoard.setPosition("""
                             q|Q
                             """)

        #Act
        boardPrint = hiveBoard.printBoard()

        #Assert
        self.assertEqual(boardPrint, "q|Q")


if __name__ == "__main__":
    unittest.main()
