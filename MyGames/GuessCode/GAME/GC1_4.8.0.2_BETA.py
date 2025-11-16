# v 4.8.0.2-beta

# Add Streak saving
# Add PLAY AGAIN menu

import time
from colorama import Fore, Style, init
from random import randint, shuffle, choice
import re
import pyfiglet
from tqdm import tqdm
import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import pygame

pygame.init()
init()  # Colorama

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

WIN_STREAK = 0


class SystemPrompt:
    """
    Class for the all system communicates and functions
    """
    COLORS = [attr for attr in dir(Fore) if not attr.startswith("_")]
    shuffle(COLORS)

    def __init__(self):
        self.INPUT = self.get_colored_text("<<< ", "LIGHTWHITE_EX")
        self.RULES = (
            self.get_colored_text(">>> Press ENTER to continue\n", "LIGHTRED_EX"),
            self.get_colored_text(">>> Rules:", "LIGHTRED_EX"),
            self.get_colored_text(">>> Find the number the computer guessed.", "BLUE"),
            self.get_colored_text(">>> 1. Choose a range (e.g. 5-200).", "BLUE"),
            self.get_colored_text(">>> 2. Start guessing!", "BLUE"),
            self.get_colored_text(">>> Your turn!", "LIGHTRED_EX")
        )
        self.COMMON = self.get_colored_text("COMMON", "LIGHTBLUE_EX")
        self.EPIC = self.get_colored_text("EPIC", "LIGHTMAGENTA_EX")
        self.LEGENDARY = self.get_colored_text("LEGENDARY", "LIGHTYELLOW_EX")

    @staticmethod
    def get_colored_text(text: str, color: str, is_bold=False, is_reset_all=True, is_with_line=False):
        """
        Coloring text
        :param text:
        :param color: color
        :param is_bold: is bold?
        :param is_reset_all: is reset color after a phrase
        :return: Colored text
        """
        colored_text = getattr(Fore, color) + text
        if is_bold:
            colored_text = Style.BRIGHT + colored_text
        if is_reset_all:
            colored_text = colored_text + Style.RESET_ALL
        if is_with_line:
            colored_text = f"\033[4m{colored_text}\033[0m"
        return colored_text

    def rules(self):
        for rule in self.RULES:
            print(rule, end="")
            input()

    def coming_soon(self, communicate="Coming soon..."):
        print(self.get_colored_text(f">>> {communicate}", "LIGHTWHITE_EX"))

    def error(self, communicate="Select one of the options shown above!", end=""):
        print(self.get_colored_text(f">>> Error: {communicate}", "LIGHTRED_EX"), end)

    def farewell(self, communicate="Goodbye! :)"):
        print(self.get_colored_text(f">>> {communicate}", "LIGHTCYAN_EX"))
        time.sleep(0.5)

    def pass_func(self):
        return

    @staticmethod
    def del_ascii(text):
        ansi_escape = re.compile(r"\x1B[@-_][0-?]*[ -/]*[@-~]")
        return ansi_escape.sub("", text)


system = SystemPrompt()


class GameIntro:
    """
    All game intro functions
    """
    INTRO_SOUNDTRACK = pygame.mixer.Sound(resource_path("Sounds/IntroMusic.wav"))

    @staticmethod
    def my_accounts():
        print(system.get_colored_text("@GogaUa096 - Follow me on Instagram :)\n"
                                      "@GogaUa069 - Check my GitHub\n", "CYAN"))

    @staticmethod
    def loading():
        """
        Loading line with %
        :return: loading
        """
        with tqdm(total=100) as pbar:
            for i in range(100):
                color = choice([c for c in system.COLORS if c != "BLACK"])
                pbar.set_description_str(system.get_colored_text("Loading", color))
                pbar.update(1)
                time.sleep(0.03)
        print()

    @staticmethod
    def show_game_banner(banner: str):
        """
        Ascii game banner
        :param banner: game name
        :return: banner
        """
        time.sleep(0.5)
        print(system.get_colored_text("Welcome to:", "CYAN", True))
        time.sleep(1.5)

        ascii_banner = pyfiglet.figlet_format(banner)
        for line in ascii_banner.splitlines():
            print(system.get_colored_text(line, "LIGHTBLUE_EX"))
            time.sleep(0.25)

        print(system.get_colored_text("Made by GogaUa\n", "WHITE", True))
        time.sleep(1)

    def intro(self):
        """
        Game intro with all functions
        :return: game intro
        """
        self.INTRO_SOUNDTRACK.play()
        self.my_accounts()
        self.show_game_banner("Guess Code 4.8.0.2 BETA")  # UPDATES UPDATES UPDATES UPDATES UPDATES UPDATES
        self.loading()


