from random import randint, sample, choice
import time
import sys
import os

from colorama import Fore, Style
import yaml


def __resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


yaml_path = __resource_path("record_results.yaml")


def communicate(text, color):
    return getattr(Fore, color) + text + Style.RESET_ALL


class RecordData:
    encoding = "utf-8"

    def __init__(self):
        with open(yaml_path, "r", encoding=self.encoding) as file:
            self.record_data = yaml.safe_load(file)
            self.the_best_time = self.record_data["record_time"]
            self.win_streak = self.record_data["win_streak"]

    def save_new_data(self, data):
        with open(yaml_path, "w", encoding=self.encoding) as file:
            yaml.dump(data, file, sort_keys=False)


record_data = RecordData()


class DigitsTournament:
    questions_amount = 10

    def __init__(self):
        self.digit_list = [randint(1, 100) for _ in range(self.questions_amount)]
        self.bad_answers_limit = 3
        self.good_answers_counter = self.bad_answers_counter = 0
        self.start_time = self.stop_time = 0
        self.round_time = self.average_time_for_answer = 0
        self.bad_answers_difference = self.time_difference = self.average_time_difference = 0

    @staticmethod
    def caution():
        print(communicate("UWAGA!", "LIGHTRED_EX"))
        print(communicate("Podstawowe wyniki zostały wybrane jako mój ostatni rekord.", "LIGHTRED_EX"))

    @staticmethod
    def get_correct_answer(n1, n2, operation):
        match operation:
            case "+":
                return n1 + n2
            case _:
                return n1 - n2

    def __get_time_in_seconds(self):
        return f"[{self.round_time} s]"

    @staticmethod
    def color_win_streak(win_streak):
        if win_streak == 0:
            return communicate(str(win_streak), "LIGHTRED_EX")
        else:
            return communicate(str(win_streak), "LIGHTGREEN_EX")

    @staticmethod
    def __set_num_colors(num):
        if num < 0:
            num = communicate(str(num), "LIGHTGREEN_EX")
        elif num == 0:
            num = communicate(str(num), "LIGHTYELLOW_EX")
        else:
            num = communicate("+" + str(num), "LIGHTRED_EX")
        return num

    def __validate_bad_answers_counter(self):
        if self.bad_answers_counter > self.bad_answers_limit:
            record_data.win_streak = 0
            print(communicate("\nRekord nie został zaliczony", "LIGHTRED_EX"))
            print(communicate(f"Limit błędów: {communicate(str(self.bad_answers_limit), "LIGHTWHITE_EX")}", "LIGHTRED_EX"))
            print(communicate(f"Zrobiono błędów: {communicate(str(self.bad_answers_counter), "LIGHTWHITE_EX")}", "LIGHTRED_EX"))
            print(communicate(f"Różnica: +{self.bad_answers_difference}", "LIGHTRED_EX"))
            return False
        else:
            record_data.win_streak += 1
            return True

    def is_saving_data(self, is_saving):
        if is_saving:
            new_data = {"record_time": self.round_time, "win_streak": record_data.win_streak}
        else:
            new_data = {"record_time": record_data.the_best_time, "win_streak": record_data.win_streak}
        record_data.save_new_data(new_data)

    def is_new_record(self):
        if self.round_time < record_data.the_best_time:
            print(communicate("Nowy rekord!", "LIGHTCYAN_EX"))
            print(communicate(f"Poprzedni rekord: {record_data.the_best_time}", "LIGHTCYAN_EX"))
            print(communicate(f"Różnica czasów: {self.__set_num_colors(self.difference_time)}", "LIGHTCYAN_EX"))
            self.is_saving_data(self.__validate_bad_answers_counter())
        else:
            record_data.win_streak = 0
            print(communicate(f"Rekord: {record_data.the_best_time}", "LIGHTCYAN_EX"))
            print(communicate(f"Różnica czasów: {self.__set_num_colors(self.difference_time)}", "LIGHTCYAN_EX"))
            self.is_saving_data(False)

    def results(self):
        print(communicate("\n\nWYNIKI:\n", "LIGHTWHITE_EX"))
        print(communicate(f"Punkty: {self.good_answers_counter}/{self.questions_amount}", "LIGHTWHITE_EX"))
        print(communicate(f"Czas: {self.__get_time_in_seconds()}\n", "LIGHTWHITE_EX"))
        self.is_new_record()
        print(communicate(f"\nSeria zwycięstw: {self.color_win_streak(record_data.win_streak)}\n", "LIGHTWHITE_EX"))

    def validate_answer(self, n1, n2, operation):
        is_bad = bad_counter = 0
        correct_answer = self.get_correct_answer(n1, n2, operation)
        while True:
            try:
                answer = int(input("<<< "))
                if answer == correct_answer:
                    print(communicate("Poprawna odpowiedź!\n", "LIGHTGREEN_EX"))
                    break
                else:
                    print(communicate("Błędna odpowiedź!\n", "LIGHTRED_EX"))
                    bad_counter += 1
                    if bad_counter > 1:
                        is_bad = True
                    if bad_counter == 3:
                        print(communicate(f"Poprawna odpowiedź: {communicate(correct_answer, "LIGHTWHITE_EX")}\n","LIGHTRED_EX"))
                        break
            except TypeError:
                print(communicate("BŁĄD: Wpisz liczbę!", "LIGHTRED_EX"))
        if not is_bad:
            self.good_answers_counter += 1
        else:
            self.bad_answers_counter += 1

    def set_timing_data(self, start_time_for_answer, stop_time_for_answer):
        time_for_answer = round(stop_time_for_answer - start_time_for_answer, 3)
        time_since_start = round(stop_time_for_answer - self.start_time, 3)

        print(communicate(f"Czas na odpowiedź: {time_for_answer}", "LIGHTWHITE_EX"))
        print(communicate(f"Czas od początku: {time_since_start}", "LIGHTWHITE_EX"))

    def get_digits(self):
        for indx in range(len(self.digit_list)):
            n1, n2 = sample(self.digit_list, k=2)
            operation = choice(["+", "-"])
            print(communicate(f"{indx+1}/{self.questions_amount}. {n1}{operation}{n2}=", "CYAN"))
            start_time_for_answer = time.time()
            self.validate_answer(n1, n2, operation)
            stop_time_for_answer = time.time()
            self.set_timing_data(start_time_for_answer, stop_time_for_answer)
            os.system("cls")

    def __call__(self):
        self.caution()
        input(communicate("\nNaciśnij ENTER, aby rozpocząć.", "LIGHTRED_EX"))

        self.start_time = time.time()
        self.get_digits()
        self.stop_time = time.time()

        self.round_time = round(self.stop_time - self.start_time, 3)
        self.difference_time = round(self.round_time - record_data.the_best_time, 3)
        self.bad_answers_difference = self.bad_answers_counter - self.bad_answers_limit

        self.results()

        input(communicate("Naciśnij ENTER, aby zakończyć.", "LIGHTRED_EX"))


digit_tournament = DigitsTournament()
digit_tournament()
