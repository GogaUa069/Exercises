class Budget:
    def __init__(self):
        self.item_list = list()

    def add_item(self, it):
        if isinstance(it, Item):
            self.item_list.append(it)

    def remove_item(self, indx):
        try:
            del self.item_list[indx]
        except IndexError:
            print(False)

    def get_items(self):
        return self.item_list


class Item:
    def __init__(self, name: str, money: (int, float)):
        self.name = name
        self.money = money

    def __add__(self, other):
        return self.money + other.money

    def __radd__(self, other):
        return self.money + other
