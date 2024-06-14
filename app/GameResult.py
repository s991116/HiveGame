from __future__ import annotations

from enum import Enum

class GameResult(Enum):
    FirstPlayerWon = "First Player won"
    SecondPlayerWon = "Second Player won"
    Tie = "Tie"
    Undecided = "Undecided"