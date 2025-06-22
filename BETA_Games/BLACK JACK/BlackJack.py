from colorama import Fore, Style
from random import shuffle, choice
from time import sleep


cards = [str(i) for i in range(1, 12)]
values = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "11": (1, 11)}
monologues = ["Well, well, well", "Okay", "Good!", "Hmm...", "Well done!", "Ahh!", "One more?", "Good decision!"]
print(Fore.RED + "Task: Have the CLOSEST number to 21\n" + Style.RESET_ALL)


def is_victory(pl1, pl2, counter):  # BETA ****************************************
    players = counter.keys()
    answers = counter.values()
    pl1_sub = 21 - PlHuman.POINTS
    pl2_sub = 21 - PlBot.POINTS

    def winner(pl):
        return Fore.BLUE + f"{pl.NAME}!" + Style.RESET_ALL

    if all(players) == "PLAYER1" or all(players) == "PLAYER2" or not all(answers) == "STAY" or len(counter) != 2 or pl1 == pl2 == 0:
        pass
    else:
        print("*** WINNER IS... ***")
        sleep(5)
        if pl1_sub < pl2_sub and pl2 < 0:
            winner(pl2.NAME)
        elif pl1_sub < pl2_sub and pl2 > 0:
            winner(pl1.NAME)
        elif pl1_sub > pl2_sub and pl2 < 0:
            winner(pl1.NAME)
        elif pl1_sub > pl2_sub and pl2 > 0:
            winner(pl2.NAME)
        elif pl1_sub == pl2_sub:
            print("Draw!")
        elif len(self.deck) == 0:
            pass
        elif a == 0 and b == 0:
            return False
        else:
            return False
        return True


class GameData:

    def __init__(self):
        self.values = values
        self.deck = cards
        self.STAY_COUNTER = dict()
        self.CARD_LIST = list()
        self.POINTS = 0
        self.ANSWER = str()

        shuffle(self.deck)
        self.first_distribution(pl1.NAME)
        self.first_distribution(pl2.NAME)

    def first_distribution(self, player):
        for _ in range(2):
            player.CARD_LIST.append(self.deck[0])
            del self.deck[0]

    def stay_addition(self, player):
        self.STAY_COUNTER[player.NAME.upper()] = player.ANSWER
        first_key = next(iter(self.STAY_COUNTER))
        del my_dict[first_key]



class PlHuman(GameData):

    def __init__(self):
        self.NAME = "PLAYER1"
        GameData.__init__(self)

    def get_move_info(self):
        print(Fore.BLUE + "\n*** INFO ***" + Style.RESET_ALL)
        print(f"Decision: {self.ANSWER}")
        print(f"Your points: {self.POINTS}")
        print(f"Your cards: {", ".join(self.CARD_LIST)}\n")

    def move(self):
        print("Your turn! Enter:\nHIT/1 - Get one more card.\nSTAY/2 - Stay with your cards.\n")
        while self.ANSWER.lower() != "stay":
            self.ANSWER = input("-----> ")
            match self.ANSWER.lower():
                case "hit" | "1":
                    self.CARD_LIST.append(self.deck[0])
                    del self.deck[0]
                    self.get_points()
                    self.ANSWER = "HIT"
                    print(choice(monologues))
                case "stay" | "2":
                    self.stay_addition(...)
                case _:
                    print("Please, enter: HIT/1 or STAY/2")
        self.get_move_info()

    def get_points(self):
        for card in self.CARD_LIST:
            self.POINTS += self.values[card]
            if card == "11" and self.POINTS + 11 > 21:
                self.POINTS -= 10


class PlBot(GameData):

    def __init__(self):
        self.NAME = "PLAYER2"
        GameData.__init__(self)

    def hit_or_stay(self):
        next_card = self.deck[0]
        next_value = self.values[next_card]
        if next_value + self.POINTS <= 21:
            hit()
        else:
            stay()
        if next_value == 11:
            if 11 + self.POINTS <= 21:
                hit()
            else:
                if 1 + self.POINTS <= 21:
                    hit()
                else:
                    stay()


    def move(self):
        print("*** Opponent's move ***")
        sleep(5)

        def hit():
            self.ANSWER = "HIT"
            self.get_card("HOFFMAN")
            self.POINTS += next_value

        def stay():
            self.ANSWER = "STAY"

        while self.ANSWER != "STAY":
            self.hit_or_stay()

    def get_points(self):
        points = list()
        for card in self.CARD_LIST[1:]:
            points.append(self.values[card])
        return sum(points)

    def get_move_info(self):
        print(Fore.BLUE + "*** Info ***" + Style.RESET_ALL)
        print(f"Decision: {self.ANSWER}")
        print(f"Opponent's points: X + {PlBot.get_points(self)}")
        print(f"Opponent's cards: X + {", ".join(self.CARD_LIST[1:])}\n")


victory = is_victory(pl1, pl2, data.STAY_COUNTER)


data = GameData()


def game():
    pl1 = PlHuman()
    pl2 = PlBot()
    data.first_distribution(pl1)
    data.first_distribution(pl2)
    while not victory():
        pl1.move()
        victory()
        pl2.move()
        victory()


game()
