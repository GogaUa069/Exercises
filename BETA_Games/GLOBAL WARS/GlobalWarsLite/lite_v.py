from colorama import Fore, Style
from random import randint


class Section:
    def __init__(self, name: str, symbol: str, amount: tuple):
        self.name = name
        self.symbol = symbol
        self.amount = amount


squad = Section("squad", "S", (5, 10))
battalion = Section("battalion", "B", (100, 500))


class Location:
    def __init__(self, name: str, symbol: str, amount: int, cost: int, energy: int):
        self.name = name
        self.symbol = symbol
        self.amount = amount
        self.cost = cost
        self.energy = energy


field_tent = Location("field tent", "T", 20, 100, 10)


class Habit:
    def __init__(self, name: str):
        self.name = name
        self.lvl = 0  # MAX: 5


class Psychology:
    def __init__(self, name: str):
        self.name = name
        self.lvl = 0  # MAX: 5


class Team:
    def __init__(self, name: str):
        self.name = name
        self.budget = 100_000
        self.energy = 1000


bulwark = Team("bulwark")
vanguard = Team("vanguard")


class Data:
    income = 100_000
    moves = 100
    energy = 1000

    def __init__(self):
        self.INPUT = self.communicate("<<< ", "LIGHTWHITE_EX")
        self.pass_func = lambda: None
        self.coming_soon = lambda: print(self.communicate("COMING SOON...", "LIGHTWHITE_EX"))

    @staticmethod
    def communicate(text, color):
        text = getattr(Fore, color) + text + Style.RESET_ALL if color is not None else text
        return text


data = Data()


class Menu:
    def __init__(self, header, options):
        self.HEADER = header.upper()
        self.OPTIONS = options

    def get_menu(self):
        print(data.communicate(f"\n[ {self.HEADER} ]", "LIGHTRED_EX"))
        for indx, option in enumerate(self.OPTIONS, 1):
            print(data.communicate(f"{indx}. {option.NAME}", "GREEN"))

    def _check_answer(self, answer):
        for indx, option in enumerate(self.OPTIONS, 1):
            if answer == str(indx):
                option()
                return
        print(data.communicate("ERROR: Select one of the options shown above!", "LIGHTRED_EX"))

    def __call__(self):
        answer = str()
        while answer != str(len(self.OPTIONS)):
            self.get_menu()
            answer = input(data.INPUT)
            self._check_answer(answer)


class Option:
    def __init__(self, name, func):
        self.NAME = name.upper()
        self.FUNC = func

    def __call__(self):
        self.FUNC()


