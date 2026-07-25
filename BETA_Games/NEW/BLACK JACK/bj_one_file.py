from colorama import Fore, Style
from random import shuffle


class Person:
    def __init__(self, name):
        self.name = name
        self.cards = list()
        self.points = 0


player = Person("you")
dealer = Person("dealer")


class Data:
    monologues = ("Well, well, well.", "Okay.", "Good!", "Hmm...", "Well done!", "Ahh!")
    max_points = 21

    def __init__(self):
        self.answers = dict()

    def check_answers(self):
        return all(pair in (("dealer", "stand"), ("you", "stand")) for pair in self.answers)

    def is_victory(self):
        answer = None

        match player, dealer:
            case x, y if x.points == y.points:
                answer = "draw"
            case x, y if x.points > y.points and x.points > 21:
                answer = y.name
            case x, y if y.points < x.points <= 21:
                answer = x.name
            case _, y:
                return y.name
        return

data = Data()


class Deck:
    def __init__(self):
        self.deck = list(range(1, 12))

    def shuffle_deck(self):
        shuffle(self.deck)

    def first_allocation(self, opponent):
        for _ in range(2):
            opponent.cards.append(self.deck[0])
            del self.deck[0]
