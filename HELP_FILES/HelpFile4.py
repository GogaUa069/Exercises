from colorama import Fore, Style
from random import shuffle
import time
import yaml

with open("../MyProjects/Learning/GermanLearning/the_best_time.yaml", "r", encoding="utf-8") as file:
    answer_timing = yaml.safe_load(file)

words = {"wygrywać": ("gewinnen", "gewonnen"), "mieć": ("haben", "gehabt"), "pochodić": ("kommen", "gekommen"),
         "biegać": ("laufen", "gelaufen"), "czytać": ("lesen", "gelesen"), "leżeć": ("liegen", "gelegen"),
         "musieć": ("mussen", "gemusst"), "spać": ("schlafen", "geschlafen"), "wisieć": ("hangen", "gehangen"),
         "lubić": ("mogen", "gemacht"), "iść": ("gehen", "gegangen"), "ładować": ("laden", "geladen"),
         "umieć": ("konnen", "gekonnt"), "trzymać": ("halten", "gehalten"), "brać": ("nehmen", "genommen"),
         "nazywać": ("nennen", "genannt"), "nazywać się": ("heissen", "geheissen"), "znać": ("kennen", "gekannt"),
         "pomagać": ("helfen", "geholfen"), "pisać": ("schreiben", "geschrieben"), "wołać": ("rufen", "gerufen"),
         "kroić": ("schneiden", "geschnitten")}

items = list(words.items())
shuffle(items)

good_answers_counter = bad_answers_counter = 0.0

input(Fore.LIGHTRED_EX + "Naciśnij ENTER, aby rozpociąć" + Style.RESET_ALL)

start = time.time()
last_answer_time = 0
answer_timing_list = list()

for indx, word in enumerate(items, 1):
    start_answer_time = time.time()
    bad_flag1 = bad_flag2 = False
    bad_counter1 = bad_counter2 = 0
    print(Fore.CYAN + f"\n{indx}/{len(words)}. {word[0]}:" + Style.RESET_ALL)

    while True:
        if bad_counter1 == 3:
            print(Fore.CYAN + f"Poprawna odpowiedź: {word[1][0]}\n" + Style.RESET_ALL)  # index
            break
        a1 = input(Fore.LIGHTWHITE_EX + f"Bezokolicznik ({bad_counter1+1}/3): " + Style.RESET_ALL).strip()  # word
        if a1 == word[1][0]:
            print(Fore.LIGHTGREEN_EX + "Poprawna odpowiedź!\n" + Style.RESET_ALL)
            break
        else:
            bad_counter1 += 1
            if bad_counter1 > 1:
                bad_answers_counter += 1
                bad_flag1 = True
            print(Fore.LIGHTRED_EX + "Błędna odpowiedź!\n" + Style.RESET_ALL)
    if not bad_flag1:
        good_answers_counter += 0.5
    while True:
        if bad_counter2 == 3:
            print(Fore.CYAN + f"Poprawna odpowiedź: {word[1][1]}" + Style.RESET_ALL)
            break
        a2 = input(Fore.LIGHTWHITE_EX + f"Imiesłów ({bad_counter2+1}/3): " + Style.RESET_ALL).strip()
        if a2 == word[1][1]:
            print(Fore.LIGHTGREEN_EX + "Poprawna odpowiedź!" + Style.RESET_ALL)
            break
        else:
            bad_counter2 += 1
            if bad_counter2 > 1:
                bad_answers_counter += 1
                bad_flag2 = True
            print(Fore.LIGHTRED_EX + "Błędna odpowiedź!\n" + Style.RESET_ALL)
    if not bad_flag2:
        good_answers_counter += 0.5
    stop_answer_time = time.time()
    record_sub_of_answer = round(answer_timing["times_for_answer"][indx]["time_for_answer"]+start_answer_time-stop_answer_time, 3)
    if record_sub_of_answer <= 0:
        record_sub_of_answer = Fore.LIGHTRED_EX + "+" + str(abs(record_sub_of_answer)) + Style.RESET_ALL
    else:
        record_sub_of_answer = Fore.LIGHTGREEN_EX + "-" + str(record_sub_of_answer) + Style.RESET_ALL
    last_answer_time = round(stop_answer_time - start_answer_time, 3)
    time_for_answer = round(stop_answer_time - start, 3)
    record_sub_since_start = round(stop_answer_time - answer_timing["times_for_answer"][indx]["time_since_start"], 3)
    print(f"Czas na odpowiedź: {last_answer_time}")
    print(f"Czas od początku: {time_for_answer}")
    print(f"Różnica z rekordowym czasem odpowiedzi: {record_sub_of_answer}")
    print(f"Różnica z rekordowym czasem od początku: {record_sub_since_start}")

stop = time.time()

time_count = round(stop-start, 3)

minutes = (time_count % 3600) // 60
seconds = time_count % 60
milliseconds = round(time_count % 1, 3)

minutes = str(int(minutes)).rjust(2, "0")
seconds = str(int(seconds)).rjust(2, "0")
milliseconds = str(milliseconds).split(".")[1]
if  milliseconds[0] != 0:
    milliseconds = milliseconds.ljust(3, "0")
else:
    milliseconds = milliseconds.rjust(3, "0")

bad_answers_limit = 2.0

print(Fore.LIGHTWHITE_EX + "\nWYNIKI:\n" + Style.RESET_ALL)

print(Fore.LIGHTWHITE_EX + f"Punkty: {good_answers_counter} / {len(words)}.0\n"
                           f"Czas: [{round(time_count, 3)} s] / [{minutes}:{seconds}.{milliseconds} min]" + Style.RESET_ALL)

with open("../MyProjects/Learning/GermanLearning/the_best_time.yaml", "r", encoding="utf-8") as file:
    data = yaml.safe_load(file)

if time_count >= data["the_best_time"]:
    print(Fore.LIGHTCYAN_EX + f"Rekord: {data["the_best_time"]}\n"
                      f"Różnica: +{time_count-data["the_best_time"]}" + Style.RESET_ALL)

if time_count < data["the_best_time"]:
    print(Fore.LIGHTCYAN_EX + f"To jest twój najlepszy czas! Poprzedni rekord: {data["the_best_time"]}\n"
                              f"Różnica: -{data["the_best_time"]-time_count} s" + Style.RESET_ALL)
    if bad_answers_counter <= bad_answers_limit:
        data["the_best_time"] = time_count
        with open("../MyProjects/Learning/GermanLearning/the_best_time.yaml", "w", encoding="utf-8") as file:
            yaml.dump(data, file)
    else:
        print(Fore.LIGHTRED_EX + f"Rekord się nie liczy:\n"
                                 f"Limit błędów: {bad_answers_limit}\n"
                                 f"Zrobiono błędów: {bad_answers_counter}\n"
                                 f"Różnica: {bad_answers_counter-bad_answers_limit}" + Style.RESET_ALL)