game_intro = GameIntro()


class MenuPattern:
    def __init__(self, header: str, options: tuple, is_border=False):
        self.header = header
        self.options = options
        self.answer = str()
        self.is_border = is_border

    def show_menu(self):
        if not self.is_border:
            print(system.get_colored_text(f"\n>>> {self.header}", "LIGHTRED_EX"))
            for indx, option in enumerate(self.options):
                print(system.get_colored_text(f"{indx + 1}. {option.name}", "BLUE"))
        else:
            border.show_border()
            print()

    def match_answer(self):
        for indx, option in enumerate(self.options):
            if self.answer in option.variants:
                option.usage()
                return
        system.error()

    def select_answer(self):
        while self.answer not in self.options[-1].variants:
            self.show_menu()
            self.answer = input(system.INPUT).strip().upper()
            self.match_answer()


class Option:
    def __init__(self, name: str, func, variants: tuple):
        self.name = name
        self.func = func
        self.variants = variants

    def usage(self):
        self.func()


class SoundtrackOption:
    def __init__(self, name: str, path, variants: tuple):
        self.name = name
        self.path = path
        self.variants = variants

    def usage(self):
        Soundtracks.play_soundtrack(self.path)


class SoundOption:
    def __init__(self, name: str, sound, variants: tuple, is_sound: bool):
        self.name = name
        self.sound = sound
        self.variants = variants
        self.is_sound = is_sound

    def usage(self):
        flag = sounds.toggle_sound()
        print(self.sound[flag]["COMMUNICATE"])
        sound = self.sound[flag]
        sound["SOUND"].play(maxtime=sound["MAXTIME"])


basic_game_data = ("1", "BASIC", system.COMMON, "Infinite lives. Time-free mode.")
average_game_data = ("2", "AVERAGE", system.COMMON, "Finite lives. Time-free mode.")
advanced_game_data = ("3", "ADVANCED", system.COMMON, "Finite lives. Countdown active.")
wild_game_data = ("4", "WILD", system.EPIC, "Lives and time are randomized.")
custom_game_data = ("5", "CUSTOM", system.EPIC, "Lives and time are under your control.")
adventure_data = ("6", "ADVENTURE", system.LEGENDARY, "Beat AVERAGE, ADVANCED, and WILD levels in a single run!")


class Credits:
    HEADER = "CREDITS:"
    SOUNDTRACK = resource_path("Music/EpicCreditsSoundtrack.wav")
    freesound_comm = system.get_colored_text(
        "\nAll soundtracks were taken from freesound.org",
        "LIGHTWHITE_EX", is_with_line=True
    )

    def __init__(self, *args):
        self.credit_list = list(args)

    def __call__(self, *args, **kwargs):
        pygame.mixer.music.load(resource_path(self.SOUNDTRACK))
        pygame.mixer.music.play(-1)

        def name_by_let(name: str, indx=0):
            if indx > 0:
                print(system.get_colored_text(f"{indx}. ", "LIGHTWHITE_EX"), end="")
            for char in name:
                time.sleep(0.21)
                print(system.get_colored_text(f"{char}", "LIGHTWHITE_EX"), end="")
            print()

        def get_banner_by_let(banner: str):
            ascii_banner = pyfiglet.figlet_format(banner)
            for line in ascii_banner.splitlines():
                print(system.get_colored_text(line, "LIGHTBLUE_EX"))
                time.sleep(0.25)

        get_banner_by_let(self.HEADER)
        for indx, credit in enumerate(self.credit_list):
            name_by_let(credit, indx+1)
            time.sleep(1)

        print(self.freesound_comm)
        input(system.get_colored_text(">>> Press ENTER to leave ", "LIGHTRED_EX"))
        pygame.mixer.music.stop()


credits = Credits("GogaUa (Yegor Pavlenko) - CEO")


class GameBorderPattern:
    def __init__(self, lvl: str, name: str, type_: str, description: str):
        self.lvl = {"FUNC": lvl, "SPACE": ""}
        self.name = {"FUNC": name, "SPACE": ""}
        self.type = {"FUNC": type_, "SPACE": ""}
        self.description = {"FUNC": description, "SPACE": ""}

        self.data_list = [self.lvl, self.name, self.type, self.description]


basic_game_border = GameBorderPattern(*basic_game_data)
average_game_border = GameBorderPattern(*average_game_data)
advanced_game_border = GameBorderPattern(*advanced_game_data)
wild_game_border = GameBorderPattern(*wild_game_data)
custom_game_border = GameBorderPattern(*custom_game_data)
adventure_border = GameBorderPattern(*adventure_data)


