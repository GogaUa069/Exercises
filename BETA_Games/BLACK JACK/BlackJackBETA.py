from colorama import Fore, Style
from random import shuffle, choice
from time import sleep

print(Fore.RED + "Have the CLOSEST number to 21\n" + Style.RESET_ALL)


class GameData:
    def __init__(self):
        self.deck = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "11": (1, 11)}
        self.cards = list(self.deck.keys())
        self.values = list(self.deck.values())
        self.answer_counter = dict()
        shuffle(self.cards)
        self.monologues = ["Well, well, well", "Okay", "Good!", "Hmm...", "Well done!", "Ahh!", "One more?",
                           "Good decision!"]

    def first_distribution(self, player):
        for _ in range(2):
            card = self.cards[0]
            player.CARD_LIST.append(card)
            player.POINTS += self.deck[card]
            del self.cards[0]

    def answer_counting(self):
        person_list = list(self.answer_counter.keys())
        answer_list = list(self.answer_counter.values())
        if (len(self.answer_counter) == 2 and
                "DILLER" in person_list and
                "PLAYER" in person_list and
                answer_list == ["STAY", "STAY"]):
            return True
        return False

    @classmethod
    def is_victory(cls, player1, player2):
        pl1_sub = 21 - player1.NAME
        pl2_sub = 21 - player2.NAME

        def winner(player):
            return Fore.RED + f"{player.NAME}!" + Style.RESET_ALL

        print(Fore.BLUE + f"*** WINNER IS... ***" + Style.RESET_ALL)
        sleep(5)
        if pl1_sub < pl2_sub and player2 < 0:
            winner(player2.NAME)
        elif pl1_sub < pl2_sub and player2 > 0:
            winner(player1.NAME)
        elif pl1_sub > pl2_sub and player2 < 0:
            winner(player1.NAME)
        elif pl1_sub > pl2_sub and player2 > 0:
            winner(player2.NAME)
        elif pl1_sub == pl2_sub:
            print("DRAW!")


class Human(GameData):
    CARD_LIST = list()

    def __init__(self):
        self.NAME = "YOU"
        self.POINTS = 0
        self.ANSWER = str()
        self.POINTS = 0
        GameData.__init__(self)
        GameData.first_distribution(self, )  # Human ex. there!     <----------------

    def get_move_info(self):
        print(Fore.BLUE + "***INFO***" + Style.RESET_ALL)
        print(f"Decision: {self.ANSWER}")
        print(f"You points: {self.get_points()}")
        print(f"Your cards: {self.CARD_LIST}")
        print(f"Diller's points: {"..."}")  # Diller's points there     <--------------------
        print(f"Diller's cards: X + {"..."}")  # Diller's cards there     <----------------

    def move(self):
        print("Your turn!\n"
              "1. HIT - Get one more card.\n"
              "2. STAY - Stay with your cards.\n")
        if self.POINTS < 21:
            while self.ANSWER.upper() != "STAY":
                self.ANSWER = input("-----> ")
                match self.ANSWER.upper():
                    case "HIT" | "1":
                        self.CARD_LIST.append(self.cards[0])
                        del self.cards[0]
                    case "STAY" | "2":
                        break
                    case _:
                        print("Enter HIT/STAY")
            print(choice(self.monologues), "\n")
            self.answer_counter[self.NAME] = self.ANSWER
            self.get_move_info()

    def get_points(self):
        self.POINTS = 0
        for card in self.CARD_LIST:
            self.POINTS += self.deck[card]
            if card == "11" and self.POINTS > 21:
                self.POINTS -= 10
        return self.POINTS


human1 = Human()
human1.get_move_info()
