import pygame
from random import random, shuffle, randint
import time
from colorama import Fore, Style

pygame.init()

monologues = ["Well, well, well.", "Okay.", "Good!", "Hmm...", "Well done!", "Ahh!", "One more?"]


def music():
    pygame.mixer.music.load("ElectricJazz.wav")
    pygame.mixer.music.play(-1)


def get_points(opponent):
    opponent.POINTS = sum(opponent.CARD_LIST)
    if 11 in opponent.CARD_LIST and opponent.POINTS > 21:
        opponent.POINTS -= 10


def first_distribution(opponent, deck):
    for _ in range(2):
        opponent.CARD_LIST.append(deck[0])
        del deck[0]
    get_points(opponent)


def answer_counting(answer_counter):
    return all(pair in answer_counter for pair in (("DEALER", "STAND"), ("PLAYER", "STAND")))


def victory_checking(pl1, pl2):  # Class ex

    def get_winner(winner):
        dealer_cards = Fore.BLUE + ", ".join(pl2.CARD_LIST) + Style.RESET_ALL
        player_cards = Fore.BLUE + ", ".join(pl1.CARD_LIST) + Style.RESET_ALL
        dealer_points = Fore.RED + f"{pl2.POINTS}" + Style.RESET_ALL
        player_points = Fore.RED + f"{pl1.POINTS}" + Style.RESET_ALL
        print(Fore.RED + f"\n{winner}!\n" + Style.RESET_ALL)
        print(f"Dealer's points: {dealer_points}; Dealer's hand: ({dealer_cards})\n"
              f"Your points: {player_points}; Your hand: ({player_cards})\n")

    print("*** Winner is... ***")
    time.sleep(5)
    match (pl1.POINTS, pl2.POINTS):
        case (x, y) if x == y:
            get_winner("DRAW")
        case (x, y) if x >= 21 and y >= 21:
            if x < y:
                get_winner(pl1.NAME)
            else:
                get_winner(pl2.NAME)
        case (x, y) if x <= 21 and y <= 21:
            if x > y:
                get_winner(pl1.NAME)
            else:
                get_winner(pl2.NAME)
        case (x, y) if x <= 21 < y:
            get_winner(pl1.NAME)
        case (x, y) if y <= 21 < x:
            get_winner(pl2.NAME)
        case _:
            print(Fore.RED + "Error while checking points!" + Style.RESET_ALL)  # Looking for errors

def rename_first_key(answer_counter):
    if len(answer_counter) >= 2:
        answer_counter[:] = answer_counter[:2]


class Data:
    def __init__(self):
        self.deck = [num for num in range(1, 12)]
        self.shuffling_deck()

    def shuffling_deck(self):
        for _ in range(randint(1, 10)):
            shuffle(self.deck)

    @staticmethod
    def rules():
        print(Fore.RED + "Click Enter to continue:\n" + Style.RESET_ALL)
        rules_tuple = (Fore.BLUE + "Simple BlackJack Rules:\n",
                       "1. The deck contains 11 cards.",
                       "2. The game lasts one round.",
                       "3. The player whose total score is closest to 21, wins.",
                       "4. Players who exceed 21 points lose the round!",
                       "The round ends when:",
                       "- Each player chooses to Stand.",
                       "- A player exceeds 21 points.\n",
                       "Good Luck!" + Style.RESET_ALL)
        for rule in rules_tuple:
            print(rule, end="")
            input()

    @staticmethod
    def get_move_info(suspect, player, dealer):
        player_cards = ", ".join(player.CARD_LIST)
        print(Fore.RED + "\n*** Move Info: ***")
        print(Fore.LIGHTBLUE_EX +
              f"Person: {suspect.NAME}\n"
              f"Choice: {suspect.ANSWER}\n\n"
              f"PLAYER's points: {player.POINTS}\n"
              f"PLAYER's hand: {player_cards}\n\n"
              f"DEALER's points: {dealer.POINTS}\n"
              f"DEALER's hand: {dealer.CARD_LIST[0]} + XXX\n"
              + Style.RESET_ALL)


class Human:
    NAME = "PLAYER"

    def __init__(self):
        self.POINTS = 0
        self.CARD_LIST = list()
        self.ANSWER = ""

    def hit_move(self, deck):
        self.ANSWER = "HIT".upper()
        card = deck[0]
        self.CARD_LIST.append(card)
        get_points()



    def move(self, deck, answer_counter, dealer):
        if self.POINTS < 21 and dealer.POINTS <= 21:
            self.ANSWER = ""
            while self.ANSWER.upper() not in ("2", "STAND"):
                if self.POINTS >= 21:
                    self.ANSWER = "STAND".upper()
                    answer_counter.append((self.NAME, self.ANSWER))
                    break
                else:
                    print(Fore.RED + "Your turn!")
                    print(Fore.BLUE + "1. HIT - Take another card.\n"
                                      "2. STAND - Keep Your hand. End Your turn." + Style.RESET_ALL)
                    self.ANSWER = input("-----> ").upper()
                    match self.ANSWER.upper():
                        case "1" | "HIT":
                            self.hit_move(deck)
                        case "2" | "STAND":
                            self.ANSWER = "STAND".upper()

                        case _:
                            ...
