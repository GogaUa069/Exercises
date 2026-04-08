#  I hope that this project will help me keep a proper diet before the summer holidays 2026 :) * 08.04.26 22:12

from datetime import date
from colorama import Fore, Style
import yaml


def communicate(text, color):
    return getattr(Fore, color) + text + Style.RESET_ALL


class Data:
    ENCODING = "utf-8"

    def __init__(self):
        self.DATA = dict()

    def load_data(self):
        with open("data.yaml", "r", encoding=self.ENCODING) as file:
            self.DATA = yaml.safe_load(file)

    def save_data(self):
        with open("data.yaml", "w", encoding=self.ENCODING) as file:
            yaml.safe_dump(self.DATA, file, sort_keys=False)


data = Data()
data.load_data()


class TimeControl:
    START_DATE = date(2026, 4, 9)
    HOLIDAYS_DATE = date(2026, 6, 27)

    def __init__(self):
        self.today = date.today()
        self.today_answer = None

    def set_day_streak(self):
        match self.today_answer:
            case 0:
                data.DATA["day_streak"] += 1
                data.DATA["days_attended"] += 1
            case 1:
                data.DATA["day_streak"] = 0
                data.DATA["days_missed"] += 1

    def set_days_before_holidays(self):
        data.DATA["days_before_holidays"] = (self.HOLIDAYS_DATE - self.today).days

    def set_needed_days(self):
        data.DATA["days_needed"] = (self.HOLIDAYS_DATE - self.START_DATE).days

    def set_today_answer(self):
        while True:
            print(communicate(f"({time_control.today}) Have you eaten sweets today?", "CYAN"))
            try:
                answer = int(input(communicate("<<< ", "LIGHTWHITE_EX")))
                if answer in (0, 1):
                    break
                else:
                    print(communicate("ERROR: Enter 1 or 0.", "LIGHTRED_EX"))
            except TypeError:
                print(communicate("ERROR: Enter digit", "LIGHTRED_EX"))
        self.today_answer = answer

    def set_data(self):
        self.set_day_streak()
        self.set_days_before_holidays()
        self.set_needed_days()
        data.save_data()

    def __str__(self):
        return communicate(f"\n*** DIET INFO ***\n"
                           f"- Days left: {data.DATA["days_before_holidays"]} / {data.DATA["days_needed"]}\n"
                           f"- Day streak: {data.DATA["day_streak"]}\n\n"
                           f"- Days attended: {data.DATA["days_attended"]}\n"
                           f"- Days missed: {data.DATA["days_missed"]}\n", "LIGHTWHITE_EX")

    def __call__(self):
        self.set_today_answer()
        self.set_data()
        print(self)
        input(communicate("[ENTER] to quit", "LIGHTRED_EX"))


time_control = TimeControl()
time_control()
