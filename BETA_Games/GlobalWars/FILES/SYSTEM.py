# 2.1

from colorama import Fore, Style


class System:
    def __init__(self):
        self.INPUT = self.communicate("<<< ", "LIGHTWHITE_EX")
        self.pass_func = lambda: None
        self.coming_soon = lambda: print(self.communicate("COMING SOON...", "LIGHTWHITE_EX"))

    @staticmethod
    def communicate(text, color, is_underlined=False):
        text = getattr(Fore, color) + text + Style.RESET_ALL
        text = "\033[4m" + text + "\033[0m" if is_underlined else text
        return text

    class Menu:
        def __init__(self, header, options):
            self.HEADER = header.upper()
            self.OPTIONS = options

        def get_menu(self):
            print(system.communicate(f"\n[ {self.HEADER} ]", "LIGHTRED_EX"))
            for indx, option in enumerate(self.OPTIONS, 1):
                print(system.communicate(f"{indx}. {option.NAME}", "GREEN"))

        def _check_answer(self, answer):
            for indx, option in enumerate(self.OPTIONS, 1):
                if answer.upper() in (option.NAME.upper(), str(indx)):
                    print()
                    option()
                    return
            print(system.communicate("ERROR: Select one of the options shown above!", "LIGHTRED_EX"))

        def __call__(self):
            answer = str()
            while answer != str(len(self.OPTIONS)):
                self.get_menu()
                answer = input(system.INPUT)
                self._check_answer(answer)

    class Option:
        def __init__(self, name, func):
            self.NAME = name.upper()
            self.FUNC = func

        def __call__(self):
            self.FUNC()


system = System()
