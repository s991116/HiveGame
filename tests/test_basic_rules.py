# test_my_module.py

import unittest
from HiveGame import HiveGame

class TestBasicRules(unittest.TestCase):

    def test_start_with_empty_board(self):
        
        #Arrange
        hiveGame = HiveGame()

        #Act
        board = hiveGame.getBoard()

        #Assert
        self.assertEqual(len(board), 0)

    def test_add_first_piece(self):
        
        #Arrange
        hiveGame = HiveGame()
        pieces = hiveGame.playerOnePieces
        onePiece = pieces[0]
        centerPosition = hiveGame.centerPosition

        #Act
        hiveGame.SetPiece(onePiece, centerPosition)

        #Assert
        self.assertEqual(len(hiveGame.getBoard()), 1)


if __name__ == "__main__":
    unittest.main()
