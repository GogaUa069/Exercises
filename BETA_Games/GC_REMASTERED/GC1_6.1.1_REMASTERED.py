# Guess Code 1 v6.1.1 Remastered

# Add CONTINUE MENU
# Add channels for soundtracks
# Make a few files

# ***************************************************************************************************

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
    """
    Class for all patterns.
    """
    COLORS = [attr for attr in dir(colorama.Fore) if not attr.startswith("_")]

    def __init__(self):
        self.INPUT = self.communicate("<<< ", "LIGHTWHITE_EX")
        self.RULES = (self.communicate("Press ENTER to continue\n","LIGHTRED_EX"),
                      self.communicate(">>> Rules:","LIGHTRED_EX"),
                      self.communicate(">>> Find the number the computer guessed.","LIGHTBLUE_EX"),
                      self.communicate(">>> 1. Select a range (e.g. 5-200).","LIGHTBLUE_EX"),
                      self.communicate(">>> 2. Start guessing.","LIGHTBLUE_EX"),
                      self.communicate(">>> Your turn!","LIGHTRED_EX"))
        self.LVL_TYPES = {"COMMON": self.communicate("COMMON", "LIGHTBLUE_EX"),
                          "EPIC": self.communicate("EPIC", "LIGHTMAGENTA_EX"),
                          "LEGENDARY": self.communicate("LEGENDARY", "LIGHTYELLOW_EX")}

    @staticmethod
    def del_color(text: str):
        """
        Deletes color from text.
        """
        ansi_escape = re.compile(r"\x1B[@-_][0-?]*[ -/]*[@-~]")
        return ansi_escape.sub("", text)

    @staticmethod
    def resource_path(relative_path: str):
        """
        Saves soundtracks.
        """
        base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    @staticmethod
    def communicate(text=None, color=None, is_error=False, is_bold=False, is_underlined=False):
        """
        Pattern for communicates.
        """
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

    def quit_game(self):
        """
        Quits the game.
        """
        print(self.communicate("Goodbye! :)", "LIGHTCYAN_EX"))
        sleep(0.5)

    def get_ascii_text(self, text: str, color="LIGHTBLUE_EX", font="standard"):
        """
        Prints text in ASCII format.
        """
        f = pyfiglet.Figlet(font=font)
        ascii_text = f.renderText(text)
        for line in ascii_text.splitlines():
            print(self.communicate(line, color, is_bold=True))
            sleep(0.25)

    def get_text_by_let(self, text: str):
        """
        Prints text char by char.
        """
        for char in text:
            sleep(0.21)
            print(self.communicate(char, "LIGHTWHITE_EX"), end="")

    def get_rules(self):
        """
        Gives rules line by line.
        """
        for line in self.RULES:
            print(line, end="")
            input()


system = SystemPrompt()


class Soundtrack:
    """
    Soundtrack pattern.
    """
    def __init__(self, name: str, repeats=1):
        self.NAME = name
        self.REPEATS = repeats

    @staticmethod
    def turn_off_soundtrack():
        """
        Turning off a soundtrack.
        """
        pygame.mixer.music.stop()
        print(system.communicate(">>> Music if turned Off", "LIGHTRED_EX"))

    def __call__(self):
        pygame.mixer.music.load(system.resource_path(f"Soundtracks/{self.NAME}"))
        pygame.mixer.music.play(self.REPEATS)


intro_soundtrack = Soundtrack("IntroSoundtrack.wav")
credits_soundtrack = Soundtrack("CreditsSoundtrack.wav", -1)
jazz1 = Soundtrack("Jazz1.wav", -1)
jazz2 = Soundtrack("Jazz2.mp3", -1)
jazz3 = Soundtrack("Jazz3.wav", -1)


class SoundPrompt:
    """
    Works with sounds.
    """
    YOU_WIN_SOUND = pygame.mixer.Sound(system.resource_path("Sounds/YouWinSound.wav"))  # MAXTIME = 2350
    YOU_LOST_SOUND = pygame.mixer.Sound(system.resource_path("Sounds/YouLostSound.wav"))  # MAXTIME = 2500
    ABLE_TO_PLAY = True

    def __call__(self):
        """
        Toggles sound.
        """
        self.ABLE_TO_PLAY = not self.ABLE_TO_PLAY
        match self.ABLE_TO_PLAY:
            case True:
                self.YOU_WIN_SOUND.play(maxtime=2350)
                print(system.communicate(">>> Sound is turned ON", "LIGHTGREEN_EX"))
            case False:
                self.YOU_LOST_SOUND.play(maxtime=2500)
                print(system.communicate(">>> Sound is turned OFF", "LIGHTRED_EX"))


toggle_sound = SoundPrompt()


