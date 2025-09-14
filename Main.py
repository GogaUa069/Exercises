class NewList:
    def __init__(self, *args):
        self.__data_list = list(*args)

    def get_list(self):
        return self.__data_list

    def __sub__(self, other):
        other_list = other.get_list() if isinstance(other, NewList) else other
        for other_data in other_list:
            for data in self.__data_list:
                if other_data is data:
                    self.__data_list.remove(data)
                    other_list.remove(data)
        return NewList(self.__data_list)


list1 = NewList([0, 1, 2, 3])
list2 = NewList([0, False, True])

res1 = list1 - list2
print(res1.get_list())  # [1, 2, 3]
