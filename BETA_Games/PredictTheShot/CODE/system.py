import os
import yaml
from colorama import Fore, Style

version = "v4.3.0"


class System:
    __instance = None

    MAX_BULLETS = 6
    MAX_ENERGY = 6
    MAX_LIVES = 3

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        raise RuntimeError("Singleton instance already exists.")

    def __init__(self):
        self.pass_func = lambda: None

        self.INPUT = self.communicate("<<< ", "LIGHTWHITE_EX")
        self.TUTORIAL = (self.communicate("[ENTER] to continue", "LIGHTRED_EX"),
                         self.communicate("\nTutorial:", "LIGHTCYAN_EX"),
                         self.communicate("\n1.1 You have 4 options to choose: 'shot', 'load', 'block' and 'deflect'.", "LIGHTCYAN_EX"),
                         self.communicate("1.2 Shot (0 energy) - You shot at your enemy. If you both select shot, nothing will happen.", "LIGHTCYAN_EX"),
                         self.communicate("1.3 Load (0 energy) - You add 1 bullet. (MAX 6)", "LIGHTCYAN_EX"),
                         self.communicate("1.4 Block (2 energy) - You block one enemy bullet. (disables after move.)", "LIGHTCYAN_EX"),
                         self.communicate("1.5 Deflect (3 energy) - Enemy bullet deflects and hurts him. (disables after move.)", "LIGHTCYAN_EX"),
                         self.communicate("\n2.1 Tip #1: Use 'load' as a first move, your opponent does not have bullets.", "LIGHTCYAN_EX"),
                         self.communicate("\nI think you are ready. Next tips will be in the future.", "LIGHTCYAN_EX"))

    @staticmethod
    def communicate(text: str, color: str) -> str:
        return getattr(Fore, color) + text + Style.RESET_ALL

    @staticmethod
    def clear_console():
        os.system("cls")

    def coming_soon(self):
        print(self.communicate("Coming soon...", "LIGHTWHITE_EX"))
        input()

    def error(self, text: str):
        print(self.communicate(f"ERROR: {text}", "LIGHTRED_EX"))

    def get_tutorial(self):
        for row in self.TUTORIAL:
            print(row, end="")
            input()


system = System()


class GUIOption:
    def __init__(self, name: str, func: ()):
        self.NAME = name.upper()
        self.FUNC = func

    def __call__(self):
        self.FUNC()


class Menu:
    def __init__(self, header: str, options: tuple):
        self.HEADER = header.upper()
        self.OPTIONS = options

    def show_menu(self):
        system.clear_console()
        print(system.communicate(f"\n[ {self.HEADER} ] [{version}]", "LIGHTRED_EX"))
        for index, option in enumerate(self.OPTIONS, 1):
            print(system.communicate(f"{index}. {option.NAME}", "GREEN"))

    def __check_answer(self, answer):
        for index, option in enumerate(self.OPTIONS, 1):
            if answer in (option.NAME, str(index)):
                option()
                return
        # system.error("Select one of the options shown above!")

    def __call__(self):
        answer = None
        while answer not in (str(len(self.OPTIONS)), self.OPTIONS[-1].NAME):
            self.show_menu()
            answer = input(system.INPUT).upper()
            self.__check_answer(answer)


