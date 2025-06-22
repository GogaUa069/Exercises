from random import choice


class Cell:

    def __init__(self, is_mine=None, symbol=None, is_open=False, mines_around=0):
        self.is_mine = is_mine
        self.symbol = symbol
        self.is_open = is_open
        self.mines_around = mines_around


class GameBoard:
    def __init__(self, n, m):
        self.N = n
        self.M = m
        self.board = [[Cell(is_mine=0, symbol="#") for _ in range(self.N)] for _ in range(self.N)]
        self.row = None
        self.column = None
        self.counter = 0

    def get_mines(self):
        indexes = [i for i in range(len(self.board))]

        for _ in range(self.M):
            while True:
                indx1 = choice(indexes)
                indx2 = choice(indexes)
                cell = self.board[indx1][indx2]
                if cell.is_mine != 1:
                    cell.is_mine = 1
                    break
                else:
                    continue

        self.show()

    def mines_around_cell(self):
        for i in range(len(self.board)-1):
            for j in range(len(self.board)-1):
                this_cell = self.board[i][j]
                if this_cell.is_mine == 1:
                    continue
                else:
                    cell = self.board
                    indexes = {"left_up": cell[i-1][j-1].is_mine, "up": cell[i-1][j].is_mine, "right_up": cell[i-1][j+1].is_mine,
                               "left": cell[i][j-1].is_mine, "right": cell[i][j+1].is_mine,
                               "left_down": cell[i+1][j-1].is_mine, "down": cell[i+1][j].is_mine, "right_down": cell[i+1][j+1].is_mine}
                    # 1
                    if i == 0 and j == 0:
                        this_cell.mines_around = indexes["down"] + indexes["right_down"] + indexes["right"]
                    # 3
                    elif i == 0 and j not in (0, len(self.board)):
                        this_cell.mines_around = indexes["left"] + indexes["left_down"] + indexes["down"] + indexes["right_down"] + indexes["right"]
                    # 7
                    elif i not in (0, len(self.board)) and j == 0:
                        this_cell.mines_around = indexes["up"] + indexes["right_up"] + indexes["right"] + indexes["right_down"] + indexes["down"]
                    # 9
                    elif i not in (0, len(self.board)) and j not in (0, len(self.board)):
                        this_cell.mines_around = sum([indexes["left_up"], indexes["up"], indexes["right_up"],
                                                      indexes["left"], indexes["right"],
                                                      indexes["left_down"], indexes["down"], indexes["right_down"]])
        length = len(self.board)-1
        for i in range(length+1):
            for j in range(length+1):
                this_cell = self.board[i][j]
                if this_cell.is_mine == 1:
                    continue
                else:
                    if i == 0 and j == length:
                        this_cell.mines_around = self.board[i+1][j].is_mine + self.board[i+1][j-1].is_mine + self.board[i][j-1].is_mine
                    elif i == length and j == 0:
                        this_cell.mines_around = self.board[i-1][j].is_mine + self.board[i-1][j+1].is_mine + self.board[i][j+1].is_mine
                    elif i == length and j == length:
                        this_cell.mines_around = self.board[i][j-1].is_mine + self.board[i-1][j-1].is_mine + self.board[i-1][j].is_mine
                    elif i == length and j not in (0, length):
                        this_cell.mines_around = self.board[i-1][j-1].is_mine + self.board[i-1][j].is_mine + self.board[i-1][j+1].is_mine + self.board[i][j-1].is_mine + self.board[i][j+1].is_mine
                    elif i not in (0, length) and j == length:
                        this_cell.mines_around = self.board[i-1][j].is_mine + self.board[i-1][j-1].is_mine + self.board[i][j-1].is_mine + self.board[i+1][j-1].is_mine + self.board[i+1][j].is_mine

    def get_indx(self):
        print()
        print("Enter ROW of cell.")
        self.row = int(input("-----> "))
        print()
        print("Enter COLUMN of cell")
        self.column = int(input("-----> "))
        if self.board[self.row-1][self.column-1].symbol == "#":
            self.counter += 1
        print()

    def change_symbol(self):
        self.get_indx()
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                cell = self.board[i][j]
                if i+1 == self.row and j+1 == self.column:
                    cell.is_open = True
                    match cell.is_mine:
                        case 1:
                            cell.symbol = "*"
                        case 0:
                            cell.symbol = cell.mines_around

    def show(self):
        for row in self.board:
            for cell in row:
                print(cell.symbol, end=" ")
            print()


my_game = GameBoard(5, 5)


def game():
    my_game.get_mines()
    my_game.mines_around_cell()
    while True:
        my_game.change_symbol()
        my_game.show()
        if my_game.counter == my_game.N**2:
            break


game()
