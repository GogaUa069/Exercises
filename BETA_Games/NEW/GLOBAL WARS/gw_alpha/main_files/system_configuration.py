from colorama import Fore, Style
import time
import pyfiglet


class Data:
    def __init__(self):
        self.moves_left = self.max_moves = 100
        self.basic_income = 100000
        self.energy_per_move = 1000


data = Data()


class System:
    def __init__(self):
        self.INPUT = self.communicate("<<< ", "LIGHTWHITE_EX")
        self.coming_soon = lambda: print(self.communicate("COMING SOON...", "LIGHTWHITE_EX"))
        self.pass_func = lambda: None

    @staticmethod
    def communicate(text, color):
        return getattr(Fore, color) + text + Style.RESET_ALL

    def __get_ascii_text(self, text, color="LIGHTGREEN_EX", font="standard"):
        f = pyfiglet.Figlet(font=font)
        ascii_text = f.renderText(text)
        return self.communicate(ascii_text, color)

    def get_banner(self, banner):
        ascii_banner = self.__get_ascii_text(banner)
        for line in ascii_banner.splitlines():
            print(line)
            time.sleep(0.21)


system = System()


class Menu:
    def __init__(self, header, options):
        self.HEADER = header.upper()
        self.OPTIONS = options

    def get_menu(self):
        print(system.communicate(f"\n[ {self.HEADER} ]", "LIGHTRED_EX"))
        for indx, option in enumerate(self.OPTIONS, 1):
            if indx == len(self.OPTIONS):
                option.NAME = f"\033[4m{option.NAME}\033[0m"
            print(system.communicate(f"{indx}. {option.NAME}", "GREEN"))

    def __check_answer(self, answer):
        for indx, option in enumerate(self.OPTIONS, 1):
            if answer == str(indx):
                option()
                return
        print(system.communicate("ERROR: Select one of the options shown above!", "LIGHTRED_EX"))

    def __call__(self):
        answer = str()
        while answer != str(len(self.OPTIONS)):
            self.get_menu()
            answer = input(system.INPUT)
            self.__check_answer(answer)


class Option:
    def __init__(self, name, func):
        self.NAME = name.upper()
        self.FUNC = func

    def __call__(self):
        self.FUNC()
