from colorama import Fore, Style
from random import randint, shuffle, choice, uniform
import time
import pygame

pygame.init()

LOW_MUSIC, NORMAL_MUSIC = 0.3, 1


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
    def __init__(self, name, color):
        self.NAME = name
        self.COLOR = color

    def __call__(self, *args, **kwargs):
        comm = self.NAME(*args, **kwargs) if callable(self.NAME) else self.NAME
        print(self.COLOR + comm + Style.RESET_ALL)


wrong_type_comm = Communicate("Invalid input type!", Fore.LIGHTRED_EX)
wrong_answer_comm = Communicate("Select one of the options shown above!", Fore.LIGHTRED_EX)
round_starting_comm1 = Communicate("Dealing items and loading the shotgun...", Fore.CYAN)
round_starting_comm2 = Communicate(lambda x: f"STARTING ROUND {x}", Fore.CYAN)
remaining_bullets = Communicate(lambda: f"Remaining bullets: {len(shotgun.AMMO)}", Fore.CYAN)


class Shotgun:
    MIN_DAMAGE, MAX_DAMAGE = 1, 2
    RAND_RANGE_BULLETS = (1, 4)

    def __init__(self):
        self.AMMO = list()
        self.DAMAGE = self.MIN_DAMAGE

    def load_ammo(self):
        pygame.mixer.music.set_volume(LOW_MUSIC)
        soundtrack_player.SHOTGUN_LOAD_SOUND.play()

        total_bullets = randint(5, 8)
        bullet_ratio = uniform(0.5, 0.7)

        live = round(total_bullets * bullet_ratio)
        blank = total_bullets - live

        self.AMMO.extend(["BLANK"]*blank)
        self.AMMO.extend(["LIVE"]*live)
        shuffle(self.AMMO)
        time.sleep(len(self.AMMO))
        soundtrack_player.SHOTGUN_LOAD_SOUND.stop()
        pygame.mixer.music.set_volume(NORMAL_MUSIC)

    def shot(self, who, at):
        soundtrack_player.SHOTGUN_SHOT_SOUND.play()
        at.HEALTH -= self.DAMAGE
        self.shot_info(who, at)
        del self.AMMO[0]
        self.DAMAGE = self.MIN_DAMAGE

    def shot_info(self, who, at):
        time.sleep(1)
        print(Fore.LIGHTWHITE_EX + f"Shot INFO:\n"
                                   f"Who shot: {who.NAME}\n"
                                   f"Shot at: {at.NAME}\n"
                                   f"Bullet type: {self.AMMO[0]}\n"
                                   f"{at.NAME}'s health: {at.HEALTH}" + Style.RESET_ALL)

    def __repr__(self):
        return (f"AMMO: {self.AMMO}\n"
                f"DAMAGE: {self.DAMAGE}")


shotgun = Shotgun()


class PLayer:
    def __init__(self, name):
        self.__MAX_HP = 5
        self.NAME = name
        self.HEALTH = self.__MAX_HP
        self.ITEMS = list()

    def show_items(self):
        for indx, item in enumerate(dict.fromkeys(self.ITEMS)):
            print(f"{indx + 1}. {item.NAME} {self.ITEMS.count(item)}x - {item.DESCRIPTION}")

    def __repr__(self):
        str_items = ", ".join([item.NAME for item in self.ITEMS])

        return (f"NAME: {self.NAME}\n"
                f"HEALTH: {self.HEALTH}\n"
                f"ITEMS: {str_items}")


player = PLayer("PLAYER")
dealer = PLayer("DEALER")


class Item:
    def __init__(self, name: str, description: str, func):
        self.NAME = name
        self.DESCRIPTION = description
        self.FUNC = func

    def __call__(self, *args, **kwargs):
        return self.FUNC(*args, **kwargs)


PHONE_HINTS = [...]

cigarettes = Item("CIGARETTES", "+1 HP after smoking", lambda who: setattr(who, "HEALTH", who.HEALTH + 1))
beer = Item("BEER", "Extracts the next bullet", lambda: shotgun.AMMO.pop(0))
loupe = Item("LOUPE", "Shows the next bullet type", lambda: shotgun.AMMO[0])
knife = Item("KNIFE", "Deals 2x HP damage", lambda: setattr(shotgun, "DAMAGE", shotgun.MAX_DAMAGE))
#manacles = Item("MANACLES", "Grants a second move", lambda: True)
#phone = Item("PHONE", "Gives a hint", lambda: choice(PHONE_HINTS))

ITEMS = [cigarettes, beer, loupe, knife]


class Game:
    def __init__(self):
        self.ROUND = 1

    @staticmethod
    def give_item(who, times=1):
        for _ in range(times):
            who.ITEMS.append(choice(ITEMS))
        who.ITEMS = sorted(who.ITEMS, key=lambda item: ITEMS.index(item))

    def round_starting(self):
        soundtrack_player.soundtrack_player(soundtrack=soundtrack_player.MAIN_SOUNDTRACK)
        round_starting_comm1()
        self.give_item(player, 3)
        self.give_item(dealer, 3)
        shotgun.load_ammo()
        round_starting_comm2(self.ROUND)
        remaining_bullets()


game = Game()


class MenuPattern:
    def __init__(self, name: str, options: tuple):
        self.NAME = name.capitalize()
        self.OPTIONS = options

    def show_menu(self):
        print(Fore.LIGHTRED_EX + f">>> {self.NAME}:")
        for indx, option in enumerate(self.OPTIONS):
            print(Fore.BLUE + f"{indx+1}. {option.NAME}" + Style.RESET_ALL)

    def option_selecting(self):
        self.show_menu()
        while True:
            answer = input("<<< ")
            for indx, option in enumerate(self.OPTIONS):
                if answer.upper() in (option.NAME.upper(), str(indx+1)):
                    option()


class Option:
    def __init__(self, name: str, func):
        self.NAME = name.capitalize()
        self.FUNC = func

    def __call__(self, *args, **kwargs):
        return self.FUNC()


def hello_world():
    print("Hello World")

mm_options = (Option("Play", hello_world), Option("Settings", hello_world), Option("Quit", hello_world))
main_menu_option = MenuPattern("Main Menu", mm_options)
main_menu_option.option_selecting()
