from random import randint, choice
from time import sleep, time
import shutil
import sys
import os
import re

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

from colorama import Fore, Style
from tqdm import tqdm
import pyfiglet
import pygame

pygame.init()


class System:
    COLORS = [color for color in dir(Fore) if not color.startswith("_") and color != "BLACK"]

    def __init__(self):
        self.INPUT = self.communicate("<<< ", "LIGHTWHITE_EX")
        self.RULES = (self.communicate("Press ENTER to continue.\n", "LIGHTRED_EX"),
                      self.communicate("Rules:", "LIGHTRED_EX"),
                      self.communicate("Task: Find the number the computer guessed with the specified conditions.", "LIGHTBLUE_EX"),
                      self.communicate("1. Choose a difficulty level. each with its own conditions.", "LIGHTBLUE_EX"),
                      self.communicate("2. Set the range in which you will search for the number", "LIGHTBLUE_EX"),
                      self.communicate("3. Start guessing.", "LIGHTBLUE_EX"),
                      self.communicate("Your turn!", "LIGHTRED_EX"))
        self.LVL_TYPES = {"COMMON": self.communicate("COMMON", "LIGHTBLUE_EX"),
                          "EPIC": self.communicate("EPIC", "LIGHTMAGENTA_EX"),
                          "LEGENDARY": self.communicate("LEGENDARY", "LIGHTYELLOW_EX")}

    @staticmethod
    def del_color(text):
        ansi_escape = re.compile(r"\x1B[@-_][0-?]*[ -/]*[@-~]")
        return ansi_escape.sub("", text)

    @staticmethod
    def resource_path(relative_path):
        base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    @staticmethod
    def communicate(text=None, color=None):
        if text is not None and color is not None:
            text = getattr(Fore, color) + text + Style.RESET_ALL
        return text

    def quit_game(self):
        print(self.communicate("Goodbye! :)", "LIGHTCYAN_EX"))
        sleep(0.5)

    def get_rules(self):
        for rule in self.RULES:
            print(rule, end="")
            input()

    def get_text_by_let(self, text):
        for char in text:
            print(self.communicate(char, "LIGHTWHITE_EX"), end="")
            sleep(0.21)

    def set_ascii_text(self, text, color="LIGHTBLUE_EX", font="standard"):
        f = pyfiglet.Figlet(font=font)
        ascii_text = f.renderText(text)
        for line in ascii_text.splitlines():
            print(self.communicate(line, color))
            sleep(0.25)


system = System()
