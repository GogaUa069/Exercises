from System import system


class Option:
    def __init__(self, name, func):
        self.NAME = name
        self.FUNC = func

    def __call__(self):
        self.FUNC()


class BorderOption:
    def __init__(self, lvl, name, lvl_type, descr):
        self.LVL = lvl
        self.NAME = name
        self.LVL_TYPE = lvl_type
        self.DESCR = descr
        self.DATA = [self.LVL, self.NAME, self.LVL_TYPE, self.DESCR]


LEVELS = [
    BorderOption("1", "BASIC", system.LVL_TYPES["COMMON"], "Infinite lives. Time-free mode."),
    BorderOption("2", "AVERAGE", system.LVL_TYPES["COMMON"], "Finite lives. Time-free mode."),
    BorderOption("3", "ADVANCED", system.LVL_TYPES["COMMON"], "Finite lives. Countdown active."),
    BorderOption("4", "WILD", system.LVL_TYPES["EPIC"], "Lives and time are randomized."),
    BorderOption("5", "CUSTOM", system.LVL_TYPES["EPIC"], "Lives and time are under your control."),
    BorderOption("6", "ADVENTURE",  system.LVL_TYPES["LEGENDARY"],"Beat AVERAGE, ADVANCED, and WILD levels in a single run and get a prize!"),
    BorderOption("7", "DUEL", system.LVL_TYPES["LEGENDARY"], "Think of a number and let the computer try to guess it."),
    BorderOption("8", "MAIN MENU", "---------", "Back to Main Menu")]