class Border:
    left_border = data.communicate("|", "LIGHTGREEN_EX")
    right_border = data.communicate("|", "LIGHTRED_EX")
    water = data.communicate("≈", "LIGHTBLUE_EX")
    tree = data.communicate("^", "LIGHTGREEN_EX")
    fog = data.communicate("*", "LIGHTBLACK_EX")
    space = data.communicate(".", "WHITE")
    road = "="

    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height
        self.BORDER = [[self.space for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]
        self.FOG_BORDER = None
        self()

    @staticmethod
    def get_border(b):
        for line in b:
            print("".join(line))

    def set_forest(self, trees=3000):
        for _ in range(trees):
            x = randint(2, self.WIDTH-3)
            y = randint(0, self.HEIGHT-1)
            self.BORDER[y][x] = self.tree

    def set_rivers(self):
        for point in (4, 2, 1.334):
            x = int(self.WIDTH//point)
            for indx, _ in enumerate(self.BORDER):
                step = randint(-2, 2)
                length = randint(7, 10)
                for i in range(length):
                    self.BORDER[indx][x+step+i] = self.water

    def set_roads(self):
        for _ in range(5):
            while True:
                y1, y2 = randint(1, self.HEIGHT-2), randint(1, self.HEIGHT-2)
                if ("=" not in (self.BORDER[y1-1][1], self.BORDER[y1][1], self.BORDER[y1+1][1])
                        and "=" not in (self.BORDER[y2-1][-2], self.BORDER[y2][-2], self.BORDER[y2+1][-2])):
                    break
            self.BORDER[y1][1:6] = ("=", )*5
            self.BORDER[y2][-6:-1] = ("=", )*5

    def set_borders(self):
        for line in self.BORDER:
            line[0] = self.left_border
            line[-1] = self.right_border

    def set_fog_border(self):
        self.FOG_BORDER = [row[:] for row in self.BORDER]
        half_x = int(self.WIDTH // 2)
        for line in self.FOG_BORDER:
            line[half_x:] = [self.fog] * (self.WIDTH - half_x)

    def __call__(self):
        self.set_forest()
        self.set_rivers()
        self.set_roads()
        self.set_borders()
        self.set_fog_border()


border = Border(1000, 100)
fog_border = lambda: border.get_border(border.FOG_BORDER)


class CheckMove:
    def __call__(self, team, thing):
        if not team.budget - thing.cost >= 0:
            print(data.communicate("ERROR: Not enough money to purchase this item!", "LIGHTRED_EX"))
            return False
        elif not team.energy - thing.energy >= 0:
            print(data.communicate("ERROR: Not enough energy to purchase this item!", "LIGHTRED_EX"))
            return False
        else:
            team.energy -= thing.energy
            team.budget -= thing.cost
            return True


class SetPosition:
    def __init__(self, team, cell):
        self.x = self.y = 0
        self.cell = cell
        self.team = team

    def set_coords(self):
        while True:
            try:
                self.x = int(input("Enter X: "))
            except self.x not in range(1, 1001):
                data.communicate("ERROR: Enter an integer in range 1-150", "LIGHTRED_EX")
            except ValueError:
                data.communicate("ERROR: Enter an integer in range 1-150", "LIGHTRED_EX")
            else:
                break
        while True:
            try:
                self.y = int(input("Enter Y: "))
            except self.y not in range(1, 101):
                data.communicate("ERROR: Enter an integer in range 1-100", "LIGHTRED_EX")
            except ValueError:
                data.communicate("ERROR: Enter an integer in range 1-100", "LIGHTRED_EX")
            else:
                break

    def __call__(self):
        a = CheckMove()
        if a(self.team, self.cell):
            self.set_coords()
            border.BORDER[self.y-1][self.x] = self.cell.symbol
            border.set_fog_border()
            fog_border()
            return True
        else:
            return False


# LOCATION
field_tent_option = Option("field tent", SetPosition(bulwark, field_tent))
from_location_to_soldiers = Option("back - soldiers", data.pass_func)

location_options = (field_tent_option, from_location_to_soldiers)
location_menu = Menu("location", location_options)

# SOLDIERS
psychology_option = Option("psychology", data.coming_soon)
habits_option = Option("habits", data.coming_soon)
sections_option = Option("sections", data.coming_soon)
location_option = Option("location", location_menu)
from_soldiers_to_army = Option("back - army", data.pass_func)

soldiers_options = (psychology_option, habits_option, sections_option, location_option, from_soldiers_to_army)
soldiers_menu = Menu("soldiers", soldiers_options)

# ARMY
soldiers_option = Option("soldiers", soldiers_menu)
combat_transport = Option("combat transport", data.coming_soon)
from_army_to_hq = Option("back - headquarter", data.pass_func)

army_options = (soldiers_option, combat_transport, from_army_to_hq)
army_menu = Menu("army", army_options)

# HEADQUARTER
map_option = Option("map", fog_border)
army_option = Option("army", army_menu)
logistics_option = Option("logistics", data.coming_soon)
quit_option = Option("quit", data.pass_func)

hq_options = (map_option, army_option, logistics_option, quit_option)
hq_menu = Menu("headquarter", hq_options)

hq_menu()
