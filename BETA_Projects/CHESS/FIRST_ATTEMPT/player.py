from pieces import *

set_pieces = lambda piece, coords: [piece(coord) for coord in coords]

pawns = set_pieces(Pawn, (*(f"{letters[i]}{2}" for i in range(8)), *(f"{letters[i]}{7}" for i in range(8))))
knights = set_pieces(Knight, ("b1", "g1", "b8", "g8"))
bishops = set_pieces(Bishop, ("c1", "f1", "c8", "f8"))
rooks = set_pieces(Rook, ("a1", "h1", "a8", "h8"))
queens = set_pieces(Queen, ("d1", "d8"))
kings = set_pieces(King, ("e1", "e8"))

pieces = {
    "white": [*pawns[:8], *knights[:2], *bishops[:2], *rooks[:2], queens[0], kings[0]],
    "black": [*pawns[8:], *knights[2:], *bishops[2:], *rooks[2:], queens[1], kings[1]]
}


class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.pieces = pieces[self.color]
        self.points = lambda: sum(piece.points for piece in self.pieces)
        self.__set_piece_color()

    def __set_piece_color(self):
        for piece in self.pieces:
            piece.color = f"LIGHT{self.color.upper()}_EX"

    def __repr__(self):
        return (f"color: {self.color}\n"
                f"points: {self.points()}\n"
                f"pieces: {self.pieces}")


player1 = Player(name="GUEST1", color="white")
player2 = Player(name="GUEST2", color="black")