class DataRemote:
    def __init__(self):
        self.DATA = None
        self.is_victory = None
        self.lives = self.moves = 0
        self.local_options_rate = dict().fromkeys(("shot", "load", "block", "deflect"), 0)
        self.local_options_utility = dict().fromkeys(("shot", "load", "block", "deflect"), 0)

    def load_data(self):
        with open("../UTILS/data.yaml", "r", encoding="utf-8") as file:
            self.DATA = yaml.safe_load(file)

    def set_params(self):
        self.DATA["all_games"] += 1

        match self.is_victory:
            case True:
                self.DATA["victories"] += 1
                self.DATA["win_streak"] += 1
                self.DATA["defeat_streak"] = 0
            case False:
                self.DATA["defeats"] += 1
                self.DATA["win_streak"] = 0
                self.DATA["defeat_streak"] += 1

        self.DATA["average_lives"]["all"] += 1
        self.DATA["average_lives"]["lives"] += self.lives
        self.DATA["average_lives"]["average"] = round(self.DATA["average_lives"]["lives"] / self.DATA["average_lives"]["all"], 3)

        self.DATA["average_moves"]["all"] += 1
        self.DATA["average_moves"]["moves"] += self.moves
        self.DATA["average_moves"]["average"] = round(self.DATA["average_moves"]["moves"] / self.DATA["average_moves"]["all"], 3)

        self.DATA["win_rate"] = round(self.DATA["victories"] / self.DATA["all_games"], 3) * 100

        self.DATA["options_rate"]["all"] += self.moves

        self.DATA["options_rate"]["shot"]["normal"] += self.local_options_rate["shot"]
        self.DATA["options_rate"]["load"]["normal"] += self.local_options_rate["load"]
        self.DATA["options_rate"]["block"]["normal"] += self.local_options_rate["block"]
        self.DATA["options_rate"]["deflect"]["normal"] += self.local_options_rate["deflect"]

        self.DATA["options_rate"]["shot"]["percent"] = round(self.DATA["options_rate"]["shot"]["normal"] / self.DATA["options_rate"]["all"] * 100, 3)
        self.DATA["options_rate"]["load"]["percent"] = round(self.DATA["options_rate"]["load"]["normal"] / self.DATA["options_rate"]["all"] * 100, 3)
        self.DATA["options_rate"]["block"]["percent"] = round(self.DATA["options_rate"]["block"]["normal"] / self.DATA["options_rate"]["all"] * 100, 3)
        self.DATA["options_rate"]["deflect"]["percent"] = round(self.DATA["options_rate"]["deflect"]["normal"] / self.DATA["options_rate"]["all"] * 100, 3)

        self.DATA["options_rate"]["shot"]["useful"] += self.local_options_utility["shot"]
        self.DATA["options_rate"]["load"]["useful"] += self.local_options_utility["load"]
        self.DATA["options_rate"]["block"]["useful"] += self.local_options_utility["block"]
        self.DATA["options_rate"]["deflect"]["useful"] += self.local_options_utility["deflect"]

        if self.DATA["options_rate"]["shot"]["normal"] != 0:
            self.DATA["options_rate"]["shot"]["useful_percent"] = round(self.DATA["options_rate"]["shot"]["useful"] / self.DATA["options_rate"]["shot"]["normal"] * 100, 3)
        if self.DATA["options_rate"]["load"]["normal"] != 0:
            self.DATA["options_rate"]["load"]["useful_percent"] = round(self.DATA["options_rate"]["load"]["useful"] / self.DATA["options_rate"]["load"]["normal"] * 100, 3)
        if self.DATA["options_rate"]["block"]["normal"] != 0:
            self.DATA["options_rate"]["block"]["useful_percent"] = round(self.DATA["options_rate"]["block"]["useful"] / self.DATA["options_rate"]["block"]["normal"] * 100, 3)
        if self.DATA["options_rate"]["deflect"]["normal"] != 0:
            self.DATA["options_rate"]["deflect"]["useful_percent"] = round(self.DATA["options_rate"]["deflect"]["useful"] / self.DATA["options_rate"]["deflect"]["normal"] * 100, 3)

    def save_data(self):
        with open("../UTILS/data.yaml", "w", encoding="utf-8") as file:
            yaml.safe_dump(self.DATA, file, sort_keys=False)

    def __str__(self):
        return (f"\n*** ACCOUNT INFO ***\n\n"
              f"- Games played: {self.DATA["all_games"]}\n"
              f"- Win rate: {self.DATA["win_rate"]}%\n\n"
              f"- Victories: {self.DATA["victories"]}\n"
              f"- Defeats: {self.DATA["defeats"]}\n\n"
              f"- Win streak: {self.DATA["win_streak"]}\n"
              f"- Lose streak: {self.DATA["defeat_streak"]}\n\n"
              f"- Average lives per game: {self.DATA["average_lives"]["average"]}\n"
              f"- Average moves per game: {self.DATA["average_moves"]["average"]}\n\n"
              f"- Action distribution:\n"
              f"    - Total moves: {self.DATA["options_rate"]["all"]}\n"
              f"    - SHOT: {self.DATA["options_rate"]["shot"]["percent"]}% ({self.DATA["options_rate"]["shot"]["normal"]}) (utility: {self.DATA["options_rate"]["shot"]["useful_percent"]}%)\n"
              f"    - LOAD: {self.DATA["options_rate"]["load"]["percent"]}% ({self.DATA["options_rate"]["load"]["normal"]}) (utility: {self.DATA["options_rate"]["load"]["useful_percent"]}%)\n"
              f"    - BLOCK: {self.DATA["options_rate"]["block"]["percent"]}% ({self.DATA["options_rate"]["block"]["normal"]}) (utility: {self.DATA["options_rate"]["block"]["useful_percent"]}%)\n"
              f"    - DEFLECT: {self.DATA["options_rate"]["deflect"]["percent"]}% ({self.DATA["options_rate"]["deflect"]["normal"]}) (utility: {self.DATA["options_rate"]["deflect"]["useful_percent"]}%)\n")

    def __call__(self):
        self.load_data()
        self.set_params()
        self.save_data()

    def get_account_info(self):
        self()
        print(self)
        input(system.communicate("[ENTER] to continue", "LIGHTRED_EX"))


data_remote = DataRemote()
