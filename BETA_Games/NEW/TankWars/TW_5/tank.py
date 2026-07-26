from system import *

attributes = ("armor", "firepower", "radar", "camouflage", "speed")

stats_values = {
    3: (0, 1, 2, 3, 4),
    4: (1, 2, 3, 4, 5),
    5: (2, 3, 4, 5, 6)
}

max_lvls = {
    "light": {"armor": 3, "firepower": 3, "radar": 5, "camouflage": 5, "speed": 5},
    "medium": {"armor": 4, "firepower": 4, "radar": 4, "camouflage": 4, "speed": 4},
    "heavy": {"armor": 5, "firepower": 5, "radar": 3, "camouflage": 3, "speed": 3}
}


class Category:
    def __init__(self, name, num, symbol):
        self.name = name
        self.num = num
        self.symbol = symbol
        self.buffs = list(attributes)


class Light(Category):
    def __init__(self):
        super().__init__(name="light", num=1, symbol="○")


class Medium(Category):
    def __init__(self):
        super().__init__(name="medium", num=2, symbol="△")


class Heavy(Category):
    def __init__(self):
        super().__init__(name="heavy", num=3, symbol="□")


categories = {
    "light": Light,
    "medium": Medium,
    "heavy": Heavy
}


class Tank:
    __id = 0
    MAX_RANK = 3

    def __new__(cls, *args, **kwargs):
        cls.__id += 1
        return super().__new__(cls)

    def __init__(self, nation, category):
        self.nation = nation
        self.category = category
        self.name = "tank"
        self.rank = 1

        self.timed_stats = {"shelter": 0, "moving": 0, "territory": 1}
        self.timed_attr_effects = dict.fromkeys(attributes, 0)

        self.selected_buff = None
        self.selected_debuff = None

        self.set_effect(is_buff=True)
        self.set_effect(is_buff=False)

        self.stats = {
            "armor": stats_values[max_lvls[self.category.name]["armor"]][self.rank],
            "firepower": stats_values[max_lvls[self.category.name]["firepower"]][self.rank],
            "radar": stats_values[max_lvls[self.category.name]["radar"]][self.rank],
            "camouflage": stats_values[max_lvls[self.category.name]["camouflage"]][self.rank],
            "speed": stats_values[max_lvls[self.category.name]["speed"]][self.rank]
        }

    @property
    def id(self):
        return self.__id

    def get_symbol(self):
        return communicate(self.category.symbol, self.nation.color)

    def set_effect(self, is_buff):
        print(communicate(f"Select attribute to set {"buff" if is_buff else "debuff"}:", "CYAN"))
        while True:
            get_attrs(self.category.buffs, False)
            attr = input(communicate("<<< ", "LIGHTWHITE_EX"))
            match attr in self.category.buffs:
                case True:
                    max_lvls[self.category.name][attr] += 1 if is_buff else -1
                    match is_buff:
                        case True:
                            self.selected_buff = attr
                        case False:
                            self.selected_debuff = attr
                    self.category.buffs.remove(attr)
                    break
                case _:
                    print(communicate("ERROR: Incorrect name of attribute!", "LIGHTRED_EX"))

    def validate_timed_effects(self):
        pass

    def __repr__(self):
        return (f"unit __repr__\n"
                f"name:               {self.name}\n"
                f"id:                 {self.id}\n"
                f"rank:               {self.rank}\n"
                f"nation:             {self.nation.name} ({set_color(self.nation.color)})\n"
                f"category:           {self.category.name} / {self.category.num} / {self.category.symbol}\n"
                f"buffs:              {self.selected_buff}\n"
                f"debuffs:            {self.selected_debuff}\n"
                f"timed stats:        {self.timed_stats}\n"
                f"timed attr effects: {self.timed_attr_effects}\n"
                f"max levels:         {max_lvls[self.category.name]}\n"
                f"stats:              {self.stats}")

    def __str__(self):
        return communicate(f"UNIT INFO:\n"
                           f"- id:       {self.id}\n"
                           f"- rank:     {self.rank}\n"
                           f"- nation:   {self.nation.name} ({set_color(self.nation.color)})\n"
                           f"- category: {self.category.name} / {self.category.num} / {self.category.symbol}", "LIGHTWHITE_EX")
