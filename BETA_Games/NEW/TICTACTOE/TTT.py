from colorama import Fore, Style
import re


class Data:
    STAR = Fore.LIGHTWHITE_EX + "*" + Style.RESET_ALL
    BOARD_LINE = Fore.LIGHTWHITE_EX + "|" + Style.RESET_ALL

    def __init__(self):
        self.BOARD = [self.STAR]*9
        self.WINNER = str()

    @staticmethod
    def del_ascii(text):
        ansi_escape = re.compile(r"\x1B[@-_][0-?]*[ -/]*[@-~]")
        return ansi_escape.sub("", text)

    def get_board(self):
        print()
        print(*self.BOARD[6:9], sep=self.BOARD_LINE)
        print(*self.BOARD[3:6], sep=self.BOARD_LINE)
        print(*self.BOARD[0:3], sep=self.BOARD_LINE)

    def check_combinations(self):
        diagonal_lines_left = (self.BOARD[2], self.BOARD[4], self.BOARD[6])
        diagonal_lines_right = (self.BOARD[0], self.BOARD[4], self.BOARD[8])

        diagonal_lines = (diagonal_lines_left, diagonal_lines_right)
        vertical_lines = tuple(zip(self.BOARD[:3], self.BOARD[3:6], self.BOARD[6:]))
        horizontal_lines = tuple(zip(vertical_lines[0], vertical_lines[1], vertical_lines[2]))

        all_lines = [vertical_lines, horizontal_lines, diagonal_lines]

        combinations = ("X"*3, "O"*3)

        for lines in all_lines:
            for line in lines:
                if self.del_ascii("".join(line)) in combinations:
                    print("Found a combination!")
                    return True
        return False

    def set_position(self, symbol, position):
        self.BOARD[position-1] = symbol


data = Data()


class Player:
    def __init__(self, name, symbol):
        self.NAME = name
        self.SYMBOL = symbol

    def get_symbol(self):
        print(Fore.LIGHTWHITE_EX + f"{self.NAME} - {self.SYMBOL}" + Style.RESET_ALL)

    def move(self):
        print(Fore.CYAN + f"\n{self.NAME}'s move!" + Style.RESET_ALL)
        while True:
            position = input("<<< ")
            if position.isdigit() and int(position) in range(1, 10):
                data.set_position(self.SYMBOL, int(position))
                data.get_board()
                break
            else:
                print(Fore.LIGHTRED_EX + "Enter DIGIT in range 1-9\n" + Style.RESET_ALL)


player1 = Player("PLAYER1", Fore.LIGHTRED_EX + "X" + Style.RESET_ALL)
player2 = Player("PLAYER2", Fore.LIGHTBLUE_EX + "O" + Style.RESET_ALL)
PLAYERS = (player1, player2)

player1.get_symbol()
player2.get_symbol()
data.get_board()

while True:
    if data.check_combinations():
        break
    for player in PLAYERS:
        player.move()
