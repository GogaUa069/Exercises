import time


class FilterTemplate:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__.keys():
            return
        else:
            object.__setattr__(self, key, value)


class Mechanical(FilterTemplate):
    pass


class Aragon(FilterTemplate):
    pass


class Calcium(FilterTemplate):
    pass


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slot_indx = (("Mechanical", 1), ("Aragon", 2), ("Calcium", 3))
        self.slots = {1: False, 2: False, 3: False}

    def add_filter(self, slot_num, filter):
        for template in self.slot_indx:
            if (filter.__class__.__name__, slot_num) == template and not self.slots[slot_num]:
                self.slots[slot_num] = filter


    def remove_filter(self, slot_num):
        if self.slots[slot_num]:
            self.slots[slot_num] = False

    def get_filters(self):
        slot_tuple = tuple(self.slots.values())
        return slot_tuple

    def water_on(self):
        if all(list(self.slots.values())):
            for filter_ in self.slots.values():
                end = time.time()
                start = filter_.date
                if end - start > self.MAX_DATE_FILTER:
                    return False
                return True
        else:
            return False


# my_water = GeyserClassic()
# my_water.add_filter(1, Mechanical(time.time()))
# my_water.add_filter(2, Aragon(time.time()))
#
# w = my_water.water_on() # False
# print("Water_on 1:", w)
# my_water.add_filter(3, Calcium(time.time()))
# w = my_water.water_on() # True
# print("Water_on 2:", w)
#
# f1, f2, f3 = my_water.get_filters()
# print("\nFilters:")
# print("Mechanical:", f1)
# print("Aragon:", f2)
# print("Calcium:", f3)
#
# my_water.remove_filter(1)
# print(my_water.get_filters())
#
# print("Water_on 3 (After deleting):", my_water.water_on())
