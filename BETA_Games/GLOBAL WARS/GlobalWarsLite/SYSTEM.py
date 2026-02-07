from colorama import Fore, Style


class System:
    basic_income = 100_000
    moves_limit = 100
    move_energy = 1000

    def __init__(self):
        self.INPUT = self.communicate("<<<", "LIGHTWHITE_EX")
        self.coming_soon = lambda: print(self.communicate("COMING SOON...", "LIGHTWHITE_EX"))
        self.pass_func = lambda: None

    @staticmethod
    def communicate(text, color):
        return getattr(Fore, color) + text + Style.RESET_ALL


system = System()


class Error:
    def __init__(self, code: int, descr: str):
        self.code = code
        self.descr = descr

    def __call__(self):
        return system.communicate(f"ERROR{self.code}: {self.descr}", "LIGHTRED_EX")


error1 = Error(1, "Select one of the options shown above!")
error2 = Error(2, "Enter an integer!")
error3 = Error(3, "Enter total in the given range!")


class Menu:
    def __init__(self, header: str, options: tuple):
        self.header = header.upper()
        self.options = options

    def get_menu(self):
        print(system.communicate(f"[ {self.header} ]", "LIGHTRED_EX"))
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
