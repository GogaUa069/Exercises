from prettytable import PrettyTable

border = PrettyTable()
border.field_names = ["LVL", "NAME", "TYPE", "DESCRIPTION"]

border.add_row(["1", "BASIC", "COMMON", "Infinite lives. Time-free mode."])
border.add_row(["2", "AVERAGE", "COMMON", "Finite lives. Time-free mode."])
border.add_row(["3", "ADVANCED", "COMMON", "Finite lives. Countdown active."])
border.add_row(["4", "WILD", "EPIC", "Lives and time are randomized."])
border.add_row(["5", "CUSTOM", "EPIC", "Lives and time are under your control."])
border.add_row(["6", "ADVENTURE", "LEGENDARY", "Beat AVERAGE, ADVANCED, and WILD levels in a single run!"])
border.add_row(["7", "MAIN MENU", "---------", "Back to Main Menu"])

print(border, end="\n")
