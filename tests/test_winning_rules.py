import unittest
from typing import List, Tuple, Optional
from parameterized import parameterized # type: ignore
from app.HivePiece import HivePiece
from app.GameResult import GameResult

from tests.HiveGameTestBuilder import HiveGameTestBuilder

param_list = [('a', 'a'), ('a', 'b'), ('b', 'b')]

class TestWinningRules(unittest.TestCase):

    def test_Game_can_continue_when_queens_not_surrounded(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1, 0,0).\
            Play(HivePiece.QueenBee_P2, -1,0).\
            Build()

        #Act
        gameResult = hiveGame.getGameState()

        #Assert
        self.assertEqual(gameResult, GameResult.Undecided)

    def test_Game_StartinPlayer_Losses_when_StartingPlayers_queen_is_surronded(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1,  0, 0).\
            Play(HivePiece.QueenBee_P2, -1, 0).\
            Play(HivePiece.Ant_0_P1,     1, 0).\
            Play(HivePiece.Ant_0_P2,    -2, 0).\
            Play(HivePiece.Ant_1_P1,     2, 0).\
            Play(HivePiece.Ant_1_P2,    -2,-1).\
            Play(HivePiece.Ant_1_P1,    -1,-1).\
            Play(HivePiece.Ant_2_P2,    -2, 1).\
            Play(HivePiece.Ant_0_P1,    -1, 1).\
            Build()

        #Act
        print(hiveGame.board.printBoard())
        gameResult = hiveGame.getGameState()

        #Assert
        self.assertEqual(gameResult, GameResult.FirstPlayerWon)

    def test_Game_StartinPlayer_Wins_when_opponents_queen_is_surronded(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1,  0, 0).\
            Play(HivePiece.QueenBee_P2, -1, 0).\
            Play(HivePiece.Ant_0_P1,     1, 0).\
            Play(HivePiece.Ant_0_P2,    -2, 0).\
            Play(HivePiece.Ant_1_P1,     0,-1).\
            Play(HivePiece.Ant_0_P2,    -1,-1).\
            Play(HivePiece.Ant_2_P1,     0, 1).\
            Play(HivePiece.Ant_1_P2,    -2, 0).\
            Play(HivePiece.Spider_0_P1,  2, 0).\
            Play(HivePiece.Ant_1_P2,    -1, 1).\
            Build()

        #Act
        print(hiveGame.board.printBoard())
        gameResult = hiveGame.getGameState()

        #Assert
        self.assertEqual(gameResult, GameResult.SecondPlayerWon)


if __name__ == "__main__":
    unittest.main()
