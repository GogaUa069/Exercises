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
        return communicate(self.symbol, set_color(self.color))

    def __setattr__(self, key, value):
        if key == "unit" and value is not None:
            self.nation = value.nation
        if key == "nation" and value is not None:
            self.color = value.color
        object.__setattr__(self, key, value)

    def __repr__(self):
        return (f"cell __repr__:\n"
                f"- name: {self.name}\n"
                f"- symbol: {self.symbol}\n"
                f"- nation: {self.get_nation()}\n"
                f"- unit: {self.unit is not None}")

    def __str__(self):
        return communicate(f"CELL INFO:\n"
                           f"- name: {self.name}\n"
                           f"- nation: {self.get_nation()}")


class Border:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.border = [[Cell() for _ in range(self.width)] for _ in range(self.height)]
        ...

    def __getitem__(self, item):
        ...

    def __setitem__(self, key, value):
        ...

    def __delitem__(self, key):
        ...
