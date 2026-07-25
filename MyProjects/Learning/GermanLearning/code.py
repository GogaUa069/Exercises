# v 3.3.3

from random import shuffle
import time
import sys
import os

from colorama import Fore, Style
import yaml

words_dict = {
    "obcas": ("der Absatz", "die Absatze"),
    "garnitur": ("der Anzug", "die Anzuge"),
    "bluzka (damska)": ("die Bluse", "die Blusen"),
    "okulary": ("die Brille", "die Brillen"),
    "garderoba, odzież": ("die Garderobe", ""),
    "naszyjnik": ("die Halskette", "die Halsketten"),
    "rękawiczka": ("der Handschuh", "die Handschuhe"),
    "koszula": ("das Hemd", "die Hemden"),
    "spodnie": ("die Hose", "die Hosen"),
    "kapelusz": ("der Hut", "die Hute"),
    "kurtka": ("die Jacke", "die Jacken"),
    "dżinsy": ("die Jeans", ""),
    "sukienka": ("das Kleid", "die Kleider"),
    "odzież, ubrania": ("die Kleidung", ""),
    "element odzieży": ("das Kleidungsstuck", "die Kleidungsstucke"),
    "krawat": ("die Krawatte", "die Krawatten"),
    "płaszcz": ("der Mantel", "die Mantel"),
    "czapka": ("die Mutze", "die Mutzen"),
    "sweter": ("der Pullover", "die Pullovers"),
    "spódnica": ("der Rock", "die Rocke"),
    "szalik": ("der Schal", "die Schals"),
    "but": ("der Schuh", "die Schuhe"),
    "skarpetka": ("die Socke", "die Socken"),
    "dres": ("der Sportanzug", "die Sportanzuge"),
    "rajstopy": ("die Strumpfhose", "die Strumpfhosen"),
    "bluza": ("das Sweatshirt", "die Sweatshirts"),
    "torebka": ("die Tasche", "die Taschen"),
    "koszulka": ("das T-Shirt", "die T-Shirts"),
    "kamizelka": ("die Weste", "die Westen")}



