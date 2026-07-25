from colorama import Fore, Style, Back


def communicate(text, color):
    return getattr(Fore, color) + text + Style.RESET_ALL


def get_back(figure, color):
    return getattr(Back, color) + f" {figure} " + Style.RESET_ALL


def _get_back(symbol, color):
    return getattr(Back, color) + symbol + Style.RESET_ALL


y_coords = list(range(1, 9))[::-1]
x_coords = [chr(cod) for cod in range(65, 73)]

colors = {
    "white": "LIGHTWHITE_EX",
    "black": "BLACK"
}


class Cell:
    def __init__(self, x: int, y: int, color: str):
        self.x = x
        self.y = y
        self.color = color
        self.figure = None

    def __repr__(self):
        return f"color: {self.color}, x: {self.x}, y: {self.y}, figure: {self.figure}, position: {x_coords[self.y][self.x]}"

    def get_cell(self):
        match self.figure:
            case None:
                return get_back(" ", colors[self.color])
            case _:
                return get_back(self.figure, colors[self.color])


class Border:
    LENGTH = 8

    def __init__(self):
        self.border = list()
        self.__set_border()

    def __getitem__(self, item):
        x, y = item
        return self.border[8-int(y)][x_coords.index(x.upper())]

    def __setitem__(self, key, value):
        x, y = key
        self.border[8-int(y)][x_coords.index(x.upper())].figure = value

    def __delitem__(self, key):
        x, y = key
        self.border[8-int(y)][x_coords.index(x.upper())].figure = None

    def __set_border(self):
        def get_color(x_, y_):
            match (x_ % 2, y_ % 2):
                case (0, 0) | (1, 1):
                    return "white"
                case _:
                    return "black"

        for x in range(self.LENGTH):
            row = list()
            for y in range(self.LENGTH):
                color = get_color(x, y)
                cell = Cell(x, y, color)
                row.append(cell)
            self.border.append(row)

    def get_border(self):
        print(" ", *x_coords, sep="  ")
        for indx, row in enumerate(self.border):
            symbol = ""
            if not any(cell.figure is not None for cell in row):
                symbol = " "
            print(y_coords[indx], "".join(cell.get_cell() for cell in row) + _get_back(symbol, colors[row[-1].color]))


border = Border()
border.get_border()

border["a3"] = "♛"
border["d5"] = "♙"
border["d7"] = "♟"
border["d6"] = "♙"
border["d8"] = "♟"

border.get_border()
