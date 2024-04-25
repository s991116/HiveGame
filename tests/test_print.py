# test_my_module.py

import unittest
from HiveGame import HiveGame

class TestPrint(unittest.TestCase):

    def test_print_empty_board(self):
        #Arrange
        hiveGame = HiveGame()

        #Act
        boardPrint = hiveGame.printBoard()

        #Assert
        self.assertEqual(boardPrint, "")
        
    def test_print_board_with_one_piece(self):
        #Arrange
        hiveGame = HiveGame()
        hiveGame.setPiece(hiveGame.getValidMoves()[0])
        #Act
        boardPrint = hiveGame.printBoard()

        #Assert
        self.assertEqual(boardPrint, "Q")

    def test_print_board_with_two_pieces(self):
        #Arrange
        hiveGame = HiveGame()
        hiveGame.setPiece(hiveGame.getValidMoves()[0])
        hiveGame.setPiece(hiveGame.getValidMoves()[0])

        #Act
        boardPrint = hiveGame.printBoard()

        #Assert
        self.assertEqual(boardPrint, "q|Q")

if __name__ == "__main__":
    unittest.main()