class GameChoiceBorder:

    def __init__(self, headers_, data_: list):
        self.headers = headers_
        self.data = data_

        self.longest_length = 0
        self.longest_name = 0
        self.longest_type = 0
        self.longest_description = 0

    def get_longest(self, attr):
        attr_list = [system.del_ascii(getattr(game, attr)["FUNC"]) for game in self.data]
        longest_attr = max(attr_list, key=lambda x: len(x))
        setattr(self, "longest_"+attr, len(longest_attr))

    def get_space(self, attr):
        for game in self.data:
            space_len = (getattr(self, "longest_" + attr) - len(system.del_ascii(str(getattr(game, attr)["FUNC"])))) + 1
            getattr(game, attr)["SPACE"] = " " * space_len

    def sort_data(self):
        for header in ("lvl", "name", "type", "description"):
            self.get_longest(header)
            self.get_space(header)

    def show_border(self):
        self.sort_data()
        print(system.get_colored_text(">>> Select Game Mode:\n", "LIGHTRED_EX"))
        for game in self.data:
            print("| ", end="")
            for attr in game.data_list:
                print(attr["FUNC"]+attr["SPACE"], end="| ")
            print()


headers = GameBorderPattern("LVL", "NAME", "TYPE", "DESCRIPTION")
leave_func = GameBorderPattern("7", "MAIN MENU", "---------", "Back to Main Menu")
data = [headers, basic_game_border, average_game_border, advanced_game_border, wild_game_border, custom_game_border,
        adventure_border, leave_func]

border = GameChoiceBorder(headers, data)


class BasicGame:
    BARRIER_RANGE = range(5, 201)

    min_range = min(BARRIER_RANGE)
    max_range = max(BARRIER_RANGE)

    def __init__(self):
        self.search_barrier = self.hidden_number = self.attempts_counter = self.search_range = 0

    def set_barrier(self):
        barrier_error = f"Enter TOTAL in range {self.min_range}-{self.max_range}"
        print(system.get_colored_text("\nBasic Game:"
                                      "\n>>> Select search barrier."
                                      f"\n>>> Enter total in range {self.min_range}-{self.max_range}", "CYAN"))
        while True:
            try:
                print()
                self.search_barrier = int(input(system.INPUT))
                if self.search_barrier in self.BARRIER_RANGE:
                    self.hidden_number = randint(1, self.search_barrier)
                    self.search_range = range(1, self.search_barrier + 1)
                    break
                else:
                    system.error(barrier_error)
            except ValueError:
                system.error(barrier_error)

    def search_num(self):
        global WIN_STREAK

        answer = None
        answer_error = f"Enter TOTAL in RANGE 1-{self.search_barrier}"
        print(system.get_colored_text(f">>> Your turn!\n"
                                      f">>> Enter total in range 1-{self.search_barrier}", "CYAN"))

        while answer != self.hidden_number:
            try:
                print()
                answer = int(input(system.INPUT))
                if answer < self.hidden_number and answer in self.search_range:
                    print(system.get_colored_text("Your total is SMALLER than hidden number!", "LIGHTWHITE_EX"))
                    self.attempts_counter += 1
                elif answer > self.hidden_number and answer in self.search_range:
                    print(system.get_colored_text("Your total is BIGGER than hidden number!", "LIGHTWHITE_EX"))
                    self.attempts_counter += 1
                elif answer == self.hidden_number:
                    WIN_STREAK += 1
                    sounds.play_sound(True)
                    print(system.get_colored_text(f"Yey! You found the hidden number!\n"
                                                  f"It took {self.attempts_counter} attempt(s)!\n"
                                                  f"Your win streak: {WIN_STREAK}\n", "LIGHTCYAN_EX"))
                else:
                    system.error(answer_error)
            except ValueError:
                system.error(answer_error)

    def __call__(self, *args, **kwargs):
        self.__init__()
        self.set_barrier()
        self.search_num()


basic_game = BasicGame()


