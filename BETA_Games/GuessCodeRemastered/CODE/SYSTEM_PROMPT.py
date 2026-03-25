import random
import time
import shutil
import sys
import os
import re

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import colorama
import tqdm
import pyfiglet
import pygame
import yaml

pygame.init()


class SystemPrompt:
    def __init__(self):
        self.INPUT = self.communicate("<<< ", "LIGHTWHITE_EX")
        self.RULES = (self.communicate("Press ENTER to continue.\n", "LIGHTRED_EX"),
                      self.communicate("Rules:", "LIGHTRED_EX"),
                      self.communicate("Task: Find the number the computer guessed with the specified conditions.","LIGHTBLUE_EX"),
                      self.communicate("1. Choose a difficulty level. Each with its own conditions.", "LIGHTBLUE_EX"),
                      self.communicate("2. Set the range in which you will search for the number", "LIGHTBLUE_EX"),
                      self.communicate("3. Start guessing.", "LIGHTBLUE_EX"),
                      self.communicate("Your turn!", "LIGHTRED_EX"))

    @staticmethod
    def del_color(text):
        ansi_escape = re.compile(r"\x1B[@-_][0-?]*[ -/]*[@-~]")
        return ansi_escape.sub("", text)

    @staticmethod
    def resource_path(relative_path):
        base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    @staticmethod
    def communicate(text, color):
        return getattr(colorama.Fore, color) + text + colorama.Style.RESET_ALL

    def quit_game(self):
        print(self.communicate("Goodbye! :)", "LIGHTCYAN_EX"))
        time.sleep(0.5)

    def get_rules(self):
        for rule in self.RULES:
            print(rule, end="")
            input()

    def get_text_by_char(self, text, color):
        for char in text:
            print(self.communicate(char, color), end="")
            time.sleep(0.21)

    def get_ascii_text(self, text, color="LIGHTBLUE_EX", font="standard"):
        f = pyfiglet.Figlet(font=font)
        ascii_text = f.renderText(text)
        for line in ascii_text.splitlines():
            print(self.communicate(line, color))
            time.sleep(0.25)


system = SystemPrompt()
