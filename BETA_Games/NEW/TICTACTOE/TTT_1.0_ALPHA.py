from colorama import Fore, Style
from time import sleep


class System:
    ...


class Player:
    def __init__(self, name, symbol):
        self.NAME = name
        self.SYMBOL = symbol

    def get_symbol(self):
        return Fore.LIGHTWHITE_EX + f"{self.NAME} - {self.SYMBOL}" + Style.RESET_ALL


player1 = Player("PLAYER1", Fore.LIGHTRED_EX + "X" + Style.RESET_ALL)
player2 = Player("PLAYER2", Fore.LIGHTBLUE_EX + "O" + Style.RESET_ALL)


class Data:
    STAR = "*"
    BOARD_LINE = Fore.LIGHTWHITE_EX + "|" + Style.RESET_ALL

    def __init__(self):
        self.BOARD = [self.STAR]*9
        self.PLAYER_TUPLE = (player1, player2)

    def get_symbols(self):
        print()
        for player in self.PLAYER_TUPLE:
            print(player.get_symbol())

    def show_board(self):
        for line_indx in range(0, len(self.BOARD) + 3, 3):
            print(*self.BOARD[line_indx - 3:line_indx], sep=self.BOARD_LINE)

    def combinations(self):
        vertical = list(zip(self.BOARD[:3], self.BOARD[3:6], self.BOARD[6:]))
        horizontal = list(zip(vertical[0], vertical[1], vertical[2]))
        diagonal_left = [self.BOARD[2], self.BOARD[4], self.BOARD[6]]
        diagonal_right = [self.BOARD[0], self.BOARD[4], self.BOARD[8]]
        all_lines = [vertical, horizontal, diagonal_right, diagonal_left]
        combination_list = [["X"]*3, ["O"]*3]
        for line in all_lines:
            if line in combination_list:
                print("Yey!")
                break


    def change_board(self, mover, position):
        self.BOARD[position-1] = mover.SYMBOL

    def move(self, mover):
        while True:
            print(Fore.CYAN + f">>> {mover.NAME}'s move." + Style.RESET_ALL)
            try:
                position = int(input("<<< "))
                if position not in range(1, 10):
                    print(Fore.LIGHTRED_EX + "Enter total in range 1-9\n" + Style.RESET_ALL)
                else:
                    self.change_board(mover, position)
                    break
            except ValueError:
                print(Fore.LIGHTRED_EX + "Enter total in range 1-9\n" + Style.RESET_ALL)

    def start_game(self):
        self.get_symbols()
        self.show_board()
        while any(["*" in self.BOARD]) or not self.combinations():
            self.move(player1)
            self.show_board()


class Game:

    def settings(self):
        while True:
            print(Fore.LIGHTRED_EX + "\n>>> Settings" + Style.RESET_ALL)
            print(Fore.BLUE + "1. Set name\n"
                              "2. Music\n"
                              "3. Leave" + Style.RESET_ALL)
            answer = input("<<< ")
            match answer.upper():
                case "1" | "SET NAME":
                    print(Fore.LIGHTWHITE_EX + "Coming soon..." + Style.RESET_ALL)
                case "2" | "MUSIC":
                    print(Fore.LIGHTWHITE_EX + "Coming soon..." + Style.RESET_ALL)
                case "3" | "LEAVE":
                    break
                case _:
                    print(Fore.LIGHTRED_EX + "Select one of the options shown above!" + Style.RESET_ALL)

    def main_menu(self):
        while True:
            print(Fore.LIGHTRED_EX + "\n>>> Main Menu" + Style.RESET_ALL)
            print(Fore.LIGHTBLUE_EX + "1. Play\n"
                              "2. Settings\n"
                              "3. Quit" + Style.RESET_ALL)
            answer = input("<<< ")
            match answer.upper():
                case "1" | "PLAY":
                    data.start_game()
                case "2" | "SETTINGS":
                    print(Fore.LIGHTWHITE_EX + "Coming soon..." + Style.RESET_ALL)
                case "3" | "QUIT":
                    print(Fore.LIGHTCYAN_EX + "Goodbye!" + Style.RESET_ALL)
                    sleep(0.5)
                    break
                case _:
                    print(Fore.LIGHTRED_EX + "Select one of the options shown above!" + Style.RESET_ALL)


data = Data()

game = Game()
game.main_menu()
