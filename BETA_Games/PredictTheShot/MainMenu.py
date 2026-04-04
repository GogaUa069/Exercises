from code import *


class Menu:
    def __init__(self, header, options):
        self.HEADER = header
        self.OPTIONS = options

    def show_menu(self):
        os.system("cls")
        print(system.communicate(f"\n[ {self.HEADER.upper()} ]", "LIGHTRED_EX"))
        for indx, option in enumerate(self.OPTIONS, 1):
            print(system.communicate(f"{indx}. {option.name.upper()}", "GREEN"))

    def check_answer(self, answer):
        for indx, option in enumerate(self.OPTIONS, 1):
            if answer.upper() in (option.name.upper(), str(indx)):
                option()
                return

    def __call__(self):
        answer = str()
        while answer != str(len(self.OPTIONS)):
            self.show_menu()
            answer = input(system.communicate("<<< ", "LIGHTWHITE_EX"))
            self.check_answer(answer)


class Option:
    def __init__(self, name, func):
        self.name = name
        self.func = func

    def __call__(self):
        self.func()


def tutorial():
    print(system.communicate("Press ENTER to continue", "LIGHTRED_EX"))
    input()
    print(system.communicate("Tutorial:", "LIGHTCYAN_EX"), end="")
    input()
    print(system.communicate("\n1.1 You have 4 options to choose: 'shot', 'load', 'block' and 'deflect'.", "LIGHTCYAN_EX"), end="")
    input()
    print(system.communicate("1.2 Shot (0 energy) - You shot at your enemy. If you both select shot, nothing will happen.", "LIGHTCYAN_EX"), end="")
    input()
    print(system.communicate("1.3 Load (0 energy) - You add 1 bullet. (MAX 6)", "LIGHTCYAN_EX"), end="")
    input()
    print(system.communicate("1.4 Block (2 energy) - You block one enemy bullet. (disables after move.)", "LIGHTCYAN_EX"), end="")
    input()
    print(system.communicate("1.5 Deflect (3 energy) - Enemy bullet deflects and hurts him. (disables after move.)", "LIGHTCYAN_EX"), end="")
    input()
    print(system.communicate("\n2.1 Tip #1: Use 'load' as a first move, your opponent does not have bullets.", "LIGHTCYAN_EX"), end="")
    input()
    print(system.communicate("2.2 Tip #2: If you will input 3 wrong answer you will get random option.", "LIGHTCYAN_EX"), end="")
    input()
    print(system.communicate("\nI think you are ready. Next tips will be in the future.", "LIGHTCYAN_EX"), end="")
    input()


def update_log():
    print()
    print("02.04.26. - v1.0 ALPHA")
    print("03.04.26. - v1.0 BETA, v1.1 BETA, v1.2 BETA, v2.0")
    print("04.04.26. - v2.1, v2.2, v2.2.1, v2.3")
    input()


def coming_soon():
    print(system.communicate("Coming soon...", "LIGHTWHITE_EX"))
    input()


pass_func = lambda: None

# SETTINGS:
tutorial_option = Option("tutorial", tutorial)
audio_option = Option("audio", coming_soon)
update_log_option = Option("update log", update_log)
credits_option = Option("credits", coming_soon)
from_settings_to_mm = Option("leave - main menu", pass_func)

settings_options = (tutorial_option, audio_option, update_log_option, credits_option, from_settings_to_mm)
settings_menu = Menu("settings", settings_options)

# MAIN MENU:
play_option = Option("play", game)
settings_option = Option("settings", settings_menu)
quit_option = Option("quit", pass_func)

mm = Menu("main menu", (play_option, settings_option, quit_option))
mm()
