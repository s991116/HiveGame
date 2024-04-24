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

if __name__ == "__main__":
    unittest.main()
