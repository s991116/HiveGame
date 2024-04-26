import unittest
from HiveBoard import HiveBoard
from Creatues import Creatues
from Coordinate import Coordinate

class TestBoardNomalization(unittest.TestCase):

    def test_center_P1_QueenBee(self):
        #Arrange
        hiveBoard = HiveBoard()

        #Act
        hiveBoard.setupPosition("A|a|Q")        

        #Assert
        board = hiveBoard.getBoard()
        
        self.assertEqual(len(board), 3)
        for piece in board:
            if(piece.creature == Creatues.QueenBee and piece.firstPlayer):
                self.assertEqual(piece.coordinate, Coordinate(0,0))
        
    def test_center_P1_QueenBee_PlacedFirst(self):
        #Arrange
        hiveBoard = HiveBoard()

        #Act
        hiveBoard.setupPosition("A|Q|a")        

        #Assert
        board = hiveBoard.getBoard()
        
        self.assertEqual(len(board), 3)
        for piece in board:
            if(piece.creature == Creatues.QueenBee and piece.firstPlayer):
                self.assertEqual(piece.coordinate, Coordinate(0,0))

if __name__ == "__main__":
    unittest.main()
