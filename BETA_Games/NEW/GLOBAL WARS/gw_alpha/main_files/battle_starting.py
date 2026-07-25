from team import *
from system_configuration import *
from player import *


class BattleStarting:

    @staticmethod
    def select_side():
        side = vanguard  # choice((bulwark, vanguard))
        player.team = side

    @staticmethod
    def reset_values():
        data.moves_left = data.max_moves

