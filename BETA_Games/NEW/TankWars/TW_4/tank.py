from system import *

attributes = ("armor", "firepower", "radar", "camouflage")

stats_values = {
    1: (0, 0, 0.5, 1, 1.5),
    2: (0.5, 1, 1.5, 2, 2.5),
    3: (0, 1, 2, 3, 4)
}

effects = {
    "light": list(attributes[:2]),  # armor, firepower
    "medium": list(attributes),     # armor, firepower, radar, camouflage
    "heavy": list(attributes[2:])   # radar, camouflage
}

max_lvls = {
    "light": {"armor": 1, "firepower": 1, "radar": 3, "camouflage": 3},
    "medium": {"armor": 2, "firepower": 2, "radar": 2, "camouflage": 2},
    "heavy": {"armor": 3, "firepower": 3, "radar": 1, "camouflage": 1}
}


class Category:
    def __init__(self, name, num, symbol):
        super().__init__()
        self.name = name
        self.num = num
        self.symbol = symbol
        self.buffs = effects[self.name].copy()


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
        self.category = categories[category]()
        self.name = "tank"
        self.rank = 1

        self.timed_stats = {"shelter": 0, "moving": 0, "territory": 1}
        self.timed_attr_effects = dict.fromkeys(attributes, 0)

        self.selected_buff = None
        self.selected_debuff = None

        match self.category.name:
            case "heavy" | "light":
                self.set_effect(is_buff=True)
            case "medium":
                self.set_effect(is_buff=True)
                self.set_effect(is_buff=False)

        self.stats = {
            "armor": stats_values[max_lvls[self.category.name]["armor"]][self.rank],
            "firepower": stats_values[max_lvls[self.category.name]["firepower"]][self.rank],
            "radar": stats_values[max_lvls[self.category.name]["radar"]][self.rank],
            "camouflage": stats_values[max_lvls[self.category.name]["camouflage"]][self.rank]
        }

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    def get_symbol(self):
        return communicate(self.category.symbol, self.nation.color)

    def set_effect(self, is_buff):
        print(communicate(f"Select attribute to set {"buff" if is_buff else "debuff"}:", "CYAN"))
        while True:
            get_attrs(self.category.buffs)
            attr = input(communicate("<<< ", "LIGHTWHITE_EX")).lower()
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
                case False:
                    print(communicate("ERROR: The attribute name is not correct or is already in use!", "LIGHTRED_EX"))

    def validate_timed_effects(self):
        pass

    def __str__(self):
        return communicate(f"UNIT INFO:\n"
                f"- id:       {self.__id}\n"
                f"- rank:     {self.rank}\n"
                f"- nation:   {self.nation.name} ({self.nation.color})\n"
                f"- category: {self.category.name} / {self.category.num} / {self.category.symbol}\n", "LIGHTWHITE_EX")

    def __repr__(self):
        return (f"__repr__:\n"
                f"name:              {self.name}\n"
                f"id:                {self.__id}\n"
                f"rank:              {self.rank}\n"
                f"nation:            {self.nation.name} ({self.nation.color})\n"
                f"category:          {self.category.name} / {self.category.num} / {self.category.symbol}\n"
                f"buffs:             {self.selected_buff}\n"
                f"debuffs:           {self.selected_debuff}\n"
                f"timed stats:       {self.timed_stats}\n"
                f"timed attr effects {self.timed_attr_effects}\n"
                f"max levels:        {max_lvls[self.category.name]}\n"
                f"stats:             {self.stats}")
