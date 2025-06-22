import time


class TicTacToe:

    while True:
        print("\033[34m{}".format("Welcome to the Tic-tac-toe!"))
        player1 = 'X'
        player2 = 'O'
        board = ['*']*10
        numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        num = 0
        counter = 0
        answer_play = input("\033[0m{}".format("Enter 'play' to play, or 'leave' to leave: "))
        if answer_play == 'leave':
            print("Bye!")
            time.sleep(1.5)
            break
        else:
            print("\033[31m{}".format(f"Player1: {player1}\nPlayer2: {player2}"))
            while True:

                while num not in numbers_list:
                    num = int(input("\033[0m{}".format("Player1, enter the number *(1-9): ")))
                    if num not in numbers_list:
                        continue
                numbers_list.remove(num)
                board[num-1] = 'X'
                print('\n')
                print(board[6] + '|' + board[7] + '|' + board[8])
                print(board[3] + '|' + board[4] + '|' + board[5])
                print(board[0] + '|' + board[1] + '|' + board[2])
                print('\n')
                counter += 1
                if counter == 9:
                    if player1 == 'X':
                        if board[0] + board[1] + board[2] == 'XXX':
                            print("Player1 won!")
                            break
                        elif board[3] + board[4] + board[5] == 'XXX':
                            print("Player1 won!")
                            break
                        elif board[6] + board[7] + board[8] == 'XXX':
                            print("Player1 won!")
                            break
                        elif board[0] + board[3] + board[6] == 'XXX':
                            print("Player1 won!")
                            break
                        elif board[1] + board[4] + board[7] == 'XXX':
                            print("Player1 won!")
                            break
                        elif board[2] + board[5] + board[8] == 'XXX':
                            print("Player1 won!")
                            break
                        elif board[0] + board[4] + board[8] == 'XXX':
                            print("Player1 won!")
                            break
                        elif board[2] + board[4] + board[6] == 'XXX':
                            print("Player1 won!")
                            break
                        else:
                            print('Tie!')
                            break
                elif counter < 9:
                    if player1 == 'X':
                        if board[0] + board[1] + board[2] == 'XXX':
                            print("Player1 won!")
                            break
                        elif board[3] + board[4] + board[5] == 'XXX':
                            print("Player1 won!")
                            break
                        elif board[6] + board[7] + board[8] == 'XXX':
                            print("Player1 won!")
                            break
                        elif board[0] + board[3] + board[6] == 'XXX':
                            print("Player1 won!")
                            break
                        elif board[1] + board[4] + board[7] == 'XXX':
                            print("Player1 won!")
                            break
                        elif board[2] + board[5] + board[8] == 'XXX':
                            print("Player1 won!")
                            break
                        elif board[0] + board[4] + board[8] == 'XXX':
                            print("Player1 won!")
                            break
                        elif board[2] + board[4] + board[6] == 'XXX':
                            print("Player1 won!")
                            break

                while num not in numbers_list:
                    num = int(input("Player2, enter the number *(1-9): "))
                    if num not in numbers_list:
                        continue
                numbers_list.remove(num)
                board[num - 1] = 'O'
                print('\n')
                print(board[6] + '|' + board[7] + '|' + board[8])
                print(board[3] + '|' + board[4] + '|' + board[5])
                print(board[0] + '|' + board[1] + '|' + board[2])
                print('\n')
                counter += 1
                if counter == 9:
                    if player2 == 'O':
                        if board[0] + board[1] + board[2] == 'OOO':
                            print("Player2 won!")
                            break
                        elif board[3] + board[4] + board[5] == 'OOO':
                            print("Player2 won!")
                            break
                        elif board[6] + board[7] + board[8] == 'OOO':
                            print("Player2 won!")
                            break
                        elif board[0] + board[3] + board[6] == 'OOO':
                            print("Player2 won!")
                            break
                        elif board[1] + board[4] + board[7] == 'OOO':
                            print("Player2 won!")
                            break
                        elif board[2] + board[5] + board[8] == 'OOO':
                            print("Player2 won!")
                            break
                        elif board[0] + board[4] + board[8] == 'OOO':
                            print("Player2 won!")
                            break
                        elif board[2] + board[4] + board[6] == 'OOO':
                            print("Player2 won!")
                            break
                        else:
                            print("Tie!")
                            break
                elif counter < 9:
                    if player2 == 'O':
                        if board[0] + board[1] + board[2] == 'OOO':
                            print("Player2 won!")
                            break
                        elif board[3] + board[4] + board[5] == 'OOO':
                            print("Player2 won!")
                            break
                        elif board[6] + board[7] + board[8] == 'OOO':
                            print("Player2 won!")
                            break
                        elif board[0] + board[3] + board[6] == 'OOO':
                            print("Player2 won!")
                            break
                        elif board[1] + board[4] + board[7] == 'OOO':
                            print("Player2 won!")
                            break
                        elif board[2] + board[5] + board[8] == 'OOO':
                            print("Player2 won!")
                            break
                        elif board[0] + board[4] + board[8] == 'OOO':
                            print("Player2 won!")
                            break
                        elif board[2] + board[4] + board[6] == 'OOO':
                            print("Player2 won!")
                            break
        break


my_game = TicTacToe()
print(my_game)


def restart():

    question = ''
    while question != "restart" and question != "leave":
        while question != "leave":
            print('*'*10)
            question = input("\033[31m{}".format("restart: 'restart'\nleave: 'leave'\nEnter: "))
            if question == 'leave':
                print('Bye!')
                time.sleep(5)
                break
            elif question == 'restart':
                print(my_game)


restart()
