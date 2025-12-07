# Guess Code 2 V 1.0.0 ALPHA

# Add CONTINUE MENU
# Add channels for soundtracks

from pathlib import Path
from random import randint, shuffle, choice
from time import sleep
import shutil
import re
import sys
import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

from tqdm import tqdm
import colorama
import pyfiglet
import pygame

colorama.init()
pygame.init()
pygame.mixer.init()


class SystemPrompt:
    COLORS = [attr for attr in dir(colorama.Fore) if not attr.startswith("_")]

    def __init__(self):
        self.INPUT = self.communicate("<<< ", "LIGHTWHITE_EX")
        self.RULES = (self.communicate("Press ENTER to continue\n","LIGHTRED_EX"),
                      self.communicate(">>> Rules:","LIGHTRED_EX"),
                      self.communicate(">>> Find the number the computer guessed.","BLUE"),
                      self.communicate(">>> 1. Select a range (e.g. 5-200).","BLUE"),
                      self.communicate(">>> 2. Start guessing.","BLUE"),
                      self.communicate(">>> Your turn!","LIGHTRED_EX"))
        self.LVL_TYPES = {"COMMON": self.communicate("COMMON", "LIGHTBLUE_EX"),
                          "EPIC": self.communicate("EPIC", "LIGHTMAGENTA_EX"),
                          "LEGENDARY": self.communicate("LEGENDARY", "LIGHTYELLOW_EX")}

    @staticmethod
    def del_ascii(text: str):
        ansi_escape = re.compile(r"\x1B[@-_][0-?]*[ -/]*[@-~]")
        return ansi_escape.sub("", text)

    @staticmethod
    def resource_path(relative_path: str):
        base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    @staticmethod
    def communicate(text=None, color=None, is_error=False, is_bold=False, is_underlined=False):
        if text is None and color is None:
            return None
        elif is_error:
            text = f"ERROR: {text}"
            color = "LIGHTRED_EX"

        colored_text = getattr(colorama.Fore, color) + text + colorama.Style.RESET_ALL
        if is_bold:
            colored_text = colorama.Style.BRIGHT + colored_text
        if is_underlined:
            colored_text = "\033[4m" + colored_text + "\033[0m"
        return colored_text

    def get_ascii_text(self, text: str, color="LIGHTBLUE_EX", font="standard"):
        f = pyfiglet.Figlet(font=font)
        ascii_text = f.renderText(text)
        for line in ascii_text.splitlines():
            print(self.communicate(line, color, is_bold=True))
            sleep(0.25)

    def get_rules(self):
        for line in self.RULES:
            print(line, end="")
            input()


# system = SystemPrompt()
# system.get_ascii_text("GuessCode 2.0 V1.0.0 ALPHA")
