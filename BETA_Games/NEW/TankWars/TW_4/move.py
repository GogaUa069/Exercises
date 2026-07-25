from border import *
from tank import *


class Move:
    def __init__(self, player):
        self.player = player
        self.x_range = range(1, border.width // 2 + 1) if self.player.nation.name == "vanguard" else range(border.width // 2 + 1, border.width + 1)

    def get_positions(self):
        if len(self.player.units) != 0:
            print(communicate("Your units:", "LIGHTWHITE_EX"), end=" ")
            get_attrs(self.player.units.values(), one_row=True)
        else:
            print(communicate("No units yet.", "LIGHTWHITE_EX"))

    def set_unit(self):
        print(communicate("Creating unit...", "CYAN"))
        self.get_positions()

        while True:
            print(communicate("\nEnter data:", "CYAN"))
            try:
                x = int(input(communicate(f"- X ({self.x_range[0]}-{self.x_range[-1]}): ", "LIGHTWHITE_EX")))
                y = int(input(communicate(f"- Y (1-{border.height}): ", "LIGHTWHITE_EX")))
            except ValueError:
                print(communicate("ERROR: Wrong position!", "LIGHTRED_EX"))
                continue
            else:
                if x not in range(self.x_range[0], self.x_range[-1]+1) or y not in range(1, border.height + 1):
                    print(communicate("ERROR: Position is out of range!", "LIGHTRED_EX"))
                    continue
                cell = border[x, y]
                category = input(communicate(f"- category: ({", ".join(categories.keys())}): ", "LIGHTWHITE_EX")).lower()
                if category not in categories.keys():
                    print(communicate("ERROR: Wrong category!", "LIGHTRED_EX"))
                elif isinstance(cell.unit, Tank):
                    print(communicate("ERROR: This cell is already occupied!", "LIGHTRED_EX"))
                elif cell.nation is not None and cell.nation != self.player.nation:
                    print(communicate("ERROR: Can not spawn unit on the enemies territory!", "LIGHTRED_EX"))
                elif cell.name == "tree":
                    print(communicate("ERROR: Can not spawn units on trees!", "LIGHTRED_EX"))
                else:
                    tank = Tank(self.player.nation, category)
                    border[x, y] = tank
                    self.player.units[tank.id] = (x, y)
                    print(communicate("\nUnit created successfully!\n", "CYAN"))
                    break

    def get_unit(self):
        if len(self.player.units) == 0:
            print(communicate("WARNING: You do not have units!\n", "LIGHTYELLOW_EX"))
        else:
            print(communicate("Selecting units...", "CYAN"))
            self.get_positions()
            while True:
                print(communicate("\nSet position:", "CYAN"))
                try:
                    x = int(input(communicate(f"- X ({self.x_range[0]}-{self.x_range[-1]}): ", "LIGHTWHITE_EX")))
                    y = int(input(communicate(f"- Y (1-{border.height}): ", "LIGHTWHITE_EX")))
                except ValueError:
                    print(communicate("ERROR: Wrong position!", "LIGHTRED_EX"))
                else:
                    if x not in range(1, border.width + 1) or y not in range(1, border.height + 1):
                        print(communicate("ERROR: Position is out of range!", "LIGHTRED_EX"))
                    else:
                        print(border[x, y])
                        break

    def __call__(self):
        print(communicate(f"\n{self.player.nation.name.capitalize()} team move!", "CYAN"))
        while True:
            get_attrs(("Create unit", "Select unit", "Map", "End move"))
            option = input(communicate("<<< ", "LIGHTWHITE_EX")).lower()
            match option:
                case "1" | "create unit":
                    self.set_unit()
                case "2" | "select unit":
                    self.get_unit()
                case "3" | "map":
                    border.get_border(self.player)
                case "4" | "end move":
                    break
                case _:
                    print(communicate("ERROR: Select one of the options shown above!", "LIGHTWHITE_EX"))
