from SysConfig import system
from random import randint


class Border:
    WIDTH = 1000
    HEIGHT = 100

    left_border = system.communicate("|", "LIGHTGREEN_EX")
    right_border = system.communicate("|", "LIGHTRED_EX")
    water = system.communicate("≈", "LIGHTBLUE_EX")
    tree = system.communicate("^", "LIGHTGREEN_EX")
    fog = system.communicate("*", "LIGHTBLACK_EX")
    space = system.communicate(".", "WHITE")
    road = "="

    def __init__(self):
        self.BORDER = [[self.space for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]
        self.FOG_BORDER = None
        self()

    @staticmethod
    def get_border(b):
        print()
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


border = Border()
fog_border = lambda: border.get_border(border.FOG_BORDER)
pass_func = lambda: None
coming_soon = lambda: print(system.communicate("COMING SOON...", "LIGHTWHITE_EX"))

# ECONOMY
income_option = system.Option("INCOME", coming_soon)  # ***
budget_option = system.Option("BUDGET", coming_soon)  # ***
loan_option = system.Option("LOAN", coming_soon)  # ***
from_economy_to_logistics = system.Option(system.underlined_text("BACK - LOGISTICS"), pass_func)

economy_options = (income_option, budget_option, loan_option, from_economy_to_logistics)
economy_menu = system.Menu("ECONOMY", economy_options)

# ARMY_TRANSPORT
arc_options = system.Option("ARC", coming_soon)  # ***
troop_transport_option = system.Option("TROOP TRANSPORT", coming_soon)  # ***
aircraft_option = system.Option("AIRCRAFT", coming_soon)  # ***
from_army_transport_to_army = system.Option(system.underlined_text("BACK - ARMY"), pass_func)

army_transport_options = (arc_options, troop_transport_option, aircraft_option, from_army_transport_to_army)
army_transport_menu = system.Menu("ARMY TRANSPORT", army_transport_options)

# SOLDIERS
psychology_option = system.Option("PSYCHOLOGY", coming_soon)  # ***
equipment_option = system.Option("EQUIPMENT", coming_soon)  # ***
dislocation_option = system.Option("DISLOCATION", coming_soon)  # ***
habits_option = system.Option("HABITS", coming_soon)  # ***
sections_option = system.Option("SECTIONS", coming_soon)  # ***
from_soldiers_to_army = system.Option(system.underlined_text("BACK - ARMY"), pass_func)

soldiers_options = (psychology_option, equipment_option, dislocation_option, habits_option, sections_option, from_soldiers_to_army)
soldiers_menu = system.Menu("SOLDIERS", soldiers_options)

# LOGISTICS
economy_option = system.Option("ECONOMY", economy_menu)
urbanisation_option = system.Option("URBANISATION", coming_soon)  # ***
logistics_transport_option = system.Option("TRANSPORT", coming_soon)  # ***
from_logistics_to_hq = system.Option(system.underlined_text("BACK - HEADQUARTER"), pass_func)

logistics_options = (economy_option, urbanisation_option, logistics_transport_option, from_logistics_to_hq)
logistics_menu = system.Menu("LOGISTICS", logistics_options)

# ARMY
soldiers_option = system.Option("SOLDIERS", soldiers_menu)
army_transport_option = system.Option("TRANSPORT", army_transport_menu)
from_army_to_hq = system.Option(system.underlined_text("BACK - HEADQUARTER"), pass_func)

army_options = (soldiers_option, army_transport_option, from_army_to_hq)
army_menu = system.Menu("ARMY", army_options)

# HEADQUARTER
map_option = system.Option("MAP", fog_border)
army_option = system.Option("ARMY", army_menu)
logistics_option = system.Option("LOGISTICS", logistics_menu)
from_hq_to_main_menu = system.Option(system.underlined_text("BACK - MAIN MENU"), pass_func)

headquarter_options = (map_option, army_option, logistics_option, from_hq_to_main_menu)
headquarter_menu = system.Menu("HEADQUARTER", headquarter_options)

# MAIN MENU
battle_option = system.Option("BATTLE", headquarter_menu)
settings_option = system.Option("SETTINGS", coming_soon)  # ***
quit_option = system.Option(system.underlined_text("QUIT"), pass_func)

main_menu_options = (battle_option, settings_option, quit_option)
main_menu = system.Menu("MAIN MENU", main_menu_options)

main_menu()
