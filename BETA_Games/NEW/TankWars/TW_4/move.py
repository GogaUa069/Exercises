from border import *
from tank import *


class Move:
    def __init__(self, player):
        self.player = player

    def set_unit(self):
        print(communicate("Creating unit...\nEnter data:", "CYAN"))
        while True:
            try:
                category = input(communicate(f"- category: ({", ".join(categories.keys())}): ", "LIGHTWHITE_EX")).lower()
                x = int(input(communicate(f"- X (1-{border.width}): ", "LIGHTWHITE_EX")))
                y = int(input(communicate(f"- Y (1-{border.height}): ", "LIGHTWHITE_EX")))
            except Exception as e:
                print(e)
                print(communicate("ERROR: Wrong data!", "LIGHTRED_EX"))
            else:
                if x not in range(1, border.width + 1) or y not in range(1, border.height + 1):
                    print(communicate("ERROR: Wrong position!", "LIGHTRED_EX"))
                    continue
                cell = border[x, y]
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
                    break

    def get_unit(self):
        def get_positions():
            print(communicate("Your units:", "LIGHTWHITE_EX"))
            get_attrs(self.player.units.values())

        if len(self.player.units) == 0:
            print(communicate("WARNING: You do not have units!", "LIGHTYELLOW_EX"))
        else:
            print(communicate("Selecting units...\nEnter data:", "CYAN"))
            get_positions()
            while True:
                try:
                    x = int(input(communicate(f"- X (1-{border.width}): ", "LIGHTWHITE_EX")))
                    y = int(input(communicate(f"- Y (1-{border.height}): ", "LIGHTWHITE_EX")))
                except Exception as e:
                    print(e)
                    print(communicate("ERROR: Wrong data!", "LIGHTRED_EX"))
                else:
                    if x not in range(1, border.width + 1) or y not in range(1, border.height + 1):
                        print(communicate("ERROR: Wrong position!", "LIGHTRED_EX"))
                    else:
                        print(border[x, y])
                        break

    def __call__(self):
        print(communicate("Your move!", "CYAN"))
        while True:
            get_attrs(("Create unit", "Select unit", "Map", "End move"))
            option = input(communicate("<<< ", "LIGHTWHITE_EX")).lower()
            match option:
                case "1" | "create unit":
                    self.set_unit()
                case "2" | "select unit":
                    self.get_unit()
                case "3" | "map":
                    border.get_border()
                case "4" | "end move":
                    break
                case _:
                    print(communicate("ERROR: Select one of the options shown above!", "LIGHTWHITE_EX"))


move = Move(player1)
move()
