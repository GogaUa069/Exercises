from random import randint
from colorama import Fore, Style


def communicate(text, color):
    return getattr(Fore, color) + text + Style.RESET_ALL


class Cell:
    def __init__(self, symbol, color=None):
        self.symbol = communicate(symbol, color) if color is not None else symbol


L_BORDER = Cell("|", "LIGHTGREEN_EX")
R_BORDER = Cell("|", "LIGHTRED_EX")
WATER = Cell("≈", "LIGHTBLUE_EX")
TREE = Cell("^", "LIGHTGREEN_EX")
FOG = Cell("*", "LIGHTBLACK_EX")
LAND = Cell(".", "WHITE")
ROAD = Cell("=")


class Border:

    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height
        self.BORDER = [[LAND for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]
        self.set_border()

    def get_border(self):
        print()
        for row in self.BORDER:
            print("".join([cell.symbol for cell in row]))

    def set_forest(self, trees=3000):
        for _ in range(trees):
            x = randint(2, self.WIDTH-3)
            y = randint(0, self.HEIGHT-1)
            self.BORDER[y][x] = TREE

    def set_rivers(self):
        for point in (4, 2, 1.334):
            x = int(self.WIDTH//point)
            for indx, _ in enumerate(self.BORDER):
                step = randint(-2, 2)
                length = randint(7, 10)
                for i in range(length):
                    self.BORDER[indx][x+step+i] = WATER

    def set_roads(self):
        for _ in range(5):
            while True:
                y1, y2 = randint(1, self.HEIGHT-2), randint(1, self.HEIGHT-2)
                if (ROAD not in (self.BORDER[y1-1][1], self.BORDER[y1][1], self.BORDER[y1+1][1])
                        and ROAD not in (self.BORDER[y2-1][-2], self.BORDER[y2][-2], self.BORDER[y2+1][-2])):
                    break
            self.BORDER[y1][1:6] = (ROAD, )*5
            self.BORDER[y2][-6:-1] = (ROAD, )*5

    def set_borders(self):
        for line in self.BORDER:
            line[0] = L_BORDER
            line[-1] = R_BORDER

    def set_border(self):
        self.set_forest(trees=5000)
        self.set_rivers()
        self.set_roads()
        self.set_borders()


border = Border(width=1002, height=100)
border.get_border()
