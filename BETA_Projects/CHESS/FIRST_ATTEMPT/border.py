from player import *


class Cell:
    def __init__(self):
        self.color = None
        self.piece = None
        self.x = 0
        self.y = 0

    def __repr__(self):
        return f"color: {self.color}\npiece: {self.piece}\nX: {self.x}\nY: {self.y}"

    def __str__(self):
        return communicate("#", self.color) if self.piece is None else self.piece.__str__()


class Border:
    LENGTH = 8
    LETTERS = list(letters[:8])

    def __init__(self):
        self.border = [[Cell() for _ in range(self.LENGTH)] for _ in range(self.LENGTH)]
        self.__set_cells()

        self.get_letters = lambda: print("    ", " ".join(self.LETTERS))
        self.get_row = lambda row: " ".join(cell.__str__() for cell in row)
        self.get_row_indx = lambda indx: 8 - int(indx)
        self.get_let_indx = lambda let: self.LETTERS.index(let.upper())

        self.__set_pieces(player1)
        self.__set_pieces(player2)

    def __getitem__(self, item):
        let, num = item
        x, y = self.get_let_indx(let), self.get_row_indx(num)
        return self.border[y][x]

    def __setitem__(self, key, value):
        let, num = key
        x, y = self.get_let_indx(let), self.get_row_indx(num)
        self.border[y][x].piece = value

    def __delitem__(self, key):
        let, num = key
        x, y = self.get_let_indx(let), self.get_row_indx(num)
        self.border[y][x].piece = None

    def __set_cells(self):
        def validate_coords(_cell, _x, _y):
            match (_x % 2, _y % 2):
                case (0, 0) | (1, 1):
                    _cell.color = "LIGHTWHITE_EX"
                case _:
                    _cell.color = "LIGHTBLACK_EX"

        for y, row in enumerate(self.border):
            for x, cell in enumerate(row):
                validate_coords(cell, x, y)
                cell.x = x
                cell.y = y

    def __set_pieces(self, player):
        for piece in player.pieces:
            self[piece.coords] = piece

    def get_border(self):
        print()
        self.get_letters()
        print("   ", "_"*17)
        for indx, row in enumerate(self.border):
            print(self.get_row_indx(indx), " |", self.get_row(row), "| ", self.get_row_indx(indx))
        print("   ", "‾"*17)
        self.get_letters()


border = Border()
