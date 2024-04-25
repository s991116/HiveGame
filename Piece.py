from typing import Dict
from dataclasses import dataclass
from Creatues import Creatues

@dataclass
class Piece:
    firstPlayer: bool
    type: Creatues
    index: int