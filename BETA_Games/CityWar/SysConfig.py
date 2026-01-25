from colorama import Fore, Style


class SysConfig:
    def __init__(self):
        self.INPUT = self.communicate("<<< ", "LIGHTWHITE_EX")

    @staticmethod
    def communicate(text, color):
        return getattr(Fore, color) + text + Style.RESET_ALL

    @staticmethod
    def underlined_text(text):
        return "\033[4m" + text + "\033[0m"

    class Menu:
        def __init__(self, header, options):
            self.HEADER = header
            self.OPTIONS = options

        def get_menu(self):
            print(system.communicate(f"\n[ {self.HEADER} ]", "LIGHTRED_EX"))
            for indx, option in enumerate(self.OPTIONS, 1):
                print(system.communicate(f"{indx}. {option.NAME}", "GREEN"))

        def _check_answer(self, answer):
            for indx, option in enumerate(self.OPTIONS, 1):
                if answer.upper() in (option.NAME.upper(), str(indx)):
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
            self.NAME = name
            self.FUNC = func

        def __call__(self):
            self.FUNC()


system = SysConfig()
