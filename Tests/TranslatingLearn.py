#  It's for GermanWordsBeta.py
#  For translating words

from colorama import Fore, Style
from random import choice

monologues = ["Dobrze!", "Dobra odpowiedź!", "Świetnie!", "Co za geniusz!"]  # AFTER COPYING DELETE WITH IMPORT


class ExampleImperative:
    def __init__(self):
        self.__forms = ["Tłumaczenie", "Du", "Wir", "Ihr", "sie/Sie"]
        self.__examples = {"gotować": ["kochen", "koch(e)", "kochen wir", "kocht", "kochen Sie"],
                           "pracować": ["arbeiten", "arbeite", "arbeiten wir", "arbeitet", "arbeiten Sie"],
                           "sądzić": ["finden", "finde", "finder wir", "findet", "finden Sie"],
                           "czytać": ["lesen", "lies", "lesen wir", "lest", "lesen Sie"],
                           "mówić": ["sprechen", "sprich", "sprechen wir", "sprecht", "sprechen Sie"],
                           "pomagać": ["helfen", "hilf", "helfen wir", "helft", "helfen Sie"],
                           "spotykać": ["treffen", "triff", "treffen wir", "trefft", "treffen Sie"],
                           "jechac": ["fahren", "fahr(e)", "fahren wir", "fahrt", "fahren Sie"],
                           "biegać": ["laufen", "lauf(e)", "laufen wir", "lauft", "laufen Sie"],
                           "zasypiać": ["einschlafen", "schalf(e) ein", "schalfen wir ein", "schalft ein",
                                        "schalfen Sie ein"],
                           "myć": ["waschen", "wasch(e)", "waschen wir", "wascht", "waschen Sie"]}

    def get_words(self):
        good_answers = 0
        counter = 0
        for word in self.__examples:
            second_counter = 0  # Add it after
            bad_counter = 0
            counter += 1
            while True:
                answer = input(f"{counter}/{len(self.__examples)}. Przetłumacz {word.upper()} - ")
                if answer == self.__examples[word][0]:
                    print(Fore.GREEN + f"{choice(monologues)}\n" + Style.RESET_ALL)
                    if bad_counter == 0:
                        good_answers += 1
                    break
                else:
                    print(Fore.RED + "Źle!\n" + Style.RESET_ALL)
                    bad_counter += 1
                    if bad_counter == 3:
                        print(Fore.RED + f"Przecież to jest {self.__examples[word][0].upper()}\n" + Style.RESET_ALL)
                        break
        print(f"Masz {Fore.RED + f"{good_answers}/{len(self.__examples)}" + Style.RESET_ALL} punktów!")


my_example = ExampleImperative()
my_example.get_words()
