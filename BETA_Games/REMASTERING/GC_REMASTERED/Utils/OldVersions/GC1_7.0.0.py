# Guess Code 1 v7.0.0

# Add CONTINUE MENU
# Add channels for soundtracks
# Make a few files
# Say, if you entered this num before.
# Use yaml file.
# add time

# ***************************************************************************************************

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


class Soundtrack:
    def __init__(self, name, repeats=1):
        self.NAME = name
        self.REPEATS = repeats

    @staticmethod
    def turn_off_soundtrack():
        pygame.mixer.music.stop()
        print(system.communicate("Music is turned off.", "LIGHTRED_EX"))

    def __call__(self):
        pygame.mixer.music.load(system.resource_path(f"Soundtracks/{self.NAME}"))
        pygame.mixer.music.play(self.REPEATS)


intro_soundtrack = Soundtrack("IntroSoundtrack.wav")
credits_soundtrack = Soundtrack("CreditsSoundtrack.wav", -1)
jazz1 = Soundtrack("Jazz1.wav", -1)
jazz2 = Soundtrack("Jazz2.mp3", -1)
jazz3 = Soundtrack("Jazz3.wav", -1)


class SoundPrompt:
    YOU_WIN_SOUND = pygame.mixer.Sound(system.resource_path("Sounds/YouWinSound.wav"))  # MAXTIME = 2350
    YOU_LOST_SOUND = pygame.mixer.Sound(system.resource_path("Sounds/YouLostSound.wav"))  # MAXTIME = 2500
    ABLE_TO_PLAY = True

    def __call__(self):
        self.ABLE_TO_PLAY = not self.ABLE_TO_PLAY
        match self.ABLE_TO_PLAY:
            case True:
                self.YOU_WIN_SOUND.play(maxtime=2350)
                print(system.communicate("Sound is turned ON", "LIGHTGREEN_EX"))
            case False:
                self.YOU_LOST_SOUND.play(maxtime=2500)
                print(system.communicate("Sound is turned OFF", "LIGHTRED_EX"))


sound_prompt = SoundPrompt()


class WinStreakController:
    ENCODING = "utf-8"
    RESOURCE_NAME = SAVE_NAME = "Utils/WIN_STREAK_FILE"

    def __init__(self):
        self.SAVE_PATH = os.path.join(os.getcwd(), self.SAVE_NAME)
        self.__ensure_writable_copy()

    def __ensure_writable_copy(self):
        if not os.path.exists(self.SAVE_PATH):
            try:
                shutil.copyfile(system.resource_path(self.RESOURCE_NAME), self.SAVE_PATH)
            except Exception:
                with open(self.SAVE_PATH, "w", encoding=self.ENCODING) as file:
                    file.write("0")

    def get_win_streak(self, is_communicate=False):
        with open(self.SAVE_PATH, "r", encoding=self.ENCODING) as file:
            win_streak = file.read()
            match is_communicate:
                case True:
                    return win_streak
                case _:
                    return f"Your win streak: {win_streak}"

    def __call__(self, is_defeat=False):
        new_streak = 0 if is_defeat else self.get_win_streak() + 1
        with open(self.SAVE_PATH, "w", encoding=self.ENCODING) as file:
            file.write(str(new_streak))


win_streak_controller = WinStreakController()


class GameIntro:
    GitHub_URL = "https://github.com/GogaUa069"
    Instagram_URL = "https://www.instagram.com/gogaua096/"

    def get_accounts(self):
        print(system.communicate(f"Follow me on Instagram -> {self.Instagram_URL}", "CYAN"))
        print(system.communicate(f"Check my GitHub -> {self.GitHub_URL}\n", "CYAN"))

    @staticmethod
    def loading():
        with tqdm(total=100) as pbar:
            for _ in range(100):
                color = choice(system.COLORS)
                pbar.set_description_str(system.communicate("Loading", color))
                pbar.update(1)
                sleep(0.04)

    @staticmethod
    def show_game_banner(banner):
        sleep(0.5)
        print(system.communicate("Welcome to:", "CYAN"))
        sleep(1.5)
        system.set_ascii_text(banner)
        print(system.communicate("Made by GogaUa\n", "WHITE"))
        sleep(1)

    def __call__(self):
        intro_soundtrack()
        self.get_accounts()
        self.show_game_banner("Guess Code v.7.0.0")
        self.loading()


game_intro = GameIntro()


class Credits:
    def __init__(self, *args):
        self.CREDITS = list(args)

    def get_credits(self):
        for indx, credit in enumerate(self.CREDITS, 1):
            system.get_text_by_let(f"{indx}. {credit}")
            print()
        sleep(1)
        print()

    @staticmethod
    def close_credits_menu():
        print(system.communicate("All audio was taken from freesound.org", "LIGHTWHITE_EX"))
        input(system.communicate(">>> Press ENTER to leave", "LIGHTRED_EX"))
        pygame.mixer.music.stop()

    def __call__(self):
        credits_soundtrack()
        system.set_ascii_text("CREDITS:")
        self.get_credits()
        self.close_credits_menu()


