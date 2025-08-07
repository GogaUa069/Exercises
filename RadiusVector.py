from math import sqrt


class RadiusVector:
    def __init__(self, *args):
        if len(args) == 1:
            self.coord_list = [0]*args[0]
        else:
            self.coord_list = list(args)

    def set_coords(self, *args):
        for indx, arg in enumerate(args):
            if indx < len(self.coord_list):
                self.coord_list[indx] = arg
            else:
                self.coord_list.append(arg)

    def get_coords(self):
        return tuple(self.coord_list)

    def __len__(self):
        return len(self.coord_list)

    def __abs__(self):
        square_coords = sum([coord**2 for coord in self.coord_list])
        return sqrt(square_coords)
