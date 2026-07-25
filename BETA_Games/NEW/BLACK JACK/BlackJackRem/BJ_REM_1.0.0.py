#  V 1.0.0 ALPHA

from random import choice, shuffle, randint
from time import sleep
import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

from colorama import Fore, Style
import pygame

pygame.init()


class SystemPrompt:

    @staticmethod
    def color_text(text, color):
        print(getattr(Fore, color) + text)


system = SystemPrompt()


class Data:
    __ex = 0

    MONOLOGUES = ["Well, well, well.", "Okay.", "Good!", "Hmm...", "Well done!", "Ahh!", "One more?"]
    SOUNDTRACK = r"Audio/ElectricJazz.wav"
    RULES = [system.color_text("Press ENTER to continue\n", "LIGHTRED_EX"),
             system.color_text("BlackJack rules:\n", "LIGHTRED_EX"),
             system.color_text("1. The deck contains 11 cards.", "LIGHTBLUE_EX"),
             system.color_text("2. The game lasts one round.", "LIGHTBLUE_EX"),
             system.color_text("3. The player whose total score is closest to 21, wins.", "LIGHTBLUE_EX"),
             system.color_text("4. Players who exceed 21 points lose te round.\n", "LIGHTBLUE_EX"),
             system.color_text("The round end when:", "LIGHTBLUE_EX"),
             system.color_text(),
             "b. A player exceeds 21 points.\n",
             Fore.RED + "Good luck!" + Style.RESET_ALL]

    def __new__(cls, *args, **kwargs):
        cls.__ex += 1
        return super().__new__(cls) if cls.__ex == 1 else None

    def __init__(self):
        self.DECK = [i for i in range(1, 12)]
        self.shuffle_deck()

    def play_soundtrack(self):
        pygame.mixer.music.load(self.SOUNDTRACK)
        pygame.mixer.music.play(-1)

    def shuffle_deck(self):
        for _ in range(randint(1, 10)):
            shuffle(self.DECK)

    def get_rules(self):
        for line in self.RULES:
            print(line, end="")
            input()

    @staticmethod
    def get_hands_info(player, dealer):
        border = Fore.LIGHTWHITE_EX + "_" + Style.RESET_ALL * 72
        info = [Fore.LIGHTRED_EX + ">>> Hands info:",
                Fore.LIGHTBLUE_EX + "DEALER"]


data = Data()
data.play_soundtrack()
data.get_rules()