credits_menu = Credits("Egor Pavlenko - CEO")


class Option:
    def __init__(self, name, func):
        self.NAME = name
        self.FUNC = func

    def __call__(self):
        self.FUNC()


class BorderOption:
    def __init__(self, lvl, name, lvl_type, descr):
        self.LVL = lvl
        self.NAME = name
        self.LVL_TYPE = lvl_type
        self.DESCR = descr
        self.DATA = [self.LVL, self.NAME, self.LVL_TYPE, self.DESCR]


LEVELS = [
    BorderOption("1", "BASIC", system.LVL_TYPES["COMMON"], "Infinite lives. Time-free mode."),
    BorderOption("2", "AVERAGE", system.LVL_TYPES["COMMON"], "Finite lives. Time-free mode."),
    BorderOption("3", "ADVANCED", system.LVL_TYPES["COMMON"], "Finite lives. Countdown active."),
    BorderOption("4", "WILD", system.LVL_TYPES["EPIC"], "Lives and time are randomized."),
    BorderOption("5", "CUSTOM", system.LVL_TYPES["EPIC"], "Lives and time are under your control."),
    BorderOption("6", "ADVENTURE",  system.LVL_TYPES["LEGENDARY"],"Beat AVERAGE, ADVANCED, and WILD levels in a single run and get a prize!"),
    BorderOption("7", "MAIN MENU", "---------", "Back to Main Menu")]


class MenuPattern:
    def __init__(self, header, options, border=None):
        self.HEADER, self.OPTIONS, self.BORDER = header, options, border

    def show_menu(self):
        if self.BORDER is None:
            print(system.communicate(f"\n>>> {self.HEADER}", "LIGHTRED_EX"))
            for i, opt in enumerate(self.OPTIONS, 1):
                print(system.communicate(f"{i}. {opt.NAME}", "LIGHTBLUE_EX"))
        else:
            self.BORDER()

    def check_answer(self, answer):
        for indx, option in enumerate(self.OPTIONS, 1):
            if answer.upper() in (option.NAME.upper(), str(indx)):
                option()
                return
        print(system.communicate("ERROR: Select one of the options shown above!", "LIGHTRED_EX"))

    def __call__(self):
        answer = str()
        while answer != str(len(self.OPTIONS)):
            self.show_menu()
            answer = input(system.INPUT)
            self.check_answer(answer)


class BorderPattern:
    HEADERS = ["LVL", "NAME", "TYPE", "DESCRIPTION"]

    def __init__(self, levels: list):
        self.DATA = [self.HEADERS] + [lvl.DATA for lvl in levels]
        self.WIDTHS = [max(len(system.del_color(item)) for item in col) for col in zip(*self.DATA)]

    def __call__(self):
        for row in self.DATA:
            line = "".join(f"| {item.ljust(self.WIDTHS[i]+1)}" for i, item in enumerate(row)) + "|"
            print(line)


game_border = BorderPattern(LEVELS)


# SOUNDTRACKS
jazz1_option = Option("Jazz1", jazz1)
jazz2_option = Option("Jazz2", jazz2)
jazz3_option = Option("Jazz3", jazz3)
turn_off_soundtrack_option = Option("Turn Off", Soundtrack.turn_off_soundtrack)
from_soundtracks_to_audio = Option("Back - Audio", system.communicate)

soundtracks_options = (jazz1_option, jazz2_option, jazz3_option, turn_off_soundtrack_option, from_soundtracks_to_audio)
soundtracks_menu = MenuPattern("Soundtracks", soundtracks_options)

# SOUNDS
toggle_sound_option = Option("Turn Off/On", sound_prompt)
from_sounds_to_audio = Option("Back - Audio", system.communicate)

sounds_options = (toggle_sound_option, from_sounds_to_audio)
sounds_menu = MenuPattern("Sounds", sounds_options)

# AUDIO
soundtracks_option = Option("Soundtracks", soundtracks_menu)
sounds_option = Option("Sounds", sounds_menu)
from_audio_to_settings = Option("Back - Settings", system.communicate)

audio_options = (soundtracks_option, sounds_option, from_audio_to_settings)
audio_menu = MenuPattern("Audio", audio_options)

# SETTINGS
rules_option = Option("Rules", system.get_rules)
audio_option = Option("Audio", audio_menu)
credits_option = Option("Credits", credits_menu)
from_settings_to_main_menu = Option("Back - Main Menu", system.communicate)

settings_options = (rules_option, audio_option, credits_option, from_settings_to_main_menu)
settings_menu = MenuPattern("Settings", settings_options)

# MAIN MENU
play_option = Option("Play", system.communicate)
settings_option = Option("Settings", settings_menu)
quit_option = Option("Quit", system.quit_game)

main_menu_options = (play_option, settings_option, quit_option)
main_menu = MenuPattern("Main Menu", main_menu_options)


def game():
    game_intro()
    main_menu()


game()
