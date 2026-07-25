from SYSTEM_PROMPT import system


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
        self.TYPE = lvl_type
        self.DESCR = descr
        self.DATA = [self.LVL, self.NAME, self.TYPE, self.DESCR]


LEVELS = [
    ...
]
