from Coordinate import Coordinate
class Position:
    
    def __init__(self, coordinate: Coordinate) -> None:
        self.coordinate = coordinate

    def offset(self, offset: Coordinate) -> None:
        self.coordinate.x -= offset.x
        self.coordinate.x -= offset.y
        pass


    def __eq__(self, other): # type: ignore
    
        if isinstance(other, Position):
            return self.coordinate == other.coordinate
        return False