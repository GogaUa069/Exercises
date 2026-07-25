from border import *


class Player:
    SOLDIERS = 100000

    def __init__(self):
        self.money = 1000000
        self.income = 250000
        self.energy = 1000


class Soldier:
    def __init__(self, rank):
        
