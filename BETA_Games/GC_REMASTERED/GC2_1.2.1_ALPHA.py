# Guess Code 2 V 1.2.1 ALPHA

# Add CONTINUE MENU
# Add channels for soundtracks

from random import randint, choice
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

    def get_text_by_let(self, text):
        for char in text:
            sleep(0.21)
            print(self.communicate(char, "LIGHTWHITE_EX"), end="")

    def get_rules(self):
        for line in self.RULES:
            print(line, end="")
            input()


system = SystemPrompt()

main_soundtrack_channel = pygame.mixer.Channel(0)
secondary_soundtrack_channel = pygame.mixer.Channel(1)


class Soundtrack:
    def __init__(self, name: str, repeats=1):
        self.NAME = name
        self.REPEATS = repeats

    def __call__(self):
        pygame.mixer.music.load(f"Soundtracks/{self.NAME}")
        pygame.mixer.music.play(self.REPEATS)


intro_soundtrack = Soundtrack("IntroSoundtrack.wav")
credits_soundtrack = Soundtrack("CreditsSoundtrack.wav", -1)
jazz1 = Soundtrack("Jazz1.wav", -1)
jazz2 = Soundtrack("Jazz2.mp3", -1)
jazz3 = Soundtrack("Jazz3.wav", -1)


class SoundPrompt:
    YOU_WIN_SOUND = pygame.mixer.Sound("Sounds/YouWinSound.wav")
    YOU_LOST_SOUND = pygame.mixer.Sound("Sounds/YouLostSound.wav")
    ABLE_TO_PLAY = True

    def __call__(self):
        self.ABLE_TO_PLAY = not self.ABLE_TO_PLAY
        match self.ABLE_TO_PLAY:
            case True:
                self.YOU_WIN_SOUND.play()
            case False:
                self.YOU_LOST_SOUND.play()


toggle_sound = SoundPrompt()


class WinStreakController:
    ENCODING = "utf-8"
    RESOURCE_NAME = SAVE_NAME = "Utils/WIN_STREAK_FILE"

    def __init__(self):
        self.SAVE_PATH = os.path.join(os.getcwd(), self.SAVE_NAME)
        self._ensure_writable_copy()

    @staticmethod
    def _resource_path(relative_path):
        base_path = getattr(sys, "_MEIPASS", os.path.dirname(__file__))
        return os.path.join(base_path, relative_path)

    def _ensure_writable_copy(self):
        if not os.path.exists(self.SAVE_PATH):
            try:
                shutil.copyfile(self._resource_path(self.RESOURCE_NAME), self.SAVE_PATH)
            except Exception:
                with open(self.SAVE_PATH, "w", encoding=self.ENCODING) as file:
                    file.write("0")

    def get_win_streak(self, is_communicate=False):
        with open(self.SAVE_PATH, "r", encoding=self.ENCODING) as file:
            streak = file.read()
            if not is_communicate:
                return int(streak)
            else:
                return f"Your win streak: {streak}"

    def __call__(self, is_defeat=False):
        new_streak = 0 if is_defeat else self.get_win_streak() + 1
        with open(self.SAVE_PATH, "w", encoding=self.ENCODING) as file:
            file.write(str(new_streak))


win_streak_controller = WinStreakController()


class GameIntro:
    GitHub_URL = "https://github.com/GogaUa069"
    Instagram_URL = "https://www.instagram.com/gogaua096/"

    def get_my_accounts(self):
        print(system.communicate(f"{self.Instagram_URL} - Follow me on Instagram :)", "CYAN"))
        print(system.communicate(f"{self.GitHub_URL} - Check my GitHub\n", "CYAN"))

    @staticmethod
    def loading():
        with tqdm(total=100) as pbar:
            for i in range(100):
                color = choice([c for c in system.COLORS if c != "BLACK"])
                pbar.set_description_str(system.communicate("Loading", color))
                pbar.update(1)
                sleep(0.04)
        print()

    @staticmethod
    def show_game_banner(banner: str):
        sleep(0.5)
        print(system.communicate("Welcome to:", "CYAN", is_bold=True))
        sleep(1.5)
        system.get_ascii_text(banner)
        print(system.communicate("Made by GogaUa\n", "WHITE", is_bold=True))
        sleep(1)

    def __call__(self):
        intro_soundtrack()
        self.get_my_accounts()
        self.show_game_banner("Guess Code 2.0\n v 1.2.1 ALPHA")
        self.loading()


