from System import system
from Options import LEVELS


class MenuPattern:
    def __init__(self, header, options, border=None):
        self.HEADER, self.OPTIONS, self.BORDER = header, options, border

    def show_menu(self):
        if self.BORDER is None:
            print(system.communicate(f"\n>>> {self.HEADER}", "LIGHTRED_EX"))
            for i, opt in enumerate(self.OPTIONS, 1):
                print(system.communicate(f"{i}. {opt.NAME}", "LIGHTBLUE_EX"))
        else:
            self.BORDER()

    def check_answer(self, answer):
        for indx, option in enumerate(self.OPTIONS, 1):
            if answer.upper() in (option.NAME.upper(), str(indx)):
                option()
                return
        print(system.communicate("ERROR: Select one of the options shown above!", "LIGHTRED_EX"))

    def __call__(self):
        answer = str()
        while answer != str(len(self.OPTIONS)):
            self.show_menu()
            answer = input(system.INPUT)
            self.check_answer(answer)


class BorderPattern:
    HEADERS = ["LVL", "NAME", "TYPE", "DESCRIPTION"]

    def __init__(self, levels: list):
        self.DATA = [self.HEADERS] + [lvl.DATA for lvl in levels]
        self.WIDTHS = [max(len(system.del_color(item)) for item in col) for col in zip(*self.DATA)]

    def __call__(self):
        for row in self.DATA:
            line = "".join(f"| {item.ljust(self.WIDTHS[i]+1)}" for i, item in enumerate(row)) + "|"
            print(line)


game_border = BorderPattern(LEVELS)
