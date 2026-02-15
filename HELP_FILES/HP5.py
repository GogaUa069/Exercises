from random import shuffle
import time

from colorama import Fore, Style
import yaml


def communicate(text, color):
    return getattr(Fore, color) + text + Style.RESET_ALL


class Words:
    words = {"wygrywać": ("gewinnen", "gewonnen"), "mieć": ("haben", "gehabt"), "pochodić": ("kommen", "gekommen"),
         "biegać": ("laufen", "gelaufen"), "czytać": ("lesen", "gelesen"), "leżeć": ("liegen", "gelegen"),
         "musieć": ("mussen", "gemusst"), "spać": ("schlafen", "geschlafen"), "wisieć": ("hangen", "gehangen"),
         "lubić": ("mogen", "gemacht"), "iść": ("gehen", "gegangen"), "ładować": ("laden", "geladen"),
         "umieć": ("konnen", "gekonnt"), "trzymać": ("halten", "gehalten"), "brać": ("nehmen", "genommen"),
         "nazywać": ("nennen", "genannt"), "nazywać się": ("heissen", "geheissen"), "znać": ("kennen", "gekannt"),
         "pomagać": ("helfen", "geholfen"), "pisać": ("schreiben", "geschrieben"), "wołać": ("rufen", "gerufen"),
         "kroić": ("schneiden", "geschnitten")}

    def __init__(self):
        self.words = list(self.words.items())
        shuffle(self.words)
        self.words_len = len(self.words)


words = Words()


class RecordData:
    encoding = "utf-8"

    def __init__(self):
        with open("the_best_time.yaml", "r", encoding=self.encoding) as file:
            self.record_data = yaml.safe_load(file)
            self.answers_timing = self.record_data["answers_timing"]
            self.the_best_time = self.record_data["record_time"]

    def save_new_data(self, data):
        with open("the_best_time.yaml", "w", encoding=self.encoding) as file:
            yaml.dump(data, file)


record_data = RecordData()


class WordsChecker:
    def __init__(self):
        self.bad_answers_limit_for_record = 2.0
        self.good_answers_counter = self.bad_answers_counter = self.round_time = self.difference_time = self.bad_answers_difference = 0.0
        self.start_time = self.stop_time = 0
        self.current_answer_timing = list()

    @staticmethod
    def __set_num_colors(num):
        if num < 0:
            num = communicate(str(num), "LIGHTGREEN_EX")
        elif num == 0:
            num = communicate(str(num), "LIGHTYELLOW_EX")
        else:
            num = communicate("+" + str(num), "LIGHTRED_EX")
        return num

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
            print(communicate("Rekord nie został zaliczony", "LIGHTRED_EX"))
            print(communicate(f"Limit błędów: {communicate(self.bad_answers_limit_for_record, "LIGHTWHITE_EX")}", "LIGHTRED_EX"))
            print(communicate(f"Zrobiono błędów: {communicate(self.bad_answers_counter, "LIGHTWHITE_EX")}", "LIGHTRED_EX"))
            print(communicate(f"Różnica: +{self.bad_answers_difference}", "LIGHTRED_EX"))
            return False
        return True

    def is_saving_data(self):
        if self.__validate_bad_answers_counter():
            new_data = {"record_time": self.round_time, "answers_timing": self.current_answer_timing}
            record_data.save_new_data(new_data)

    def is_new_record(self):
        if self.round_time < record_data.the_best_time:
            print(communicate("Nowy rekord!", "LIGHTCYAN_EX"))
            print(communicate(f"Poprzedni rekord: {record_data.the_best_time}", "LIGHTCYAN_EX"))
            print(communicate(f"Różnica czasów: {self.__set_num_colors(self.difference_time)}", "LIGHTCYAN_EX"))
            self.is_saving_data()
        else:
            print(communicate(f"Rekord: {record_data.the_best_time}", "LIGHTCYAN_EX"))
            print(communicate(f"Różnica czasów: {self.__set_num_colors(self.difference_time)}", "LIGHTCYAN_EX"))

    def results(self):
        print(communicate("WYNIKI", "LIGHTWHITE_EX"))
        print(communicate(f"Punkty: {self.good_answers_counter}/{float(words.words_len)}", "LIGHTWHITE_EX"))
        print(communicate(f"Czas: {self.__get_time_in_seconds()} / {self.__get_time_in_minutes()}", "LIGHTWHITE_EX"))
        print(communicate(f"Błędów zrobiono: {self.bad_answers_counter}", "LIGHTWHITE_EX"))
        self.is_new_record()

    def validate_answer(self, word, part_order, part):
        is_bad = bad_counter = 0
        correct_answer = word[1][part_order]
        while True:
            answer = input(communicate(f"{part}: ({bad_counter+1}/3)", "LIGHTWHITE_EX"))
            if answer == correct_answer:
                print(communicate("Poprawna odpowiedź!", "LIGHTGREEN_EX"))
                break
            else:
                print(communicate("Błędna odpowiedź!", "LIGHTRED_EX"))
                bad_counter += 1
                if bad_counter > 1:
                    self.bad_answers_counter += 1
                    is_bad = True
                if bad_counter == 3:
                    print(communicate(f"Poprawna odpowiedź: {communicate(correct_answer, "LIGHTWHITE_EX")}", "LIGHTRED_EX"))
                    break
        if not is_bad:
            self.good_answers_counter += 0.5

    def set_timing_data(self, start_time_for_answer, stop_time_for_answer, order):
        time_for_answer = round(stop_time_for_answer - start_time_for_answer, 3)
        time_since_start = round(stop_time_for_answer - self.start_time, 3)
        difference_time_for_answer = self.__set_num_colors(round(time_for_answer - record_data.answers_timing[order]["time_for_answer"], 3))
        difference_time_since_start = self.__set_num_colors(round(time_since_start - record_data.answers_timing[order]["time_since_start"], 3))

        self.current_answer_timing.append({order: {"time_for_answer": time_for_answer, "time_since_start": time_since_start}})

        print(communicate(f"Czas na odpowiedź: {time_for_answer}", "LIGHTWHITE_EX"))
        print(communicate(f"Czas od początku: {time_since_start}", "LIGHTWHITE_EX"))
        print(communicate(f"Różnica z rekordowym czasem na odpowiedź: {difference_time_for_answer}", "LIGHTWHITE_EX"))
        print(communicate(f"Różnica z rekordowym czasem od początku: {difference_time_since_start}", "LIGHTWHITE_EX"))

    def get_words(self):
        for order, word in enumerate(words.words, 1):
            print(communicate(f"{order}/{words.words_len}. {word[0]}:", "CYAN"))
            start_time_for_answer = time.time()
            self.validate_answer(word, 0, "bezokolicznik")
            self.validate_answer(word, 1, "imiesłów")
            stop_time_for_answer = time.time()
            self.set_timing_data(start_time_for_answer, stop_time_for_answer, order)

    def __call__(self):
        input(communicate("Naciśnij ENTER, aby rozpocząć", "LIGHTRED_EX"))

        self.start_time = time.time()
        self.get_words()
        self.stop_time = time.time()

        self.round_time = round(self.stop_time - self.start_time, 3)
        self.difference_time = round(self.round_time - record_data.the_best_time, 3)
        self.bad_answers_difference = self.bad_answers_counter - self.bad_answers_limit_for_record

        self.results()


word_checker = WordsChecker()
word_checker()