def __resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(os.path.dirname(sys._MEIPASS), relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


yaml_path = __resource_path("the_best_time.yaml")


def communicate(text, color):
    return getattr(Fore, color) + text + Style.RESET_ALL


class Words:
    words = words_dict

    def __init__(self):
        self.words = list(self.words.items())
        shuffle(self.words)
        self.words_len = len(self.words)


words = Words()


class RecordData:
    encoding = "utf-8"

    def __init__(self):
        with open(yaml_path, "r", encoding=self.encoding) as file:
            self.record_data = yaml.safe_load(file)
            self.answers_timing = self.record_data["answers_timing"]
            self.the_best_time = self.record_data["record_time"]
            self.win_streak = self.record_data["win_streak"]
            self.average_time_for_answer = self.record_data["average_time_for_answer"]

    def save_new_data(self, data):
        with open(yaml_path, "w", encoding=self.encoding) as file:
            yaml.dump(data, file, sort_keys=False)


record_data = RecordData()


class WordsChecker:
    def __init__(self):
        self.bad_answers_limit_for_record = 2
        self.good_answers_counter = self.round_time = self.difference_time = self.average_time_difference = 0.0
        self.start_time = self.stop_time = self.average_time_for_answer = self.bad_answers_counter = self.bad_answers_difference = 0
        self.current_answer_timing = dict()

    @staticmethod
    def caution():
        print(communicate("UWAGA!", "LIGHTRED_EX"))
        print(communicate("- Podstawowe wyniki zostały wybrane jako mój ostatni rekord.", "LIGHTRED_EX"))
        print(communicate("- Niektóre znaki diakrytyczne zostały zmienione dla wygody: ü - u; ä - a; ö - o; ß - ss\n", "LIGHTRED_EX"))

    @staticmethod
    def __set_num_colors(num):
        if num < 0:
            num = communicate(str(num), "LIGHTGREEN_EX")
        elif num == 0:
            num = communicate(str(num), "LIGHTYELLOW_EX")
        else:
            num = communicate("+" + str(num), "LIGHTRED_EX")
        return num

    @staticmethod
    def color_win_streak(win_streak):
        if win_streak == 0:
            return communicate(str(win_streak), "LIGHTRED_EX")
        else:
            return communicate(str(win_streak), "LIGHTGREEN_EX")

    def set_average_time_for_answer(self):
        timings = list()
        for timing in self.current_answer_timing.items():
            timings.append(timing[1]["time_for_answer"])
        self.average_time_for_answer = round(sum(timings) / len(timings), 3)
        self.average_time_difference = round(self.average_time_for_answer - record_data.average_time_for_answer, 3)

    def __get_time_in_minutes(self):
        minutes = (self.round_time % 3600) // 60
        seconds = self.round_time % 60
        milliseconds = round(self.round_time % 1, 3)

        minutes = str(int(minutes)).rjust(2, "0")
        seconds = str(int(seconds)).rjust(2, "0")
        milliseconds = str(milliseconds).split(".")[1]
        if milliseconds[0] != 0:
            milliseconds = milliseconds.ljust(3, "0")
        else:
            milliseconds = milliseconds.rjust(3, "0")

        return f"[{minutes}:{seconds}.{milliseconds} min]"

    def __get_time_in_seconds(self):
        return f"[{self.round_time} s]"

    def __validate_bad_answers_counter(self):
        if self.bad_answers_counter > self.bad_answers_limit_for_record:
            record_data.win_streak = 0
            print(communicate("\nRekord nie został zaliczony", "LIGHTRED_EX"))
            print(communicate(f"Limit błędów: {communicate(str(self.bad_answers_limit_for_record), "LIGHTWHITE_EX")}", "LIGHTRED_EX"))
            print(communicate(f"Zrobiono błędów: {communicate(str(self.bad_answers_counter), "LIGHTWHITE_EX")}", "LIGHTRED_EX"))
            print(communicate(f"Różnica: +{self.bad_answers_difference}", "LIGHTRED_EX"))
            return False
        else:
            record_data.win_streak += 1
            return True

    def is_saving_data(self, is_saving):
        if is_saving:
            new_data = {"average_time_for_answer": self.average_time_for_answer, "win_streak": record_data.win_streak, "record_time": self.round_time, "answers_timing": self.current_answer_timing}
        else:
            new_data = {"average_time_for_answer": record_data.average_time_for_answer, "win_streak": record_data.win_streak, "record_time": record_data.the_best_time, "answers_timing": record_data.answers_timing}
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
        print(communicate(f"Punkty: {self.good_answers_counter}/{float(words.words_len)} / {round(self.good_answers_counter/words.words_len*100, 2)}%", "LIGHTWHITE_EX"))
        print(communicate(f"Czas: {self.__get_time_in_seconds()} / {self.__get_time_in_minutes()}\n", "LIGHTWHITE_EX"))
        self.is_new_record()
        print(communicate(f"\nŚredni czas na odpowiedź: {self.average_time_for_answer}", "LIGHTWHITE_EX"))
        print(communicate(f"Różnica średnich czasów: {self.__set_num_colors(self.average_time_difference)}", "LIGHTWHITE_EX"))
        print(communicate(f"\nSeria zwycięstw: {self.color_win_streak(record_data.win_streak)}\n", "LIGHTWHITE_EX"))

    def validate_answer(self, word, part_order, part):
        is_bad = bad_counter = 0
        correct_answer = word[1][part_order]
        while True:
            answer = input(communicate(f"{part} ({bad_counter+1}/3): ", "LIGHTWHITE_EX"))
            if answer == correct_answer:
                print(communicate("Poprawna odpowiedź!\n", "LIGHTGREEN_EX"))
                break
            else:
                print(communicate("Błędna odpowiedź!\n", "LIGHTRED_EX"))
                bad_counter += 1
                if bad_counter > 1:
                    is_bad = True
                if bad_counter == 3:
                    print(communicate(f"Poprawna odpowiedź: {communicate(correct_answer, "LIGHTWHITE_EX")}\n", "LIGHTRED_EX"))
                    break
        if not is_bad:
            self.good_answers_counter += 0.5
        else:
            self.bad_answers_counter += 1

    def set_timing_data(self, start_time_for_answer, stop_time_for_answer, order):
        time_for_answer = round(stop_time_for_answer - start_time_for_answer, 3)
        time_since_start = round(stop_time_for_answer - self.start_time, 3)
        difference_time_for_answer = self.__set_num_colors(round(time_for_answer - record_data.answers_timing[order]["time_for_answer"], 3))
        difference_time_since_start = self.__set_num_colors(round(time_since_start - record_data.answers_timing[order]["time_since_start"], 3))

        self.current_answer_timing[order] = {"time_for_answer": time_for_answer, "time_since_start": time_since_start}

        print(communicate(f"Czas na odpowiedź: {time_for_answer}", "LIGHTWHITE_EX"))
        print(communicate(f"Czas od początku: {time_since_start}", "LIGHTWHITE_EX"))
        print(communicate(f"Różnica z rekordowym czasem na odpowiedź: {difference_time_for_answer}", "LIGHTWHITE_EX"))
        print(communicate(f"Różnica z rekordowym czasem od początku: {difference_time_since_start}", "LIGHTWHITE_EX"))

    def get_words(self):
        for order, word in enumerate(words.words, 1):
            print(communicate(f"\n{order}/{words.words_len}. {word[0]}:", "CYAN"))
            start_time_for_answer = time.time()
            self.validate_answer(word, 0, "liczba pojedyńcza")
            self.validate_answer(word, 1, "liczba mnoga")
            stop_time_for_answer = time.time()
            self.set_timing_data(start_time_for_answer, stop_time_for_answer, order)

    def __call__(self):
        self.caution()

        input(communicate("Naciśnij ENTER, aby rozpocząć.", "LIGHTRED_EX"))

        self.start_time = time.time()
        self.get_words()
        self.stop_time = time.time()

        self.round_time = round(self.stop_time - self.start_time, 3)
        self.difference_time = round(self.round_time - record_data.the_best_time, 3)
        self.bad_answers_difference = self.bad_answers_counter - self.bad_answers_limit_for_record

        self.set_average_time_for_answer()
        self.results()

        input(communicate("Naciśnij ENTER, aby zakończyć.", "LIGHTRED_EX"))


word_checker = WordsChecker()
word_checker()