class WinStreakController:
    """
    All about win streak.
    """
    ENCODING = "utf-8"
    RESOURCE_NAME = SAVE_NAME = "Utils/WIN_STREAK_FILE"

    def __init__(self):
        self.SAVE_PATH = os.path.join(os.getcwd(), self.SAVE_NAME)
        self._ensure_writable_copy()

    @staticmethod
    def _resource_path(relative_path: str):
        """
        ...
        """
        base_path = getattr(sys, "_MEIPASS", os.path.dirname(__file__))
        return os.path.join(base_path, relative_path)

    def _ensure_writable_copy(self):
        """
        ...
        """
        if not os.path.exists(self.SAVE_PATH):
            try:
                shutil.copyfile(self._resource_path(self.RESOURCE_NAME), self.SAVE_PATH)
            except Exception:
                with open(self.SAVE_PATH, "w", encoding=self.ENCODING) as file:
                    file.write("0")

    def get_win_streak(self, is_communicate=False):
        """
        Returns win streak.
        """
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
    """
    All about game intro.
    """
    GitHub_URL = "https://github.com/GogaUa069"
    Instagram_URL = "https://www.instagram.com/gogaua096/"

    def get_accounts(self):
        """
        Shows accounts.
        """
        print(system.communicate(f"Follow me on Instagram -> {self.Instagram_URL}", "CYAN"))
        print(system.communicate(f"Check my GitHub -> {self.GitHub_URL}\n", "CYAN"))

    @staticmethod
    def loading():
        """
        Loading line.
        """
        with tqdm(total=100) as pbar:
            for i in range(100):
                color = choice([c for c in system.COLORS if c != "BLACK"])
                pbar.set_description_str(system.communicate("Loading", color))
                pbar.update(1)
                sleep(0.04)

    @staticmethod
    def show_game_banner(banner: str):
        """
        Shows game banner.
        """
        sleep(0.5)
        print(system.communicate("Welcome to:", "CYAN", is_bold=True))
        sleep(1.5)
        system.get_ascii_text(banner)
        print(system.communicate("Made by GogaUa\n", "WHITE", is_bold=True))
        sleep(1)

    def __call__(self):
        intro_soundtrack()
        self.get_accounts()
        self.show_game_banner("Guess Code v6.1.1\nRemastered")
        self.loading()


game_intro = GameIntro()


class Credits:
    """
    About game creator(s)
    """
    HEADER = "CREDITS:"

    def __init__(self, *args):
        self.CREDITS = list(args)

    def get_credits(self):
        """
        Showing credits.
        """
        for indx, credit in enumerate(self.CREDITS, 1):
            text = f"{indx}. {credit}"
            system.get_text_by_let(text)
            print()
        sleep(1)
        print()

    @staticmethod
    def leave_credits():
        """
        Leaving the credits menu
        """
        print(system.communicate("All audio was taken from freesound.org", "LIGHTWHITE_EX", is_underlined=True))
        input(system.communicate(">>> Press ENTER to leave", "LIGHTRED_EX"))
        pygame.mixer.music.stop()

    def __call__(self):
        credits_soundtrack()
        system.get_ascii_text(self.HEADER)
        self.get_credits()
        self.leave_credits()


credits_ = Credits("Egor Pavlenko - CEO")


class Option:
    """
    Options for Menus
    """
    def __init__(self, name: str, func):
        self.NAME = name
        self.FUNC = func

    def __call__(self):
        self.FUNC()


class BorderOption:
    """
    Options for Borders.
    """
    def __init__(self, lvl: str, name: str, lvl_type: str, descr: str):
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
    """
    Pattern for Menus.
    """
    def __init__(self, header: str, options: tuple, border=None):
        self.HEADER, self.OPTIONS, self.BORDER = header, options, border

    def show_menu(self):
        """
        Showing menu: In text format or border.
        """
        if self.BORDER is None:
            print(system.communicate(f"\n>>> {self.HEADER}", "LIGHTRED_EX"))
            for i, opt in enumerate(self.OPTIONS, 1):
                print(system.communicate(f"{i}. {opt.NAME}", "LIGHTBLUE_EX"))
        else:
            self.BORDER()

    def check_answer(self, answer: str):
        """
        Checks answer in menu.
        """
        for indx, option in enumerate(self.OPTIONS, 1):
            if answer.upper() in (option.NAME.upper(), str(indx)):
                option()
                return
        print(system.communicate("Select one of the options shown above!", is_error=True))

    def __call__(self):
        answer = str
        while answer != str(len(self.OPTIONS)):
            self.show_menu()
            answer = input(system.INPUT)
            self.check_answer(answer)


class BorderPattern:
    """
    Pattern for border type menu.
    """
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
toggle_sound_option = Option("Turn Off/On", toggle_sound)
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
credits_option = Option("Credits", credits_)
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
    """
    Main game func.
    """
    game_intro()
    main_menu()

game()
