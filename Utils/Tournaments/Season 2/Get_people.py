from Tournament_2_names import name_list
from random import choice


class NamesGetter:
    def __init__(self):
        self.pair_dict = dict()

    @staticmethod
    def get_name_from_list():
        name = choice(name_list)
        name_list.remove(name)
        return name

    def get_pairs(self):
        for _ in range(6):
            first_name = self.get_name_from_list()
            second_name = self.get_name_from_list()
            self.pair_dict[first_name] = second_name

    def get_pair_names(self):
        key_list = list(self.pair_dict.keys())
        value_list = list(self.pair_dict.values())
        for indx in range(6):
            print(f"{indx+1}. {key_list[indx]} - {value_list[indx]}")


name_getter = NamesGetter()
name_getter.get_pairs()
name_getter.get_pair_names()
