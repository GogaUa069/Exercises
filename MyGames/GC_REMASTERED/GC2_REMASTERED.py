# Remastering version GC1 v 5.1.1.0-beta

# Add CONTINUE MENU

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

pygame.init()
colorama.init()


class SystemPrompt:
    COLORS = [attr for attr in dir(colorama.Fore) if not attr.startswith("_")]
    UNDERLINE = "\033[4m"
    RESET_UNDERLINE = "\033[0m"

    def __init__(self):
        self.INPUT = self.color_text("<<< ", "LIGHTWHITE_EX")
        self.RULES = (self.color_text(self.communicate_pattern("Press ENTER to continue\n"), "LIGHTRED_EX"),
                      self.color_text(self.communicate_pattern("Rules:"), "LIGHTRED_EX"),
                      self.color_text(self.communicate_pattern("Find the number the computer guessed."), "BLUE"),
                      self.color_text(self.communicate_pattern("1. Select a range (e.g. 5-200)."), "BLUE"),
                      self.color_text(self.communicate_pattern("2. Start guessing."), "BLUE"),
                      self.color_text(self.communicate_pattern("Your turn!"), "LIGHTRED_EX")
                      )
        self.LVL_COLORS = {"COMMON": self.color_text("COMMON", "LIGHTBLUE_EX"),
                           "EPIC": self.color_text("EPIC", "LIGHTMAGENTA_EX"),
                           "LEGENDARY": self.color_text("LEGENDARY", "LIGHTYELLOW_EX")
                           }

    def color_text(self, text: str, color: str, is_reset_all=True, is_bold=False, is_underlined=False):
        colored_text = getattr(colorama.Fore, color) + text
        if is_reset_all:
            colored_text = colored_text + colorama.Style.RESET_ALL
        if is_bold:
            colored_text = colorama.Style.BRIGHT + colored_text
        if is_underlined:
            colored_text = self.UNDERLINE + colored_text + self.RESET_UNDERLINE
        return colored_text

    def get_rules(self):
        for rule in self.RULES:
            print(self.communicate_pattern(rule, line_after=True), end="")

    @staticmethod
    def communicate_pattern(text, is_error=False, is_pass=False, line_before=False, line_after=False):
        if is_pass:
            return None
        if is_error:
            return f">>> Error: {text}"

        text = f">>> {text}"
        if line_before:
            text = f"\n{text}"
        if line_after:
            text = f"{text}\n"
        return text

    def error(self, text="Select one of the options shown above!"):
        print(self.color_text(self.communicate_pattern(text, is_error=True), "LIGHTRED_EX", is_bold=True))

    def communicate(self, text: str, color="LIGHTWHITE_EX", is_pass=False):
        return self.color_text(self.communicate_pattern(text, is_pass=is_pass), color, is_bold=True)

    @staticmethod
    def del_ascii(text):
        ansi_escape = re.compile(r"\x1B[@-_][0-?]*[ -/]*[@-~]")
        return ansi_escape.sub("", text)

    @staticmethod
    def resource_path(relative_path):
        base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    @staticmethod
    def get_ascii_text(text, font="standard"):
        f = pyfiglet.Figlet(font=font)
        ascii_text = f.renderText(text)
        return ascii_text

    @staticmethod
    def get_ascii_text_by_line(text, color="LIGHTBLUE_EX"):
        for line in text.splitlines():
            print(system.color_text(line, color, is_bold=True))
            sleep(0.25)


system = SystemPrompt()


class Soundtrack:
    def __init__(self, name, is_infinity=False):
        self.NAME = name
        self.IS_INFINITY = is_infinity

    def __call__(self):
        pygame.mixer.music.load(system.resource_path("Soundtracks/" + self.NAME))
        pygame.mixer.music.play(-1) if self.IS_INFINITY else pygame.mixer.music.play()


intro_soundtrack = Soundtrack("IntroSoundtrack.wav")
credits_soundtrack = Soundtrack("CreditsSoundtrack.wav", is_infinity=True)
jazz1 = Soundtrack("Jazz1.wav", is_infinity=True)
jazz2 = Soundtrack("Jazz2.mp3", is_infinity=True)
jazz3 = Soundtrack("Jazz3.wav", is_infinity=True)


class SoundPrompt:
    YOU_WIN_SOUND = pygame.mixer.Sound("Sounds/YouWinSound.wav")
    YOU_LOST_SOUND = pygame.mixer.Sound("Sounds/YouLostSound.wav")
    ABLE_TO_PLAY = True

    def __call__(self):
        self.ABLE_TO_PLAY = not self.ABLE_TO_PLAY
        if self.ABLE_TO_PLAY:
            self.YOU_WIN_SOUND.play()
        else:
            self.YOU_LOST_SOUND.play()


toggle_sound = SoundPrompt()


class WinStreakController:
    ENCODING = "utf-8"
    RESOURCE_NAME = SAVE_NAME = "WIN_STREAK_FILE"

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
                with open(self.SAVE_PATH, "w", encoding=self.ENCODING) as f:
                    f.write("0")

    def get_win_streak(self, is_communicate=False):
        with open(self.SAVE_PATH, "r", encoding=self.ENCODING) as file:
            streak = file.read()
            if not is_communicate:
                return int(streak)
            else:
                return f"You win streak: {streak}"

    def __call__(self, is_defeat=False):
        new_streak = 0 if is_defeat else self.get_win_streak() + 1
        with open(self.SAVE_PATH, "w", encoding=self.ENCODING) as file:
            file.write(str(new_streak))


