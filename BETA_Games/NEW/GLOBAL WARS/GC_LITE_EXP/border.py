from random import randint
from system import *


class Border:
    left_border = system.communicate("|", "LIGHTGREEN_EX")
    right_border = system.communicate("|", "LIGHTRED_EX")
    water = system.communicate("≈", "LIGHTBLUE_EX")
    tree = system.communicate("^", "LIGHTGREEN_EX")
    fog = system.communicate("*", "LIGHTBLACK_EX")
    space = system.communicate(".", "WHITE")
    road = "="

    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height
        self.BORDER = [[self.space for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]
        self.FOG_BORDER = None
        self()

    @staticmethod
    def get_border(b):
        for line in b:
            print("".join(line))

    def set_forest(self, trees=7000):
        for _ in range(trees):
            x = randint(2, self.WIDTH-3)
            y = randint(0, self.HEIGHT-1)
            self.BORDER[y][x] = self.tree

    def set_rivers(self):
        for point in (4, 2, 1.334):
            x = int(self.WIDTH//point)
            for indx, _ in enumerate(self.BORDER):
                step = randint(-2, 2)
                length = randint(7, 10)
                for i in range(length):
                    self.BORDER[indx][x+step+i] = self.water

    def set_roads(self):
        for _ in range(5):
            while True:
                y1, y2 = randint(1, self.HEIGHT-2), randint(1, self.HEIGHT-2)
                if ("=" not in (self.BORDER[y1-1][1], self.BORDER[y1][1], self.BORDER[y1+1][1])
                        and "=" not in (self.BORDER[y2-1][-2], self.BORDER[y2][-2], self.BORDER[y2+1][-2])):
                    break
            self.BORDER[y1][1:6] = ("=", )*5
            self.BORDER[y2][-6:-1] = ("=", )*5

    def set_borders(self):
        for line in self.BORDER:
            line[0] = self.left_border
            line[-1] = self.right_border

    def set_fog_border(self):
        self.FOG_BORDER = [row[:] for row in self.BORDER]
        half_x = int(self.WIDTH // 2)
        for line in self.FOG_BORDER:
            line[half_x:] = [self.fog] * (self.WIDTH - half_x)

    def __call__(self):
        self.set_forest()
        self.set_rivers()
        self.set_roads()
        self.set_borders()
        self.set_fog_border()


border = Border(1000, 100)
fog_border = lambda: border.get_border(border.FOG_BORDER)
