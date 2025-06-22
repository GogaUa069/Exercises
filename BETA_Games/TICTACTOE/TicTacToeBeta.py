import random
import time


def step_stop():
    print()
    time.sleep(0.5)


class AllItems:
    symbols = ["X", "O"]
    random.shuffle(symbols)

    def __init__(self):
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.position = 0
        self.counter = 0
        self.board = ["*"] * 10
        self.positions = [i for i in range(1, 10)]
        self.players = {"Player1": self.symbols[0], "Player2": self.symbols[1]}
        self.values = {self.symbols[0]: "Player1", self.symbols[1]: "Player2"}

    def show_board(self):
        print("")
        print(f"{self.board[6]}|{self.board[7]}|{self.board[8]}")
        print(f"{self.board[3]}|{self.board[4]}|{self.board[5]}")
        print(f"{self.board[0]}|{self.board[1]}|{self.board[2]}")
        print("")

    def start(self):
        print(f"Player1: {self.players["Player1"]}")
        print(f"Player2: {self.players["Player2"]}")
        self.show_board()


class Moves(AllItems):
    def __init__(self):
        AllItems.__init__(self)

    def move(self, person):
        print(f"{person}, your move.\nEnter amount in range 1-9 (If it's possible)")
        step_stop()
        while self.position not in self.positions:
            try:
                self.position = int(input("-----> "))
                if 1 <= self.position <= 9 and self.position not in self.positions:
                    print("This number is already taken!")
                    step_stop()
                elif self.position < 1 or self.position > 9:
                    print("Your total is out of range!")
                    step_stop()
            except ValueError:
                print("Please, enter NUMBER!")
                step_stop()

        self.positions.remove(self.position)
        self.board[self.position-1] = self.players[person]
        self.position = 0
        self.show_board()
        self.counter += 1


class WinnerCheck(Moves):
    def __init__(self):
        Moves.__init__(self)

    def winner_checker(self):
        self.vertical = list(zip(self.board[:3], self.board[3:6], self.board[6:]))
        self.horizontal = list(zip(self.vertical[0], self.vertical[1], self.vertical[2]))
        self.lines = self.vertical + self.horizontal
        combinations = (("X", "X", "X"), ("O", "O", "O"))
        winner = None
        flag = False
        for i in self.lines:
            if i in combinations:
                winner = self.values[i[0]]
                flag = True
                break
        if flag:
            print("Winner is...")
            time.sleep(3)
            print(f"{winner}!!!")
        else:
            if self.counter < 9:
                pass
            if self.counter == 9:
                print("DRAW! Would you play again?)")


moves = Moves()
checker = WinnerCheck()


def game():
    moves.start()
    while True:
        moves.move("Player1")
        checker.winner_checker()
        moves.move("Player2")
        checker.winner_checker()


game()
