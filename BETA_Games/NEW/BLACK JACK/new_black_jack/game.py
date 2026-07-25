from system_configuration import *
from random import shuffle


class Deck:
    def __init__(self):
        self.deck = list(range(1, 12))

    def shuffle_deck(self):
        shuffle(self.deck)

    def first_allocation(self):
        ...
