from dataclasses import dataclass, field

FIGURE_SYMBOLS = {
    "pawn":   {"white": "♟", "black": "♙"},
    "knight": {"white": "♞", "black": "♘"},
    "bishop": {"white": "♝", "black": "♗"},
    "rook":   {"white": "♜", "black": "♖"},
    "queen":  {"white": "♛", "black": "♕"},
    "king":   {"white": "♚", "black": "♔"}
}


class Figure:
    def __init__(self, color, x="a", y=0):
        self.color = color
        self.x = x
        self.y = y


class Pawn(Figure):
    def __init__(self, color, x="x", y):
        super().__init__(color=color, x=x, y=y)



@dataclass
class Figure:
    color: str
    x: str = field(default="a", init=False)
    y: int = field(default=0, init=False)


@dataclass
class Pawn(Figure):
    name: str = field(default="pawn", init=False)
    amount: int = field(default=8, init=False)
    points: int = field(default=1, init=False)
    symbol: str = field(default=FIGURE_SYMBOLS[name][], init=False)


@dataclass
class Knight(Figure):
    name: str = field(default="knight", init=False)
    amount: int = field(default=2, init=False)
    points: int = field(default=3, init=False)


@dataclass
class Bishop(Figure):
    name: str = field(default="bishop", init=False)
    amount: int = field(default=2, init=False)
    points: int = field(default=3, init=False)


@dataclass
class Rook(Figure):
    name: str = field(default="rook", init=False)
    amount: int = field(default=2, init=False)
    points: int = field(default=5, init=False)


@dataclass
class Queen(Figure):
    name: str = field(default="queen", init=False)
    amount: int = field(default=1, init=False)
    points: int = field(default=9, init=False)


@dataclass
class King(Figure):
    name: str = field(default="king", init=False)
    amount: str = field(default=1, init=False)
    is_check: bool = field(default=False, init=False)
    is_mate: bool = field(default=False, init=False)


FIGURES = {
    Pawn:   {"white": {"figure": "♟", "num": 0}, "black": {"figure": "♙"}},
    Knight:   {"white": {"figure": "♞", "num": 0}, "black": "♘"},
    Bishop:   {"white": {"figure": "♝", "num": 0}, "black": "♗"},
    Rook:   {"white": {"figure": "♜", "num": 0}, "black": "♙"},
    Queen:   {"white": {"figure": "♛", "num": 0}, "black": "♙"},
    King:   {"white": {"figure": "♚", "num": 0}, "black": "♙"},
}


class Team:
    def __init__(self, color: str):
        self.color = color
        self.figures = list()
        self.points = 0
        self.set_figures()

    def set_figures(self):
        for figure in FIGURE_SYMBOLS.keys():
            for _ in range(figure.amount):
                f = figure(color=self.color, symbol=FIGURE_SYMBOLS[figure][self.color])
                self.figures.append(f)


white = Team(color="white")
black = Team(color="black")

for figure in white.figures:
    print(figure)
