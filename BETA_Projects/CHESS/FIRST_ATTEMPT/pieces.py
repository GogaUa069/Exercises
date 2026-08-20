from system import *


class Piece:
    def __init__(self, name, symbol, points, coords):
        self.name = name
        self.symbol = symbol
        self.points = points
        self.coords = coords
        self.color = None

    def __str__(self):
        return communicate(self.symbol, self.color)


class Pawn(Piece):
    def __init__(self, coords):
        super().__init__(name="pawn", symbol="•", points=1, coords=coords)
        self.has_moved = False


class Knight(Piece):
    def __init__(self, coords):
        super().__init__(name="knight", symbol="?", points=3, coords=coords)


class Bishop(Piece):
    def __init__(self, coords):
        super().__init__(name="bishop", symbol="/", points=3, coords=coords)
        self.cell_color = "white" if self.coords in ("f1", "c2") else "black"


class Rook(Piece):
    def __init__(self, coords):
        super().__init__(name="rook", symbol="|", points=5, coords=coords)
        self.has_moved = False


class Queen(Piece):
    def __init__(self, coords):
        super().__init__(name="queen", symbol="*", points=9, coords=coords)


class King(Piece):
    def __init__(self, coords):
        super().__init__(name="king", symbol="@", points=0, coords=coords)
        self.has_moved = False
        self.is_check = False
        self.is_mate = False
