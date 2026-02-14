from colorama import Fore, Style
from random import shuffle
import time
import yaml

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

for indx, word in enumerate(items, 1):
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

with open("the_best_time.yaml", "r", encoding="utf-8") as file:
    data = yaml.safe_load(file)

if time_count >= data["the_best_time"]:
    print(Fore.LIGHTCYAN_EX + f"Rekord: {data["the_best_time"]}\n"
                      f"Różnica: +{time_count-data["the_best_time"]}" + Style.RESET_ALL)

if time_count < data["the_best_time"]:
    print(Fore.LIGHTCYAN_EX + f"To jest twój najlepszy czas! Poprzedni rekord: {data["the_best_time"]}\n"
                              f"Różnica: -{data["the_best_time"]-time_count} s" + Style.RESET_ALL)
    if bad_answers_counter <= bad_answers_limit:
        data["the_best_time"] = time_count
        with open("the_best_time.yaml", "w", encoding="utf-8") as file:
            yaml.dump(data, file)
    else:
        print(Fore.LIGHTRED_EX + f"Rekord się nie liczy:\n"
                                 f"Limit błędów: {bad_answers_limit}\n"
                                 f"Zrobiono błędów: {bad_answers_counter}\n"
                                 f"Różnica: {bad_answers_counter-bad_answers_limit}" + Style.RESET_ALL)
