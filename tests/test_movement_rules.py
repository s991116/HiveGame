import unittest
from typing import List, Tuple, Optional
from parameterized import parameterized # type: ignore
from app.HiveBoard import HiveBoard
from app.BoardPiece import BoardPiece
from app.Species import Species
from app.Coordinate import Coordinate
from app.Directions import Direction
from app.HiveRulesMove import HiveRulesMove
from app.HivePiece import HivePiece
from tests.HiveGameTestBuilder import HiveGameTestBuilder
from app.BoardPieceBuilder import BoardPieceBuilder
from app.PieceBuilder import PieceBuilder

param_list = [('a', 'a'), ('a', 'b'), ('b', 'b')]

class TestMovmentRules(unittest.TestCase):

    def test_movement_not_possible_if_P1_Queen_is_not_placed(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.Ant_0_P1, 0,0).\
            Play(HivePiece.QueenBee_P2, -1,0).\
            Build()

        #Act
        movementMoves = hiveGame.rules.getMovementMoves()

        #Assert
        self.assertEqual(len(movementMoves), 0)

    def test_movement_not_possible_if_P2_Queen_is_not_placed(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1, 0,0).\
            Play(HivePiece.Ant_0_P2,-1,0).\
            Play(HivePiece.Ant_0_P1, 1,0).\
            Build()

        #Act
        movementMoves = hiveGame.rules.getMovementMoves()

        #Assert
        self.assertEqual(len(movementMoves), 0)

    @parameterized.expand([ # type: ignore
        ([True,  False, False, False, False, False], False),
        ([True,  False, True,  False, False, False], True),
        ([True,  False, True,  False, False, True ], True),
        ([True,  False, True,  False, True,  False], False),
        ([False, True,  False, True,  False, True ], False),
        ([True,  False, True,  False, False, True ], True),
        ([False, False, True,  True,  False, False], False),
        ([True,  False, False, False, False, True ], False),
        ([False, True,  False, True,  False, False], True),
        ([True, False,  True, True,  False, False], True),
    ])

    def test_detectBridgingCombinations(self, neighbourPiecesPresent: List[bool], gapExpected: bool):
        #Arrange
        navigationCircle = [
            Direction.LEFT,
            Direction.UP_LEFT,
            Direction.UP_RIGHT,
            Direction.RIGHT,
            Direction.DOWN_RIGHT,
            Direction.DOWN_LEFT
        ]

        board = HiveBoard()
        centerPiece = BoardPieceBuilder().WithHivePiece(HivePiece.Grasshopper_0_P1, Coordinate(0,0)).Build()
        board.movePiece(centerPiece)

        for directionIndex in range(0,6):
            if(neighbourPiecesPresent[directionIndex]):
                neighbourCoordinate = board.navigate(navigationCircle[directionIndex], centerPiece.coordinate)
                boardPiece = BoardPieceBuilder().WithPiece(PieceBuilder().With(Species.Grasshopper, directionIndex, True).Build()).WithCoordinate(neighbourCoordinate).Build()
                board.movePiece(boardPiece)

        movementRules = HiveRulesMove(board)

        #Act
        pieces: Optional[Tuple[BoardPiece, BoardPiece]] = movementRules.getBridgingPieces(centerPiece)

        #Assert
        if(gapExpected):
            self.assertIsNotNone(pieces)
        else:
            self.assertIsNone(pieces)            

    def test_no_movement_when_queen_is_not_placed(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.Beetle_0_P1, 0,0).\
            Play(HivePiece.Beetle_0_P2,-1,0).\
            Play(HivePiece.Ant_0_P1, 0,1).\
            Play(HivePiece.Ant_0_P2,-2,0).\
            Play(HivePiece.Ant_1_P1, 1,0).\
            Play(HivePiece.Ant_1_P2, -3,0).\
            Build()

        print(hiveGame.board.printBoard())

        #Act
        moveablePieces = hiveGame.rules.moveablePieces()

        #Assert
        self.assertEqual(len(moveablePieces), 0)

    def test_movement_possible_for_all_moveable_pieces(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1, 0,0).\
            Play(HivePiece.QueenBee_P2,-1,0).\
            Play(HivePiece.Ant_0_P1, 0,1).\
            Play(HivePiece.Ant_0_P2,-2,0).\
            Play(HivePiece.Ant_1_P1, 1,0).\
            Play(HivePiece.Ant_1_P2, -3,0).\
            Build()

        #Act
        moveablePieces = hiveGame.rules.moveablePieces()

        #Assert
        self.assertEqual(len(moveablePieces), 2)

    def test_allpieces_in_loop_can_move(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1,      0, 0).\
            Play(HivePiece.QueenBee_P2,     -1, 0).\
            Play(HivePiece.Ant_0_P1,  1, 0).\
            Play(HivePiece.Ant_0_P2, -2, 0).\
            Play(HivePiece.Ant_1_P1,  1, 1).\
            Play(HivePiece.Ant_1_P2, -3, 0).\
            Play(HivePiece.Ant_2_P1,  1, 2).\
            Play(HivePiece.Ant_2_P2, -4,-1).\
            Play(HivePiece.Grasshopper_0_P1, 0, 2).\
            Play(HivePiece.Grasshopper_0_P2,-4,-2).\
            Play(HivePiece.Grasshopper_1_P1,-1, 1).\
            Play(HivePiece.Grasshopper_1_P2,-3,-2).\
            Build()

        #Act
        moveablePieces = hiveGame.rules.moveablePieces()

        #Assert
        self.assertEqual(len(moveablePieces), 6)

    def test_movement_should_remove_piece_from_starting_point_on_the_board(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1,      0, 0).\
            Play(HivePiece.QueenBee_P2,     -1, 0).\
            Play(HivePiece.Grasshopper_0_P1, 1, 0).\
            Play(HivePiece.Grasshopper_0_P2,-2, 0).\
            Build()

        startingPiecePlacement = BoardPieceBuilder().WithHivePiece(HivePiece.Grasshopper_0_P1, Coordinate(1,0)).Build()

        #Act
        hiveGame.playMove(BoardPieceBuilder().WithHivePiece(HivePiece.Grasshopper_0_P1, Coordinate(-3, 0)).Build())
        print(hiveGame.board.printBoard())
        
        #Assert
        board = hiveGame.getBoard()
        self.assertNotIn(startingPiecePlacement, board)


if __name__ == "__main__":
    unittest.main()
