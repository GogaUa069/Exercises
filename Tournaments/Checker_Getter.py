from colorama import Fore, Style
from random import choice


class PairGetter:
    def __init__(self):
        self.name_count = 0
        self.name_list = list()
        self.pair_list = list()

    def get_name_number(self):
        while True:
            print(Fore.BLUE + "\nWpisz ilość osób:" + Style.RESET_ALL)
            try:
                self.name_count = int(input("-----> "))
                if self.name_count not in range(2, 51):
                    print(Fore.RED + "Dopuszczalna luczba ludzi: 2-50" + Style.RESET_ALL)
                    continue
            except ValueError:
                print(Fore.RED + "Wpisz liczbę!" + Style.RESET_ALL)
            else:
                break

    def get_people(self):
        print(Fore.BLUE + "\nWpisz osoby: (Imię Nazwisko)" + Style.RESET_ALL)
        for num in range(1, self.name_count+1):
            person = input(f"{num}. ")
            self.name_list.append(person)

    def get_person(self):
        person = choice(self.name_list)
        self.name_list.remove(person)
        return person

    def get_pairs_even_num(self):
        for _ in range(len(self.name_list)//2):
            person1 = self.get_person()
            person2 = self.get_person()
            pair = [person1, person2]
            self.pair_list.append(pair)

    def get_pairs_not_even_num(self):
        last_person = self.name_list[-1]
        del self.name_list[-1]
        my_range = range(len(self.name_list)//2)
        for indx in my_range:
            person1 = self.get_person()
            person2 = self.get_person()
            pair = [person1, person2]
            if indx == max(my_range):
                pair.append(last_person)
            self.pair_list.append(pair)

    def get_pairs(self):
        if len(self.name_list) % 2 == 0:
            self.get_pairs_even_num()
        else:
            self.get_pairs_not_even_num()

    def show_pairs(self):
        counter = 1
        print(Fore.BLUE + "\nPary:" + Style.RESET_ALL)
        for pair in self.pair_list:
            print(f"{counter}.", end=" ")
            print(*pair, sep=" - ")
            counter += 1


pair_getter1 = PairGetter()


def one_part():
    pair_getter1.get_name_number()
    pair_getter1.get_people()
    pair_getter1.get_pairs()
    pair_getter1.show_pairs()


one_part()
