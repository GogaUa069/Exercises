from SYSTEM import *
from random import randint


class Border:
    water = system.communicate("≈", "LIGHTBLUE_EX")
    tree = system.communicate("^", "LIGHTGREEN_EX")
    fog = system.communicate("*", "LIGHTBLACK_EX")
    land = system.communicate(".", "WHITE")
    road = system.communicate("=", "LIGHTWHITE_EX")
    border = "|"

    def __init__(self, width: int, height: int):
        self.WIDTH = width + 2
        self.HEIGHT = height
        self.BORDER = [[self.land for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]
        self.FOG_BORDER = None

    def __set_x_indexes(self, is_reversed=False):
        length = tuple(str(num) for num in range(1, self.WIDTH-1))
        spaces = (" ", )*6
        ones = tuple(num[0] for num in length)
        tens = tuple(num[1] if len(num) >= 2 else " " for num in length)
        hundreds = tuple(num[2] if len(num) >= 3 else " " for num in length)
        thousands = tuple(num[3] if len(num) >= 4 else " " for num in length)
        indexes = (thousands, hundreds, tens, ones)
        if is_reversed:
            indexes = indexes[::-1]
        for indx in indexes:
            print("".join(spaces + indx))

    def get_border(self, b):
        self.__set_x_indexes()
        for indx, row in enumerate(b, 1):
            print(f"{indx}".rjust(4, " "), "".join(row), indx)
        self.__set_x_indexes(True)
        print()

    def set_fog_border(self):
        self.FOG_BORDER = [row[:] for row in self.BORDER]
        half_x = self.WIDTH//2
        for row in self.FOG_BORDER:
            row[half_x:-1] = self.fog * (half_x-1)

    def set_forest(self):
        amount = int((self.WIDTH * self.HEIGHT) / 26.66)
        for _ in range(amount):
            x = randint(0, self.WIDTH-1)
            y = randint(0, self.HEIGHT-1)
            self.BORDER[y][x] = self.tree

    def __set_river_indexes(self):
        a = len(str(self.WIDTH))+1
        divisions = list()
        for num in range(2, a+1, 2):
            divisions.append(self.WIDTH//num)
        if len(divisions) != 1:
            divisions.append(sum(divisions))
        return sorted(divisions)

    def set_rivers(self):
        points = self.__set_river_indexes()
        for point in points:
            for indx in range(len(self.BORDER)):
                step = randint(-len(str(self.WIDTH))+1, len(str(self.WIDTH))//2)
                length = randint(int(self.WIDTH//100*0.7)+3, self.WIDTH//100+3)
                for i in range(length):
                    self.BORDER[indx][point+step+i] = self.water

    def set_roads(self):
        amount = int(self.HEIGHT*0.1)
        length = int(self.WIDTH*0.005)
        for _ in range(amount):
            while True:
                y1, y2 = randint(1, self.HEIGHT-2), randint(1, self.HEIGHT-2)
                if (self.road not in (self.BORDER[y1-1][1], self.BORDER[y1][1], self.BORDER[y1+1][1])
                        and self.road not in (self.BORDER[y2-1][-2], self.BORDER[y2][-2], self.BORDER[y2+1][-2])):
                    break
            self.BORDER[y1][1:6] = (self.road, )*length
            self.BORDER[y2][-6:-1] = (self.road, )*length

    def set_borders(self):
        for row in self.BORDER:
            row[0] = system.communicate(self.border, "LIGHTGREEN_EX")
            row[-1] = system.communicate(self.border, "LIGHTRED_EX")

    def __call__(self):
        self.set_forest()
        self.set_rivers()
        self.set_roads()
        self.set_borders()
        self.set_fog_border()
        self.get_border(self.FOG_BORDER)


border = Border(1000, 100)
fog_border = lambda: border.get_border(border.FOG_BORDER)
