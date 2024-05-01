import unittest
from app.HiveGame import HiveGame

class TestMovmentRules(unittest.TestCase):

    def test_move_piece_after_P1_Queen_is_placed(self):
        #Arrange
        hiveGame = HiveGame()
        hiveGame.setupPosition(["b0|Q0"], True)

        #Act
        moves = hiveGame.getValidMoves()

        #Arrange
        self.assertEqual(len(moves), 9)



if __name__ == "__main__":
    unittest.main()
