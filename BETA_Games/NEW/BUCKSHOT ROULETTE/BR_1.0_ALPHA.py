# Add rounds with harder bullet combinations

from colorama import Fore, Style
from random import randint, shuffle, choice
import time
import pygame

pygame.init()


class SoundtrackPlayer:
    SHOTGUN_LOAD_SOUND = pygame.mixer.Sound(r"Soundtracks/ShotgunLoadSound.wav")
    SHOTGUN_SHOT_SOUND = pygame.mixer.Sound(r"Soundtracks/ShotgunShotSound.wav")
    MAIN_SOUNDTRACK = r"Soundtracks/ElectricJazzSoundtrack.wav"

    @staticmethod
    def soundtrack_player(soundtrack):
        pygame.mixer.music.load(soundtrack)
        pygame.mixer.music.play(-1)


soundtrack_player = SoundtrackPlayer()


class Communicate:
    def __init__(self, text: str, color):
        self.TEXT = text
        self.COLOR = color

    def __call__(self, *args, **kwargs):
        print(self.COLOR + self.TEXT + Style.RESET_ALL)


wrong_choice_type_communicate = Communicate("Enter number!", Fore.LIGHTRED_EX)
wrong_choice_communicate = Communicate("Select one of the options shown above!", Fore.LIGHTRED_EX)
round_starting_communicate = Communicate("Dealing items and loading the shotgun...", Fore.CYAN)


class SystemPrompt:
    MAX_HP = 5
    MIN_DAMAGE, MAX_DAMAGE = 1, 2
    LOW_MUSIC, NORMAL_MUSIC = 0.3, 1
    RAND_RANGE = (1, 4)
    HINTS = [...]

    @staticmethod
    def set_move(pl1, pl2):
        pl1.IS_NEXT = not pl1.IS_NEXT
        pl2.IS_NEXT = not pl2.IS_NEXT


system = SystemPrompt()


class Shotgun:

    def __init__(self):
        self.AMMO = list()
        self.DAMAGE = system.MIN_DAMAGE

    def load_ammo(self):
        pygame.mixer.music.set_volume(system.LOW_MUSIC)
        soundtrack_player.SHOTGUN_LOAD_SOUND.play()

        while True:
            live, blank = randint(*system.RAND_RANGE), randint(*system.RAND_RANGE)
            if blank - live < 3:
                break

        self.AMMO.extend(["BLANK"]*blank)
        self.AMMO.extend(["LIVE"]*live)
        shuffle(self.AMMO)

        time.sleep(len(self.AMMO))
        soundtrack_player.SHOTGUN_LOAD_SOUND.stop()
        pygame.mixer.music.set_volume(system.NORMAL_MUSIC)

    def shot(self, who, at):
        at.HEALTH -= self.DAMAGE
        del self.AMMO[0]
        system.set_move(player, dealer)
        self.shot_info(who, at)

    def shot_info(self, who, at):
        soundtrack_player.SHOTGUN_SHOT_SOUND.play()
        print(Fore.LIGHTWHITE_EX + f"Shot INFO:\n"
                                   f"Who shot: {who.NAME}\n"
                                   f"Shot at: {at.NAME}\n"
                                   f"Bullet type: {self.AMMO[0]}\n"
                                   f"{at}'s HEALTH: {at.HEALTH}" + Style.RESET_ALL)


shotgun = Shotgun()


class Player:
    def __init__(self, name):
        self.NAME = name
        self.HEALTH = system.MAX_HP
        self.ITEMS = list()
        self.IS_NEXT = False

    def show_items(self):
        for indx, item in enumerate(set(self.ITEMS)):
            print(f"{indx+1}. {item.NAME} - {self.ITEMS.count(item)} - {item.DESCRIPTION}")

    def __repr__(self):
        return (f"NAME: {self.NAME}\n"
                f"HEALTH: {self.HEALTH}\n"
                f"ITEMS: {[item.NAME for item in self.ITEMS]}\n"
                f"IS_NEXT: {self.IS_NEXT}\n")


player = Player("PLAYER")
dealer = Player("DEALER")


class Item:
    def __init__(self, name: str, description: str, func):
        self.NAME = name
        self.DESCRIPTION = description
        self.FUNC = func

    def __call__(self, who, *args, **kwargs):
        return self.FUNC(who)


cigarettes = Item("CIGARETTES", "+1 HP after smoking", lambda who: who.HEALTH + 1)
beer = Item("BEER", "Extracts the next bullet", lambda: shotgun.AMMO.pop(0))
loupe = Item("LOUPE", "Shows the next bullet type", lambda: shotgun.AMMO[0])
knife = Item("KNIFE", "Deals 2x HP damage", lambda: setattr(shotgun, "DAMAGE", system.MAX_DAMAGE))
manacles = Item("MANACLES", "Grants a second move", lambda: True)
phone = Item("PHONE", "Gives a hint", lambda: choice(system.HINTS))


class Game:
    ITEMS = [cigarettes, beer, loupe, knife, manacles, phone]

    def check_round_end(self):
        if player.HEALTH <= 0 or dealer.HEALTH <= 0:
            ...

    def give_item(self, who, times=1):
        for _ in range(times):
            who.ITEMS.append(choice(self.ITEMS))
        who.ITEMS = sorted(who.ITEMS, key=lambda x: self.ITEMS.index(x))

    def round_starting(self):
        soundtrack_player.soundtrack_player(soundtrack=soundtrack_player.MAIN_SOUNDTRACK)
        round_starting_communicate()

        self.give_item(player, times=3)
        self.give_item(dealer, times=3)
        shotgun.load_ammo()
        player.IS_NEXT = True

        print(Fore.CYAN + "Round 1 starting!".upper() + Style.RESET_ALL)


game = Game()


class PlayerMove:

    @staticmethod
    def shotgun_choice():
        while True:
            print(Fore.LIGHTRED_EX + ">>> SHOTGUN")
            print(Fore.LIGHTBLUE_EX + f"1. {player.NAME} (YOU)\n"
                                      f"2. {dealer.NAME}" + Style.RESET_ALL)
            answer = input("<<< ")
            match answer.upper():
                case "YOU" | "PLAYER" | "1":
                    shotgun.shot(player, player)
                    break
                case "DEALER" | "2":
                    shotgun.shot(dealer, player)
                    break
                case _:
                    wrong_choice_communicate()

    @staticmethod
    def items_choice():
        while True:
            print(Fore.LIGHTRED_EX + ">>> ITEMS")
            player.show_items()
            print("BACK - YOUR MOVE")
            try:
                answer = int(input("<<< "))
                if answer in range(1, len(game.ITEMS)):
                    game.ITEMS[answer-1](player)
                elif answer == len(game.ITEMS) + 1:
                    break
                else:
                    wrong_choice_communicate()
            except TypeError:
                wrong_choice_type_communicate()

    def main_choice_menu(self):
        while True:
            print(Fore.LIGHTRED_EX + ">>> YOUR MOVE")
            print(Fore.LIGHTBLUE_EX + "1. Shotgun\n"
                                      "2. Items" + Style.RESET_ALL)
            answer = input("<<< ")
            match answer.upper():
                case "SHOTGUN" | "1":
                    self.shotgun_choice()
                    break
                case "ITEMS" | "2":
                    self.items_choice()
                    break
                case _:
                    wrong_choice_communicate()


game.round_starting()
player_move = PlayerMove()
player_move.main_choice_menu()
