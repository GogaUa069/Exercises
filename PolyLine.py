class PolyLine:
    def __init__(self, start_coord, *args):
        self.start_coord = start_coord
        self.coord_list = list(args)
        self.coord_list.insert(0, start_coord)

    def add_coord(self, x, y):
        new_coord = (x, y)
        self.coord_list.append(new_coord)

    def remove_coord(self, indx):
        del self.coord_list[indx]

    def get_coords(self):
        return tuple(self.coord_list)