class AverageGame:
    BARRIER_RANGE = range(5, 201)

    min_range = min(BARRIER_RANGE)
    max_range = max(BARRIER_RANGE)

    def __init__(self):
        self.search_barrier = \
        self.hidden_number = \
        self.attempts_counter = \
        self.search_range = \
        self.attempts_limit = 0

    def set_barrier(self):
        barrier_error = f"Enter TOTAL in range {self.min_range}-{self.max_range}"
        print(system.get_colored_text("\nAverage Game:"
                                      "\n>>> Select search barrier."
                                      f"\n>>> Enter total in range {self.min_range}-{self.max_range}", "CYAN"))
        while True:
            try:
                print()
                self.search_barrier = int(input(system.INPUT))
                if self.search_barrier in self.BARRIER_RANGE:
                    self.hidden_number = randint(1, self.search_barrier)
                    self.search_range = range(1, self.search_barrier + 1)
                    break
                else:
                    system.error(barrier_error)
            except ValueError:
                system.error(barrier_error)

    def set_attempts_limit(self):
        attempts = 0
        barrier = self.search_barrier

        while barrier != 1:
            barrier //= 2
            attempts += 1
        self.attempts_limit = attempts + 1

    def search_num(self):
        global WIN_STREAK

        answer = None
        answer_error = f"Enter TOTAL in RANGE 1-{self.search_barrier}"
        print(system.get_colored_text(f">>> Your turn!\n"
                                      f">>> Enter total in range 1-{self.search_barrier}\n"
                                      f">>> You have {self.attempts_limit} attempts!", "CYAN"))

        while answer != self.hidden_number and self.attempts_counter < self.attempts_limit:
            try:
                print()
                answer = int(input(system.INPUT))
                if answer < self.hidden_number and answer in self.search_range:
                    print(system.get_colored_text("Your total is SMALLER than hidden number!", "LIGHTWHITE_EX"))
                    self.attempts_counter += 1
                elif answer > self.hidden_number and answer in self.search_range:
                    print(system.get_colored_text("Your total is BIGGER than hidden number!", "LIGHTWHITE_EX"))
                    self.attempts_counter += 1
                elif answer == self.hidden_number:
                    WIN_STREAK += 1
                    sounds.play_sound(True)
                    print(system.get_colored_text(f"Yey! You found the hidden number!\n"
                                                  f"It took {self.attempts_counter} attempt(s)!\n"
                                                  f"Your win streak: {WIN_STREAK}\n", "LIGHTCYAN_EX"))
                    break
                else:
                    system.error(answer_error)
                if self.attempts_counter == self.attempts_limit:
                    sounds.play_sound(False)
                    print(Fore.LIGHTRED_EX + "You've reached the maximum number of attempts!\n"
                                             "You lost Your win streak!\n" + Style.RESET_ALL)
                    WIN_STREAK = 0
                    break
                attempts_left = self.attempts_limit-self.attempts_counter
                print(system.get_colored_text(f"{attempts_left} attempts left!", "LIGHTWHITE_EX"))
            except ValueError:
                system.error(answer_error)

    def __call__(self, *args, **kwargs):
        self.__init__()
        self.set_barrier()
        self.set_attempts_limit()
        self.search_num()


average_game = AverageGame()


class GameChoice:
    def __init__(self):
        self.BASIC = Option("BASIC", basic_game, ("BASIC", "1"))
        self.AVERAGE = Option("AVERAGE", average_game, ("AVERAGE", "2"))
        self.ADVANCED = Option("ADVANCED", system.coming_soon, ("ADVANCED", "3"))
        self.WILD = Option("WILD", system.coming_soon, ("WILD", "4"))
        self.CUSTOM = Option("CUSTOM", system.coming_soon, ("CUSTOM", "5"))
        self.ADVENTURE = Option("ADVENTURE", system.coming_soon, ("ADVENTURE", "6"))
        self.BACK = Option("BACK - MAIN MENU", system.pass_func, ("BACK", "MAIN MENU", "7"))

        self.OPTIONS = (self.BASIC, self.AVERAGE, self.ADVANCED, self.WILD, self.CUSTOM, self.ADVENTURE, self.BACK)

    def __call__(self, *args, **kwargs):
        game_choice_menu = MenuPattern("Game Choice", self.OPTIONS, True)
        game_choice_menu.select_answer()


game_choice = GameChoice()


