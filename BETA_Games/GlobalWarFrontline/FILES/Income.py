from BETA_Games.GlobalWarFrontline.FILES.MainFiles.SysConfig import system


class Income:
    def __init__(self):
        self.income = 100_000

    def __call__(self):
        print(system.communicate(f"INCOME: ${self.income}/move", "LIGHTWHITE_EX"))


income = Income()
