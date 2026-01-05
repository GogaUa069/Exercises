from colorama import Fore, Style
from random import randint

WIDTH = 175
HEIGHT = 25

border = [[Fore.WHITE + "." + Style.RESET_ALL for _ in range(WIDTH)] for _ in range(HEIGHT)]


def get_border():
    for line in border:
        print("".join(line))


def set_forest():
    for _ in range(150):
        x = randint(0, WIDTH-1)
        y = randint(0, HEIGHT-1)
        border[y][x] = Fore.LIGHTGREEN_EX + "^" + Style.RESET_ALL


def set_river():
    half_board = WIDTH//2
    for indx, line in enumerate(border):
        step = randint(-1, 1)
        length = randint(3, 7)
        for i in range(length):
            border[indx][half_board+step+i] = Fore.LIGHTBLUE_EX + "=" + Style.RESET_ALL


def set_roads():
    y1, y2 = randint(1, HEIGHT-2), randint(1, HEIGHT-2)
    border[y1][1:6] = ("=", )*5
    border[y2][-6:-1] = ("=", )*5


def set_lines():
    for line in border:
        line[0] = Fore.LIGHTGREEN_EX + "|" + Style.RESET_ALL
        line[-1] = Fore.LIGHTRED_EX + "|" + Style.RESET_ALL


set_forest()
set_river()
set_roads()
set_lines()
get_border()
