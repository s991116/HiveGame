# test_my_module.py

import unittest
from HiveBoard import HiveBoard
from Creatues import Creatues
from Position import Position
from Coordinate import Coordinate

class TestBoardNomalization(unittest.TestCase):

    def test_center_P1_QueenBee(self):
        #Arrange
        hiveBoard = HiveBoard()

        #Act
        hiveBoard.setPosition("A|a|Q")        

        #Assert
        board = hiveBoard.getBoard()
        
        self.assertEqual(len(board), 3)
        for piece, position in board:
            if(piece.type == Creatues.QueenBee and piece.firstPlayer):
                self.assertEqual(position, Position(Coordinate(0,0)))
        
    def test_center_P1_QueenBee_PlacedFirst(self):
        #Arrange
        hiveBoard = HiveBoard()

        #Act
        hiveBoard.setPosition("A|Q|a")        

        #Assert
        board = hiveBoard.getBoard()
        
        self.assertEqual(len(board), 3)
        for piece, position in board:
            if(piece.type == Creatues.QueenBee and piece.firstPlayer):
                self.assertEqual(position, Position(Coordinate(0,0)))



if __name__ == "__main__":
    unittest.main()
