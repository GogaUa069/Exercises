from random import randint
from system import *


class Cell:
    def __init__(self, name="land", symbol=".", color="WHITE"):
        self.name = name
        self.symbol = symbol
        self.color = color
        self.nation = None
        self.unit = None

    def get_symbol(self):
        return communicate(self.symbol, self.color)

    def __setattr__(self, key, value):
        if key == "unit" and value is not None:
            self.nation = value.nation
        if key == "nation" and value is not None:
            self.color = value.color
        object.__setattr__(self, key, value)

    def __repr__(self):
        return (f"__repr__:\n"
                f"name: {self.name}\n"
                f"symbol: {self.symbol}\n"
                f"nation: {self.nation if self.nation is None else self.nation.name}\n"
                f"unit: {self.unit is not None}")

    def __str__(self):
        return communicate(f"CELL INFO:\n"
                f"- name: {self.name}\n"
                f"- nation: {self.nation if self.nation is None else self.nation.name}", "LIGHTWHITE_EX") if self.unit is None else self.unit.__str__()


class Border:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.border = [[Cell() for _ in range(self.width)] for _ in range(self.height)]
        self.set_territories()
        self.set_forest()

    def __getitem__(self, item):  # ONLY FOR UNITS!
        x, y = item
        return self.border[y-1][x-1]

    def __setitem__(self, key, value):  # ONLY FOR UNITS!
        x, y = key
        self.border[y-1][x-1].unit = value

    def __delitem__(self, key):  # ONLY FOR UNITS!
        x, y = key
        self.border[y-1][x-1].unit = None

    def set_forest(self):
        trees = self.width * self.height // 10
        for _ in range(trees):
            while True:
                x = randint(0, self.width - 1)
                y = randint(0, self.height - 1)
                if self.border[y][x].name == "land":
                    break
            self.border[y][x] = Cell("tree", "^", "GREEN")

    def set_territories(self):
        for row in self.border:
            for cell in row[:self.width//2+1]:
                cell.nation = player1.nation
            for cell in row[self.width//2:]:
                cell.nation = player2.nation

    def get_border(self):
        for row in self.border:
            print("".join([cell.get_symbol() if cell.unit is None else cell.unit.get_symbol() for cell in row]))


border = Border(100, 25)
