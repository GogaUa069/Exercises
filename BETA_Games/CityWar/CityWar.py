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
ex_func = lambda: None

# ARMY
soldiers_option = system.Option("SOLDIERS", ex_func)
transport_option = system.Option("TRANSPORT", ex_func)
from_army_to_hq = system.Option(system.underlined_text("BACK - HEADQUARTER"), ex_func)

army_options = (soldiers_option, transport_option, from_army_to_hq)
army_menu = system.Menu("ARMY", army_options)

# HEADQUARTER
map_option = system.Option("MAP", fog_border)
army_option = system.Option("ARMY", army_menu)
logistics_option = system.Option("LOGISTICS", ex_func)  # ***
from_hq_to_main_menu = system.Option(system.underlined_text("BACK - MAIN MENU"), ex_func)

headquarter_options = (map_option, army_option, logistics_option, from_hq_to_main_menu)
headquarter_menu = system.Menu("HEADQUARTER", headquarter_options)

# MAIN MENU
battle_option = system.Option("BATTLE", headquarter_menu)
settings_option = system.Option("SETTINGS", ex_func)  # ***
quit_option = system.Option(system.underlined_text("QUIT"), ex_func)

main_menu_options = (battle_option, settings_option, quit_option)
main_menu = system.Menu("MAIN MENU", main_menu_options)

main_menu()
