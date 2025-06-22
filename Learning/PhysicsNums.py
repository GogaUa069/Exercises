from random import choice, shuffle
from time import sleep
from colorama import Fore, Style

monologues = ["Dobrze!", "Dobra odpowiedź!", "Swietnie", "Co za geniusz!"]

density_mean = {"gęstość": "d", "objętość": "V", "masa": "m"}
density = {"d": "m/V", "V": "m/d", "m": "d*V"}
values = {"g/cm → kg/m": "razy 1000", "g/cm → kg/dm": "wartość się nie zmienia", "g/cm → g/dm": "razy 1000",
          "kg/m → g/cm": "podzielić na 1000", "kg/m → kg/dm": "podzielić na 1000",
          "kg/m → g/dm": "wartość się nie zmienia"}


class MeaningsChecker:

    @classmethod
    def value_getter(cls, glossary):
        good_answers = 0
        word_num = 0
        names = list(glossary.keys())
        shuffle(names)
        length = len(glossary)

        for value in names:
            word_num += 1
            bad_answers = 0
            while True:
                answer = input(f"\n{word_num}/{length}. {value} - ")
                if answer == glossary[value]:
                    print(Fore.GREEN + choice(monologues) + Style.RESET_ALL)
                    if bad_answers == 0:
                        good_answers += 1
                    break
                else:
                    if bad_answers < 2:
                        print(Fore.RED + "O nie! Spróbuj jeszcze raz!" + Style.RESET_ALL)
                        bad_answers += 1
                    else:
                        print(Fore.RED + f"Oh...Chyba ci się nie udało( Przecież to jest {glossary[value].upper()}" +
                              Style.RESET_ALL)
                        break
        print(f"\nDobra sprawa! Dostałeś {Fore.RED + f"{good_answers}/{length}" + Style.RESET_ALL} punktów!")

    @classmethod
    def get_theme(cls):
        while True:
            print("\nCo chcesz powtórzyć?\n"
                  "0. Wyjdź\n"
                  "1. Znaczenia gęstości\n"
                  "2. Formuły gęstości\n"
                  "3. Zamiana jedostek")
            answer = input("-----> ")
            match answer:
                case "0":
                    print(Fore.BLUE + "Miłej nauki!" + Style.RESET_ALL)
                    sleep(1.5)
                    break
                case "1":
                    cls.value_getter(density_mean)
                case "2":
                    cls.value_getter(density)
                case "3":
                    cls.value_getter(values)
                case _:
                    print(Fore.RED + "Wpisz liczbę od 0 do 2" + Style.RESET_ALL)


my_checker = MeaningsChecker()
my_checker.get_theme()