win_streak_controller = WinStreakController()


class GameIntro:

    @staticmethod
    def get_my_accounts():
        print(system.communicate_pattern(
            system.color_text(
                "@GogaUa096 - Instagram\n@GogaUa069 - GitHub", "CYAN"), line_after=True))

    @staticmethod
    def game_loading():
        with tqdm(total=100) as pbar:
            for i in range(100):
                color = choice([c for c in system.COLORS if c != "BLACK"])
                pbar.set_description_str(system.color_text("Loading", color))
                pbar.update(1)
                sleep(0.03)
        print()

    @staticmethod
    def show_game_banner(banner: str):
        sleep(0.5)
        print(system.color_text("Welcome to:", "CYAN", is_bold=True))
        sleep(1.5)
        ascii_banner = system.get_ascii_text(banner)
        system.get_ascii_text_by_line(ascii_banner)
        print(system.color_text("Made by GogaUa\n", "WHITE", is_bold=True))
        sleep(1)

    def __call__(self):
        intro_soundtrack()
        self.get_my_accounts()
        self.show_game_banner("Guess Code 5.1.1.0 Remastered")
        self.game_loading()


game_intro = GameIntro()


class MenuPattern:
    def __init__(self, header: str, options: tuple, border=None):
        self.HEADER = header
        self.OPTIONS = options
        self.BORDER = border

    def show_menu(self):
        if self.BORDER is None:
            print(system.color_text(system.communicate_pattern(self.HEADER, line_before=True), "LIGHTRED_EX"))
            for indx, option in enumerate(self.OPTIONS):
                print(system.color_text(f"{indx + 1}. {option.name}", "LIGHTBLUE_EX"))
        else:
            self.BORDER.show_border()
            print()

    def check_answer(self, answer):
        for indx, option in enumerate(self.OPTIONS):
            if answer.upper() in (option.NAME, indx+1):
                option()
                return
            system.error()

    def select_option(self):
        while True:
            self.show_menu()
            answer = input(system.INPUT)
            self.check_answer(answer)


class Option:
    def __init__(self, name, func):
        self.NAME = name
        self.FUNC = func

    def __call__(self, *args, **kwargs):
        self.FUNC()


class Credits:
    HEADER = system.get_ascii_text("CREDITS:")
    SOUND_RESOURCES_COMM = system.color_text("All audio was taken from freesound.org",
                                             "LIGHTWHITE_EX", is_underlined=True)

    def __init__(self, *args):
        self.CREDITS = list(args)

    def get_credits(self):
        for indx, credit in enumerate(self.CREDITS):
            print(f"{indx+1}. {credit}")

    def leave(self):
        print(self.SOUND_RESOURCES_COMM)
        input(system.color_text(">>> Press ENTER to leave", "LIGHTRED_EX"))
        pygame.mixer.music.stop()

    def __call__(self):
        credits_soundtrack()
        system.get_ascii_text_by_line(self.HEADER)
        self.get_credits()
        print(self.SOUND_RESOURCES_COMM)
        self.leave()


credits_ex = Credits("Egor Pavlenko - CEO")


class BorderOption:
    def __init__(self, lvl, name, lvl_type, descr):
        self.LVL = lvl
        self.NAME = name
        self.TYPE = lvl_type
        self.DESCR = descr
        self.DATA = [self.LVL, self.NAME, self.TYPE, self.DESCR]


basic_game_border = BorderOption("1", "BASIC", system.LVL_COLORS["COMMON"], "Infinite lives. Time-free mode.")
average_game_border = BorderOption("2", "AVERAGE", system.LVL_COLORS["COMMON"], "Finite lives. Time-free mode.")
advanced_game_border = BorderOption("3", "ADVANCED", system.LVL_COLORS["COMMON"], "Finite lives. Countdown active.")
wild_game_border = BorderOption("4", "WILD", system.LVL_COLORS["EPIC"], "Lives and time are randomized.")
custom_game_border = BorderOption("5", "CUSTOM", system.LVL_COLORS["EPIC"], "Lives and time are under your control.")
adventure_game_border = BorderOption("6", "ADVENTURE", system.LVL_COLORS["LEGENDARY"], "Beat AVERAGE, ADVANCED, and WILD levels in a single run!")
leave_border = BorderOption("7", "MAIN MENU", "---------", "Back to Main Menu")

levels = [basic_game_border, average_game_border, advanced_game_border,
          wild_game_border, custom_game_border, adventure_game_border, leave_border]


class GameChoiceBorder:
    HEADERS = ["LVL", "NAME", "TYPE", "DESCRIPTION"]

    def __init__(self, levels_):
        self.LEVELS = levels_
        self.longest_length_list = list()
        self.data_list = [self.HEADERS] + [lvl.DATA for lvl in self.LEVELS]

    def set_the_longest_data_length(self):
        for items in zip(*self.data_list):
            self.longest_length_list.append(max(len(item) for item in items))

    def show_border(self):
        for row in self.data_list:
            line = ""
            for i, item in enumerate(row):
                line += "| " + item.ljust(self.longest_length_list[i]) + " "
            line += "|"
            print(line)

    def __call__(self):
        self.set_the_longest_data_length()
        self.show_border()


game_choice_border = GameChoiceBorder(levels)
game_choice_border()
