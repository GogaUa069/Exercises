import time
import random
import colorama
from abc import ABC, abstractmethod


class System:
    MAX_LIVES = 5

    def __init__(self):
        self.INPUT = self.communicate("<<< ", "LIGHTWHITE_EX")

    @staticmethod
    def communicate(text, color):
        return getattr(colorama.Fore, color) + text + colorama.Style.RESET_ALL


system = System()


class Player(ABC):
    def __init__(self, name):
        self.NAME = name.upper()
        self.LIVES = system.MAX_LIVES
        self.OPTION = None
        self.DOUBLE_MOVE = False

    @abstractmethod
    def move(self):
        ...

    @abstractmethod
    def reset(self):
        ...


class Human(Player):
    def move(self):
        ...

    def reset(self):
        ...


human = Human("human")


class Bot(Player):
    def move(self):
        ...

    def reset(self):
        ...


bot = Bot("dealer")


class Shotgun:
    ...


class Bullet:
    ...


class Item:
    def __init__(self, name, description, func, tpr=-1):
        self.NAME = name.upper()
        self.DESCR = description
        self.FUNC = func
        self.TIMES_PER_ROUND = tpr

    def __call__(self):
        self.FUNC()


cigarettes = Item("cigarettes", "Heals 1HP.", lambda player: player.LIVES + 1 if player.LIVES + 1 <= system.MAX_LIVES else 0)
beer = Item("beer", "Removes the next bullet.", lambda shotgun: shotgun.AMMO.pop(0))
loupe = Item("loupe", "Shows the next bullet type.", lambda shotgun: shotgun.AMMO[0].TYPE)
knife = Item("knife", "Sets double damage for the next shot.", lambda shotgun: shotgun.DAMAGE + 1)
manacles = Item("manacles", "Give second move.", lambda player: not player.DOUBLE_MOVE)
phone = Item("phone", "Gives one hint.", ...)
