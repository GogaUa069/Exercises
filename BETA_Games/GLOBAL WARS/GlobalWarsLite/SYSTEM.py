from colorama import Fore, Style
from tqdm import tqdm
import time
import pyfiglet
import pygame

pygame.init()

class System:
    basic_income = 100_000
    moves_limit = 100
    move_energy = 1000

    def __init__(self):
        self.INPUT = self.communicate("<<< ", "LIGHTWHITE_EX")
        self.coming_soon = lambda: print(self.communicate("COMING SOON...", "LIGHTWHITE_EX"))
        self.pass_func = lambda: None

    @staticmethod
    def communicate(text, color):
        return getattr(Fore, color) + text + Style.RESET_ALL

    def get_ascii_text(self, text, color="LIGHTGREEN_EX", font="standard"):
        f = pyfiglet.Figlet(font=font)
        ascii_text = f.renderText(text)
        for line in ascii_text.splitlines():
            print(self.communicate(line, color))
            time.sleep(0.25)


system = System()


def play_soundtrack(path, is_infinite=False):
    pygame.mixer.music.load(path)
    if is_infinite:
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.play()


def stop_soundtrack():
    pygame.mixer.music.stop()


class Intro:

    @staticmethod
    def loading():
        with tqdm(total=100) as pbar:
            for i in range(100):
                pbar.set_description_str(system.communicate("LOADING", "LIGHTRED_EX"))
                pbar.update(1)
                time.sleep(0.04)

    @staticmethod
    def show_game_banner(banner: str):
        time.sleep(0.5)
        print(system.communicate("Welcome to:", "RED"))
        time.sleep(1.5)
        system.get_ascii_text(banner)
        time.sleep(1)

    def __call__(self):
        self.show_game_banner("Global wars: Frontline")
        self.loading()


game_intro = Intro()


class Error:
    def __init__(self, code: int, descr: str):
        self.code = code
        self.descr = descr

    def __call__(self):
        return system.communicate(f"ERROR{self.code}: {self.descr}", "LIGHTRED_EX")


error1 = Error(1, "Select one of the options shown above!")
...
error3 = Error(3, "Enter total in the given range!")


class Menu:
    def __init__(self, header: str, options: tuple, soundtrack=None, is_infinite=False):
        self.header = header.upper()
        self.options = options
        self.soundtrack = soundtrack
        self.is_infinite = is_infinite

    def get_menu(self):
        print(system.communicate(f"\n[ {self.header} ]", "LIGHTRED_EX"))
        for indx, option in enumerate(self.options, 1):
            if indx == len(self.options):
                option.name = f"\033[4m{option.name}\033[0m"
            print(system.communicate(f"{indx}. {option.name}", "GREEN"))

    def __check_answer(self, answer):
        for indx, option in enumerate(self.options, 1):
            if answer == str(indx):
                option()
                return
        print(error1())

    def __call__(self):
        if self.soundtrack is not None:
            play_soundtrack(self.soundtrack, self.is_infinite)
        answer = str()
        while answer != str(len(self.options)):
            self.get_menu()
            answer = input(system.INPUT)
            self.__check_answer(answer)


class Option:
    def __init__(self, name: str, func: ()):
        self.name = name.upper()
        self.func = func

    def __call__(self):
        self.func()
