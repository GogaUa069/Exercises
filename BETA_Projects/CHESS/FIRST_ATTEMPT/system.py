from string import ascii_uppercase as letters
from copy import copy
from colorama import Fore, Style


def communicate(text, color):
    return getattr(Fore, color) + text + Style.RESET_ALL
