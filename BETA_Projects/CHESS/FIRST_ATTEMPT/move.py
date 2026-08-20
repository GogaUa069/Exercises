from border import *


class Data:
     dead_moves_counter = 0  # 50 moves without bite or pawn move.
     same_moves_counter = 0  # 3 same moves


data = Data()


class Move:
    @staticmethod
    def validate_coord(coord):
        let, num = coord

        if len(coord) != 2:
            print(communicate("ERROR: Incorrect length!", "LIGHTRED_EX"))
            return False
        elif let.upper() not in border.LETTERS:
            print(communicate("ERROR: Incorrect letter!", "LIGHTRED_EX"))
            return False
        elif int(num) not in range(1, border.LENGTH+1):
            print(communicate("ERROR: Incorrect number!", "LIGHTRED_EX"))
            return False
        return True

    @staticmethod
    def set_piece(_from_coord, _to_coord):
        border[_to_coord] = copy(border[_from_coord])
        del border[_from_coord]

    def __call__(self, player):
        while True:
            print(communicate(f"\n{player.name}'s move.", "CYAN"))
            try:
                from_coord = input(communicate("from: ", "LIGHTWHITE_EX"))
                to_coord = input(communicate("to: ", "LIGHTWHITE_EX"))
                if self.validate_coord(from_coord) and self.validate_coord(to_coord):
                    self.set_piece(from_coord, to_coord)
                    border.get_border()
                    break
            except ValueError:
                print(communicate("ERROR: Incorrect data!", "LIGHTRED_EX"))


move = Move()
