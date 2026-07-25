from border import *

UNITS = dict()


class Unit:
    def __init__(self, symbol: str, name: str, variety: str, amount: int, coords: tuple):
        self.symbol = symbol
        self.name = name
        self.variety = variety
        self.amount = amount
        self.coords = coords

    def __str__(self):
        return (f"\nUNIT INFO:\n"
                f"- NAME:    {self.name}\n"
                f"- VARIETY: {self.variety}\n"
                f"- AMOUNT:  {self.amount}\n"
                f"- COORDS:  {self.coords}")


class UnitOperations:
    platoon_counter = 0

    def set_unit(self):
        while True:
            print(communicate("\nSet coordinates of unit:", "CYAN"))
            try:
                x = int(input("X (1-1000): "))
                y = int(input("Y (1-100): "))

                if x not in range(1, border.WIDTH):
                    print(communicate("ERROR: X coordinate is out of range!", "LIGHTRED_EX"))
                elif y not in range(1, border.HEIGHT + 1):
                    print(communicate("ERROR: Y coordinate is out of range!", "LIGHTRED_EX"))
                elif border.BORDER[y-1][x] != LAND:
                    print(communicate("ERROR: Can spawn units only on land!", "LIGHTRED_EX"))
                else:
                    self.platoon_counter += 1
                    border.BORDER[y-1][x] = Unit(communicate("O", "BLUE"), f"PLATOON{self.platoon_counter}", "LITE", 50, (x, y))
                    unit = border.BORDER[y-1][x]
                    UNITS[unit.name] = unit.coords
                    border.get_border()
                    break

            except Exception:
                print(communicate("ERROR: Wrong coordinate!", "LIGHTRED_EX"))

    def select_unit(self):

        def get_units():
            print()
            for name, coord in UNITS.items():
                print(f"{name}: {coord}")
            print()

        while True:
            print(communicate("\nSet coordinates of unit:", "CYAN"))
            get_units()

            try:
                x = int(input("X (1-1000): "))
                y = int(input("Y (1-100): "))

                if x not in range(1, border.WIDTH):
                    print(communicate("ERROR: X coordinate is out of range!", "LIGHTRED_EX"))
                elif y not in range(1, border.HEIGHT + 1):
                    print(communicate("ERROR: Y coordinate is out of range!", "LIGHTRED_EX"))
                elif type(border.BORDER[y-1][x]) != Unit:
                    print(communicate("ERROR: No unit on this coordinates!", "LIGHTRED_EX"))
                else:
                    print(border.BORDER[y-1][x])
                    break

            except Exception:
                print(communicate("ERROR: Wrong coordinate!", "LIGHTRED_EX"))


unit_operation = UnitOperations()


def
