from abc import ABC, abstractmethod
from random import randint, choice, choices
from time import sleep
import os
from colorama import Fore, Style

version = "v3.1.2"


class System:
    __instance = None

    MAX_BULLETS = 6
    MAX_ENERGY = 6
    MAX_LIVES = 3

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        raise RuntimeError("Singleton instance already exists.")

    def __init__(self):
        self.pass_func = lambda: None

        self.INPUT = self.communicate("<<< ", "LIGHTWHITE_EX")
        self.TUTORIAL = (self.communicate("[ENTER] to continue", "LIGHTRED_EX"),
                         self.communicate("\nTutorial:", "LIGHTCYAN_EX"),
                         self.communicate("\n1.1 You have 4 options to choose: 'shot', 'load', 'block' and 'deflect'.", "LIGHTCYAN_EX"),
                         self.communicate("1.2 Shot (0 energy) - You shot at your enemy. If you both select shot, nothing will happen.", "LIGHTCYAN_EX"),
                         self.communicate("1.3 Load (0 energy) - You add 1 bullet. (MAX 6)", "LIGHTCYAN_EX"),
                         self.communicate("1.4 Block (2 energy) - You block one enemy bullet. (disables after move.)", "LIGHTCYAN_EX"),
                         self.communicate("1.5 Deflect (3 energy) - Enemy bullet deflects and hurts him. (disables after move.)", "LIGHTCYAN_EX"),
                         self.communicate("\n2.1 Tip #1: Use 'load' as a first move, your opponent does not have bullets.", "LIGHTCYAN_EX"),
                         self.communicate("\nI think you are ready. Next tips will be in the future.", "LIGHTCYAN_EX"))

    @staticmethod
    def communicate(text: str, color: str) -> str:
        return getattr(Fore, color) + text + Style.RESET_ALL

    @staticmethod
    def clear_console():
        os.system("cls")

    def coming_soon(self):
        print(self.communicate("Coming soon...", "LIGHTWHITE_EX"))
        input()

    def error(self, text: str):
        print(self.communicate(f"ERROR: {text}", "LIGHTRED_EX"))

    def get_tutorial(self):
        for row in self.TUTORIAL:
            print(row, end="")
            input()


system = System()


class GUIOption:
    def __init__(self, name: str, func: ()):
        self.NAME = name.upper()
        self.FUNC = func

    def __call__(self):
        self.FUNC()


class Menu:
    def __init__(self, header: str, options: tuple):
        self.HEADER = header.upper()
        self.OPTIONS = options

    def show_menu(self):
        system.clear_console()
        print(system.communicate(f"\n[ {self.HEADER} ] [{version}]", "LIGHTRED_EX"))
        for index, option in enumerate(self.OPTIONS, 1):
            print(system.communicate(f"{index}. {option.NAME}", "GREEN"))

    def __check_answer(self, answer):
        for index, option in enumerate(self.OPTIONS, 1):
            if answer in (option.NAME, str(index)):
                option()
                return
        # system.error("Select one of the options shown above!")

    def __call__(self):
        answer = None
        while answer not in (str(len(self.OPTIONS)), self.OPTIONS[-1].NAME):
            self.show_menu()
            answer = input(system.INPUT).upper()
            self.__check_answer(answer)
