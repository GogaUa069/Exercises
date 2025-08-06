from math import sqrt


class RadiusVector:
    def __init__(self, *args):
        self.coord_length = len(args)
        self.coord_tuple = tuple()

        if self.coord_length == 1:
            self.coord_tuple = (0, )*args[0]

    def set_coords(self, *args):
        self.coord_tuple = tuple(args)

    def get_coords(self):
        return self.coord_tuple

    def __len__(self):
        return len(self.coord_tuple)

    def __abs__(self):
        square_root_sum_coords = sum([coord**2 for coord in self.coord_tuple])
        return sqrt(square_root_sum_coords)


#vector3D = RadiusVector(5)
#vector3D.set_coords(10, 20, 30)

#print("Coords:", vector3D.get_coords())
#print("Length:", len(vector3D))
#print("Abs:", abs(vector3D))
#a, b, c = vector3D.get_coords()
#print("a, b, c:", a, b, c)
