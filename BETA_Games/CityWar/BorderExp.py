from colorama import Fore, Style
from random import randint


class Border:
    WIDTH = 175
    HEIGHT = 25
    fog = Fore.LIGHTBLACK_EX + "*" + Style.RESET_ALL

    def __init__(self):
        self.border = [[Fore.WHITE + "." + Style.RESET_ALL for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]
        self.fog_border = None
        self()

    def get_border(self):
        for line in self.border:
            print("".join(line))
        print()

    def set_forest(self):
        for _ in range(150):
            x = randint(0, self.WIDTH-1)
            y = randint(0, self.HEIGHT-1)
            self.border[y][x] = Fore.LIGHTGREEN_EX + "^" + Style.RESET_ALL

    def set_river(self):
        half_x = self.WIDTH//2
        for indx, line in enumerate(self.border):
            step = randint(-2, 2)
            length = randint(5, 7)
            for i in range(length):
                self.border[indx][half_x+step+i] = Fore.LIGHTBLUE_EX + "=" + Style.RESET_ALL

    def set_roads(self):
        y1, y2 = randint(1, self.HEIGHT-2), randint(1, self.HEIGHT-2)
        self.border[y1][1:6] = ("=", )*5
        self.border[y2][-6:-1] = ("=", )*5

    def set_lines(self):
        for line in self.border:
            line[0] = Fore.LIGHTGREEN_EX + "|" + Style.RESET_ALL
            line[-1] = Fore.LIGHTRED_EX + "|" + Style.RESET_ALL

    def set_fog_border(self):
        self.fog_border = [row[:] for row in self.border]
        half_x = self.WIDTH//2
        for line in self.fog_border:
            line[half_x:] = [self.fog]*(self.WIDTH-half_x)

    def get_fog_border(self):
        for line in self.fog_border:
            print("".join(line))
        print()

    def set_drone_position(self):
        x = int(input("X: "))
        y = int(input("Y: "))
        self.fog_border[y][x] = self.border[y][x]

    def __call__(self, *args, **kwargs):
        self.set_forest()
        self.set_river()
        self.set_roads()
        self.set_lines()
        self.set_fog_border()


border1 = Border()
