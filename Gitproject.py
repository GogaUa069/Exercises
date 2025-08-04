class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        """
        Adds new object to the end of the list
        :param obj: ObjList class ex.
        :return: Doesn't return anything
        """
        ...

    def remove_obj(self, indx):
        """
        Removes object from list by index
        :param indx: element index
        :return: Doesn't return anything
        """
        ...

    def __len__(self, linked_lst):
        """
        Shows total of list
        :param linked_lst:
        :return: Returns length of list
        """
        ...

    def linked_lst(self, indx):
        """
        Shows data from list object
        :param indx: class obj index
        :return: Returns __data
        """
        ...
