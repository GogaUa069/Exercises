from colorama import Fore, Style


def communicate(text: str, color : str=None):
    return getattr(Fore, color) + text + Style.RESET_ALL if color is not None else text


def get_attrs(attrs):
    for indx, attr in enumerate(attrs, 1):
        print(communicate(f"{indx}. {attr}", "LIGHTWHITE_EX"))


class Nation:
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color


vanguard_nation = Nation(name="vanguard", color="BLUE")
bulwark_nation = Nation(name="bulwark", color="RED")


class Player:
    def __init__(self, nation: Nation):
        self.nation = nation
        self.units = dict()


player1 = Player(nation=vanguard_nation)
player2 = Player(nation=bulwark_nation)
