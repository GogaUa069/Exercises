from system_configuration import *


class Team:
    def __init__(self, name: str):
        self.name = name.title()


bulwark = Team(system.communicate("bulwark", "LIGHTBLUE_EX"))
vanguard = Team(system.communicate("vanguard", "LIGHTRED_EX"))
