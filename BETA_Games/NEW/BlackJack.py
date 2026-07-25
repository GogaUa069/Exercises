from random import shuffle
from colorama import Fore, Style


def communicate(text, color="LIGHTWHITE_EX"):
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

    def __str__(self):
        return communicate(f"{self.name}'s hand: {", ".join(self.hand)}")


player1 = Player("YOU")
player2 = Player("PLAYER2")
player3 = Player("PLAYER3")


class Dealer:
    def __init__(self, name="DEALER"):
        self.name = name
        self.hand = {"opened": list(), "closed": None}

    def set_hand(self, deck):
        hand = list()
        for _ in range(2):
            hand.append(deck[0])
            del deck[0]
        self.hand["opened"].append(hand[0])
        self.hand["closed"] = hand[1]

        return deck

    def __repr__(self):
        return (f"name: {self.name}\n"
                f"hand: {self.hand}\n")

    def __str__(self):
        return communicate(f"{self.name}'s hand: {", ".join(self.hand["opened"])}, X")


dealer = Dealer()


class Game:
    symbols = ("♥", "♦", "♣", "♠")
    values = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
    bets = {25: 20, 50: 10, 100: 5, 500: 3, 1000: 2}

    def __init__(self):
        self.deck = [value+symbol for value in self.values for symbol in self.symbols]*6
        for _ in range(5):
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
        self.deck = dealer.set_hand(self.deck)

    def __str__(self):
        return (f"{dealer.__str__()}\n"
                f"{player1.__str__()}\n"
                f"{player2.__str__()}\n"
                f"{player3.__str__()}\n")

    def __call__(self):
        self.set_hands()
        print(self)


round1 = Round()
round1()
