from random import shuffle
from colorama import Fore, Style


def communicate(text, color):
    return getattr(Fore, color) + text + Style.RESET_ALL


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = list()
        self.money = 5000

    def __repr__(self):
        return (f"name: {self.name}\n"
                f"hand: {self.hand}\n"
                f"money: {self.money}\n")


player1 = Player("YOU")
player2 = Player("PLAYER2")
player3 = Player("PLAYER3")


class Dealer:
    def __init__(self, name="DEALER"):
        self.name = name
        self.hand = {"opened": list(), "closed": None}


dealer = Dealer()


class Game:
    symbols = ("♥", "♦", "♣", "♠")
    values = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
    bets = {25: 20, 50: 10, 100: 5, 500: 3, 1000: 2}

    def __init__(self):
        self.deck = [value+symbol for value in self.values for symbol in self.symbols]*6
        shuffle(self.deck)


class Round(Game):
    def set_hand(self, player):
        for _ in range(2):
            player.hand.append(self.deck[0])
            del self.deck[0]

    def set_hands(self):
        self.set_hand(player1)
        self.set_hand(player2)
        self.set_hand(player3)

    def __call__(self):
        self.set_hands()


round1 = Round()
print(player1)
print(player2)
print(player3)
