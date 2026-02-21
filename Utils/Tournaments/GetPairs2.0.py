from colorama import Fore, Style
from random import sample
from prettytable import PrettyTable

border = PrettyTable()
headers = ("PARA", "OSOBA 1", "OSOBA 2", "OSOBA 3")
border.field_names = headers
border.align["PARA"] = "l"
border.align["OSOBA 1"] = "l"
border.align["OSOBA 2"] = "l"
border.align["OSOBA 3"] = "l"


class PairsGenerator:

    def __init__(self):
        self.amount = 0
        self.players = list()
        self.pairs = list()
        self.symbols = None

    @staticmethod
    def communicate(text, color):
        return getattr(Fore, color) + text + Style.RESET_ALL

    def set_players(self):
        print(self.communicate("- Wpisz uczestników: ", "LIGHTWHITE_EX"))
        for indx in range(self.amount):
            player = input(self.communicate(f"{indx+1}. ".rjust(4, " "), "LIGHTWHITE_EX"))
            self.players.append(player)
        self.symbols = "-" * max(len(header) for header in headers+tuple(self.players))
        print()

    def set_pairs(self):
        for indx in range(len(self.players)//2):
            p3 = self.symbols
            if len(self.players) == 3:
                p1, p2, p3 = sample(self.players, k=3)
            else:
                p1, p2 = sample(self.players, k=2)
            pair = (indx+1, p1, p2, p3)
            self.pairs.append(pair)
            self.players.remove(p1)
            self.players.remove(p2)

    def set_pairs_list(self):
        for pair in self.pairs:
            border.add_row(pair)

    def __call__(self):
        self.amount = int(input(self.communicate("- Wpisz liczbę osób: ", "LIGHTWHITE_EX")))
        self.set_players()
        self.set_pairs()
        self.set_pairs_list()
        print(border)


pairs_generator = PairsGenerator()
pairs_generator()
