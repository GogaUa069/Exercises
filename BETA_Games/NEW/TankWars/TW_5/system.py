from colorama import Fore, Style


def communicate(text, color=None):
    return getattr(Fore, color) + text + Style.RESET_ALL if color else text


def set_color(color, is_light=False):
    match is_light:
        case True:
            return f"LIGHT{color.upper()}_EX"
        case _:
            return color.upper()


def get_attrs(attrs, one_row=False):
    match one_row:
        case True:
            print(", ".join(communicate(str(attr), "LIGHTWHITE_EX") for attr in attrs))
        case _:
            for indx, attr in enumerate(attrs, 1):
                print(communicate(f"{indx}. {attr}", "LIGHTWHITE_EX"))


class Nation:
    def __init__(self, name, color):
        self.name = name
        self.color = color


nation1 = Nation(name="Folk Valley", color="blue")
nation2 = Nation(name="Tuff Valley", color="red")


class Player:
    def __init__(self, nation):
        self.nation = nation
        self.units = dict()


player1 = Player(nation=nation1)
player2 = Player(nation=nation2)
