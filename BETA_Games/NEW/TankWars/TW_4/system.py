from colorama import Fore, Style

colors = {"LIGHTBLUE_EX": "blue",
          "LIGHTRED_EX": "red"}


def communicate(text: str, color : str=None):
    return getattr(Fore, color) + text + Style.RESET_ALL if color is not None else text


def get_attrs(attrs, one_row=False):
    if one_row:
        print(", ".join(communicate(str(attr), "LIGHTWHITE_EX") for attr in attrs))
    else:
        for indx, attr in enumerate(attrs, 1):
            print(communicate(f"{indx}. {attr}", "LIGHTWHITE_EX"))


class Nation:
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color


nation1 = Nation(name="Folk Valley", color="LIGHTBLUE_EX")
nation2 = Nation(name="Tuff Valley", color="LIGHTRED_EX")


class Player:
    def __init__(self, nation: Nation):
        self.nation = nation
        self.units = dict()


player1 = Player(nation=nation1)
player2 = Player(nation=nation2)
