class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.coords = list()

    def add_point(self, x, y, speed):
        data = [(x, y), speed]
        self.coords.append(data)

    def __validate_indx(self, indx):
        return isinstance(indx, int) and indx in range(len(self.coords))

    def __getitem__(self, item):
        if self.__validate_indx(item):
            return self.coords[item]
        else:
            raise IndexError("некорректный индекс")

    def __setitem__(self, key, value):
        if self.__validate_indx(key):
            self.coords[key][1] = value
        else:
            raise IndexError("некорректный индекс")
