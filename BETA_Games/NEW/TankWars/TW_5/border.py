from random import randint
from system import *


class Cell:
    def __init__(self, name="land", symbol=".", color="white"):
        self.name = name
        self.symbol = symbol
        self.color = color
        self.nation = None
        self.unit = None

    def get_nation(self):
        return self.nation if self.nation is None else self.nation.name

    def get_symbol(self):
        return communicate(self.symbol, set_color(self.color)) if self.unit is None else self.unit.get_symbol()

    def __setattr__(self, key, value):
        if key == "unit" and value is not None:
            self.nation = value.nation
        if key == "nation" and value is not None:
            self.color = value.color
        object.__setattr__(self, key, value)

    def __repr__(self):
        return (f"cell __repr__:\n"
                f"- name:   {self.name}\n"
                f"- symbol: {self.symbol}\n"
                f"- nation: {self.get_nation()}\n"
                f"- unit:   {self.unit is not None}") if self.unit is None else self.unit.__repr__()

    def __str__(self):
        return communicate(f"CELL INFO:\n"
                           f"- name:   {self.name}\n"
                           f"- nation: {self.get_nation()}") if self.unit is None else self.unit.__str__()


class Border:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.border = [[Cell() for _ in range(self.width)] for _ in range(self.height)]
        self.__set_territories()
        self.__set_forest()

    def __set_territories(self):
        for row in self.border:
            for cell in row[:self.width//2+1]:
                cell.nation = player1.nation
            for cell in row[self.width//2:]:
                cell.nation = player2.nation

    def __set_forest(self):
        trees = self.width * self.height // 10
        for _ in range(trees):
            while True:
                x = randint(1, self.width-1)
                y = randint(1, self.height-1)
                if self.border[y][x].name == "land":
                    break
            self.border[y][x] = Cell(name="tree", symbol="^", color=set_color("green"))

    def get_border(self, player):
        for row in self.border:
            for cell in row:
                print(cell.get_symbol() if cell.nation in (None, player.nation) else communicate("#", "WHITE"), end="")
            print()

    def __getitem__(self, item):
        x, y = item
        return self.border[y-1][x-1]

    def __setitem__(self, key, value):
        x, y = key
        self.border[y-1][x-1].unit = value

    def __delitem__(self, key):
        x, y = key
        self.border[y-1][x-1].unit = None


border = Border(width=100, height=25)