class Soundtracks:
    HEADER = "Soundtracks"

    CASUAL_JAZZ = resource_path("Music/CasualJazz.wav")
    COOL_JAZZ = resource_path("Music/CoolJazz.mp3")
    ELECTRIC_JAZZ = resource_path("Music/ElectricJazz.wav")

    def __init__(self):
        self.JAZZ1 = SoundtrackOption("Casual Jazz", self.CASUAL_JAZZ, ("CASUAL", "JAZZ 1", "1"))
        self.JAZZ2 = SoundtrackOption("Cool Jazz", self.COOL_JAZZ, ("COOL", "JAZZ 2", "2"))
        self.JAZZ3 = SoundtrackOption("Electric Jazz", self.ELECTRIC_JAZZ, ("ELECTRIC", "JAZZ 3", "3"))
        self.TURN_OFF = Option("Turn Off", self.turn_off_music, ("TURN OFF", "OFF", "4"))
        self.BACK = Option("Back - Audio", system.pass_func, ("BACK", "AUDIO", "5"))

        self.OPTIONS = (self.JAZZ1, self.JAZZ2, self.JAZZ3, self.TURN_OFF, self.BACK)

    @staticmethod
    def play_soundtrack(path):
        try:
            pygame.mixer.music.load(resource_path(path))
            pygame.mixer.music.play(-1)
        except pygame.error:
            system.error(f"Can't find soundtrack at path {path}")

    @staticmethod
    def turn_off_music():
        pygame.mixer.music.stop()
        print(system.get_colored_text("Music is turned Off", "LIGHTRED_EX"))

    def __call__(self, *args, **kwargs):
        soundtracks_menu = MenuPattern(self.HEADER, self.OPTIONS)
        soundtracks_menu.select_answer()


soundtracks = Soundtracks()


class Sounds:
    HEADER = "Sounds"
    IS_SOUND = True

    SOUNDS = {True: {"SOUND": pygame.mixer.Sound(resource_path("Sounds/YouWinGoga.wav")), "MAXTIME": 2350,
                     "COMMUNICATE": system.get_colored_text("Sounds are turned On", "LIGHTGREEN_EX")},
              False: {"SOUND": pygame.mixer.Sound(resource_path("Sounds/YouLostGoga.wav")), "MAXTIME": 2500,
                      "COMMUNICATE": system.get_colored_text("Sounds are turned Off", "LIGHTRED_EX")}
              }

    def __init__(self):
        self.TOGGLE = SoundOption("Turn On/Off", self.SOUNDS, ("ON", "OFF", "1"), self.IS_SOUND)
        self.BACK = Option("Back - Audio", system.pass_func, ("BACK", "AUDIO", "2"))

        self.OPTIONS = (self.TOGGLE, self.BACK)

    def toggle_sound(self):
        self.IS_SOUND = not self.IS_SOUND
        return self.IS_SOUND

    def play_sound(self, sound_type: bool):
        if self.IS_SOUND:
            sound = self.SOUNDS[sound_type]
            sound["SOUND"].play(maxtime=sound["MAXTIME"])

    def __call__(self, *args, **kwargs):
        sounds_menu = MenuPattern(self.HEADER, self.OPTIONS)
        sounds_menu.select_answer()


sounds = Sounds()


class Audio:
    HEADER = "Audio"

    def __init__(self):
        self.SOUNDTRACKS = Option(soundtracks.HEADER, soundtracks, ("SOUNDTRACKS", "1"))
        self.SOUNDS = Option(sounds.HEADER, sounds, ("SOUNDS", "2"))
        self.BACK = Option("Back - Settings", system.pass_func, ("BACK", "SETTINGS", "3"))
        self.OPTIONS = (self.SOUNDTRACKS, self.SOUNDS, self.BACK)

    def __call__(self, *args, **kwargs):
        audio_menu = MenuPattern(self.HEADER, self.OPTIONS)
        audio_menu.select_answer()


audio = Audio()


class Settings:
    HEADER = "Settings"

    def __init__(self):
        self.RULES = Option("Rules", system.rules, ("RULES", "1"))
        self.AUDIO = Option(audio.HEADER, audio, ("AUDIO", "2"))
        self.BACK = Option("Back - Main Menu", system.pass_func, ("BACK", "MAIN MENU", "3"))
        self.OPTIONS = (self.RULES, self.AUDIO, self.BACK)

    def __call__(self, *args, **kwargs):
        settings_menu = MenuPattern(self.HEADER, self.OPTIONS)
        settings_menu.select_answer()


settings = Settings()


class MainMenu:
    HEADER = "Main Menu"

    def __init__(self):
        self.PLAY = Option("Play", game_choice, ("PLAY", "P", "1"))
        self.SETTINGS = Option(settings.HEADER, settings, ("SETTINGS", "S", "2"))
        self.CREDITS = Option("Credits", credits, ("CREDITS", "C", "3"))
        self.QUIT = Option("Quit", system.farewell, ("QUIT", "Q", "4"))
        self.OPTIONS = (self.PLAY, self.SETTINGS, self.CREDITS, self.QUIT)

    def __call__(self, *args, **kwargs):
        main_menu_ = MenuPattern(self.HEADER, self.OPTIONS)
        main_menu_.select_answer()


main_menu = MainMenu()


def game_func():
    game_intro.intro()
    main_menu()


game_func()