game_intro = GameIntro()


class Option:
    def __init__(self, name: str, func):
        self.NAME = name
        self.FUNC = func

    def __call__(self):
        self.FUNC()


class BorderOption:
    def __init__(self, lvl: str, name: str, lvl_type: str, descr: str):
        self.LVL = lvl
        self.NAME = name
        self.LVL_TYPE = lvl_type
        self.DESCR = descr
        self.DATA = [self.LVL, self.NAME, self.LVL_TYPE, self.DESCR]


basic_game_border = BorderOption("1", "BASIC", system.LVL_TYPES["COMMON"], "Infinite lives. Time-free mode.")
average_game_border = BorderOption("2", "AVERAGE", system.LVL_TYPES["COMMON"], "Finite lives. Time-free mode.")
advanced_game_border = BorderOption("3", "ADVANCED", system.LVL_TYPES["COMMON"], "Finite lives. Countdown active.")
wild_game_border = BorderOption("4", "WILD", system.LVL_TYPES["EPIC"], "Lives and time are randomized.")
custom_game_border = BorderOption("5", "CUSTOM", system.LVL_TYPES["EPIC"], "Lives and time are under your control.")
adventure_game_border = BorderOption("6", "ADVENTURE", system.LVL_TYPES["LEGENDARY"],
                                     "Beat AVERAGE, ADVANCED, and WILD levels in a single run and get a prize!")
leave_border = BorderOption("7",  "MAIN MENU", "---------", "Back to Main Menu")

level_tup = (basic_game_border, average_game_border, advanced_game_border,
             wild_game_border, custom_game_border, adventure_game_border, leave_border)


class MenuPattern:
    def __init__(self, header: str, options: tuple, border=None):
        self.HEADER = header
        self.OPTIONS = options
        self.BORDER = border

    def show_menu(self):
        match self.BORDER:
            case None:
                print(system.communicate(f"\n{self.HEADER}", "LIGHTRED_EX"))
                for indx, option in enumerate(self.OPTIONS):
                    print(system.communicate(f"{indx + 1}. {option.NAME}", "LIGHTBLUE_EX"))
            case _:
                self.BORDER()

    def check_answer(self, answer: str):
        for indx, option in enumerate(self.OPTIONS):
            if answer.upper() in (option.NAME, str(indx+1)):
                option()
            else:
                print(system.communicate("Select one of the options shown above!", is_error=True))

    def __call__(self):
        while True:
            self.show_menu()
            self.check_answer(input(system.INPUT))


class BorderPattern:
    HEADERS = ["LVL", "NAME", "TYPE", "DESCRIPTION"]

    def __init__(self, levels: tuple):
        self.LEVELS = levels
        self.LONGEST_LENGTH_LIST = list()
        self.DATA = [*self.HEADERS] + [lvl.DATA for lvl in self.LEVELS]
        self.set_the_longest_data_length()

    def set_the_longest_data_length(self):
        for items in zip(*self.DATA):
            the_longest_item = max(len(item) for item in items)
            self.LONGEST_LENGTH_LIST.append(the_longest_item)

    def __call__(self):
        for row in self.DATA:
            line = ""
            for indx, item in enumerate(row):
                line += "| " + item.ljust(self.LONGEST_LENGTH_LIST[indx]) + " "
            line += "|"
            print(line)


game_border = BorderPattern(level_tup)


class Credits:
    HEADER = "CREDITS:"

    def __init__(self, *args):
        self.CREDITS = list(args)

    def get_credits(self):
        for indx, credit in enumerate(self.CREDITS):
            text = f"{indx+1}. {credit}"
            system.get_text_by_let(text)
            print()
        sleep(1)
        print()

    @staticmethod
    def leave_credits():
        print(system.communicate("All audio was taken from freesound.org", "LIGHTWHITE_EX", is_underlined=True))
        input(system.communicate(">>> Press ENTER to leave", "LIGHTRED_EX"))
        pygame.mixer.music.stop()

    def __call__(self):
        credits_soundtrack()
        system.get_ascii_text(self.HEADER)
        self.get_credits()
        self.leave_credits()


credits_ = Credits("Egor Pavlenko - CEO")
