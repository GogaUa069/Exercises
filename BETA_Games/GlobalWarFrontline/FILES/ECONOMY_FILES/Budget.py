from BETA_Games.GlobalWarFrontline.FILES.MainFiles.SysConfig import system


class Budget:
    def __init__(self):
        self.budget = 500_000

    def __call__(self):
        print(system.communicate(f"BUDGET: ${self.budget}", "LIGHTWHITE_EX"))


budget = Budget()
