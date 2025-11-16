# v 4.3.0

from random import shuffle
import time
from colorama import Fore, Style, init
import sys
import os
import pyfiglet

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import pygame

pygame.init()
init()  # Colorama

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class AudioPlayer:
    """All sounds and soundtracks are here"""

    FOREST_SOUNDTRACK = "ForestSoundtrack.wav"
    THE_END_SOUNDTRACK_DEATH = "EndMusic.wav"
    THE_END_SOUNDTRACK_LIVE = "LiveMusic.wav"
    CREDITS_SOUNDTRACK = "OldCreditsSoundtrack.wav"

    EPIC_INTRO_SOUND = pygame.mixer.Sound(resource_path("Audio/EpicIntroSound.wav"))  # MAXTIME: 1000
    CAVE_CHOICE_SCREAMER = pygame.mixer.Sound(resource_path("Audio/CaveChoiceScreamer.wav"))
    STEPS = pygame.mixer.Sound(resource_path("Audio/Steps.wav"))  # MAXTIME: 2670
    HEARTBEAT = pygame.mixer.Sound(resource_path("Audio/HeartBeat.wav"))  # MAXTIME: 3500
    INTRIGUE_SOUND = pygame.mixer.Sound(resource_path("Audio/IntrigueSound.wav"))  # MAXTIME: 4000
    DEATH_SOUND = pygame.mixer.Sound(resource_path("Audio/DeathSound.wav"))
    END_GAME_SOUND = pygame.mixer.Sound(resource_path("Audio/EndGameSound.wav"))

    @staticmethod
    def play_soundtrack(soundtrack, is_infinity=False):
        """Pattern for playing soundtracks"""
        pygame.mixer.music.load(resource_path("Audio/" + soundtrack))
        pygame.mixer.music.play(-1) if is_infinity else pygame.mixer.music.play()


class GameIntro:
    def __init__(self, *args):
        self.banners = list(args)

    def get_banners(self):
        for banner in self.banners:
            banner = pyfiglet.figlet_format(banner)
            print(Fore.LIGHTRED_EX + banner + Style.RESET_ALL)
            AudioPlayer.EPIC_INTRO_SOUND.play()
            time.sleep(1)

    def __call__(self, *args, **kwargs):
        self.get_banners()


game_intro = GameIntro("Kingdom", "Of", "Dragons")
game_intro()


class Credits:
    HEADER = "CREDITS:"
    freesound_comm = Fore.LIGHTWHITE_EX + "\n\033[4mAll soundtracks were taken from freesound.org\033[0m" + Style.RESET_ALL

    def __init__(self, *args):
        self.credit_list = list(args)

    def __call__(self, *args, **kwargs):
        AudioPlayer.play_soundtrack(AudioPlayer.CREDITS_SOUNDTRACK, True)

        def name_by_let(name: str, indx=0):
            if indx > 0:
                print(Fore.LIGHTWHITE_EX + f"{indx}. " + Style.RESET_ALL, end="")
            for char in name:
                time.sleep(0.21)
                print(Fore.LIGHTWHITE_EX + f"{char}" + Style.RESET_ALL, end="")
            print()

        def get_banner_by_let(banner: str):
            ascii_banner = pyfiglet.figlet_format(banner)
            for line in ascii_banner.splitlines():
                print(Fore.LIGHTBLUE_EX + line + Style.RESET_ALL)
                time.sleep(0.25)

        get_banner_by_let(self.HEADER)
        for indx, credit in enumerate(self.credit_list):
            name_by_let(credit, indx+1)
            time.sleep(1)

        print(self.freesound_comm)
        input(Fore.LIGHTRED_EX + ">>> Press ENTER to leave " + Style.RESET_ALL)
        print()
        pygame.mixer.music.stop()


credits = Credits("GogaUa (Yegor Pavlenko) - CEO")


class Ending:
    """
    Class for ending types (Bad/Good)
    """
    def __init__(self, word, soundtrack):
        self.word = word
        self.soundtrack = soundtrack


good_ending = Ending(Fore.LIGHTGREEN_EX + "...shares his treasures with You!", AudioPlayer.THE_END_SOUNDTRACK_LIVE)
bad_ending = Ending(Fore.LIGHTRED_EX + "...instantly eats You up!", AudioPlayer.THE_END_SOUNDTRACK_DEATH)


class Game(AudioPlayer):
    """
    Game class with main game mechanics
    """
    ENDINGS = [good_ending, bad_ending]

    INTRO = (Fore.BLUE + "You are in a land inhabited by dragons.", "You see two caves in front of You.",
             "In one of them, a friendly dragon is waiting to give You some treasure.",
             "In the second, a wicked and hungry dragon waits, ready to eat you!",
             "But You don't know which dragon is in which cave." + Style.RESET_ALL)

    def __init__(self):
        AudioPlayer.__init__(self)
        self.true_ending = None

    def get_intro(self):
        """
        Prehistory of game
        :return: text
        """
        pygame.mixer.music.stop()

        print(Fore.LIGHTRED_EX + "\nClick Enter to continue")
        input()
        self.play_soundtrack(self.FOREST_SOUNDTRACK, True)
        for text in self.INTRO:
            print(text, end="")
            input()
        pygame.mixer.music.stop()

    def cave_choice(self):
        """
        Selecting cave
        :return: Nothing
        """
        shuffle(self.ENDINGS)
        self.CAVE_CHOICE_SCREAMER.play()

        answer = ""
        while answer.upper() not in ("LEFT", "RIGHT", "1", "2"):
            print(Fore.LIGHTRED_EX + "\nWhich cave will You choose?" + Style.RESET_ALL)
            answer = input("<<< ")
            match answer.upper():
                case "LEFT" | "1":
                    self.true_ending = self.ENDINGS[0]
                case "RIGHT" | "2":
                    self.true_ending = self.ENDINGS[1]
                case _:
                    print(Fore.LIGHTRED_EX + "Select one of the options shown above!" + Style.RESET_ALL)

    def ending_checking(self):
        """
        If ending is bad, plays sound DEATH_SOUND
        :return: Sound
        """
        self.END_GAME_SOUND.play()
        print(self.true_ending.word)

        if self.true_ending == bad_ending:
            time.sleep(1.5)
            self.DEATH_SOUND.play()

        time.sleep(0.5)

    def choice_intrigue(self):
        """
        Intrigue after player's choice
        :return: Nothing
        """
        print(Fore.LIGHTWHITE_EX + "\nYou're moving toward the cave...")
        self.STEPS.play(maxtime=2670)
        time.sleep(2.67)
        print("Its darkness makes You tremble with fear...")
        self.HEARTBEAT.play(maxtime=3500)
        time.sleep(3.5)
        print("The big dragon jumps in front of you. He opens his big jaws and...")
        self.INTRIGUE_SOUND.play(maxtime=4000)
        time.sleep(4)
        self.ending_checking()
        time.sleep(3)
        print("\nThe End!\n" + Style.RESET_ALL)
        self.play_soundtrack(self.true_ending.soundtrack, True)

    def game(self):
        """
        Game func
        :return: Game
        """
        self.__init__()
        self.get_intro()
        self.cave_choice()
        self.choice_intrigue()


game_class = Game()

def main_menu():
    """
    Main menu func
    :return:
    """
    def goodbye_func():
        """
        Laughs
        :return: Goodbye
        """
        laugh_time = 3000
        fadeout_time = 1500

        pygame.mixer.music.stop()

        laugh_sound.play()
        print(Fore.LIGHTCYAN_EX + "Goodbye! :)" + Style.RESET_ALL)
        time.sleep(laugh_time / 1000)
        laugh_sound.fadeout(1500)
        time.sleep(fadeout_time / 1000)

    laugh_sound = pygame.mixer.Sound(resource_path("Audio/Laugh.wav"))  # MAXTIME: 3000
    answer = ""
    print(Fore.CYAN + "Welcome to the Kingdom of Dragons!\n" + Style.RESET_ALL)

    while answer.upper() not in ("ESCAPE", "2"):
        print(Fore.LIGHTRED_EX + ">>> Main Menu")
        print(Fore.BLUE + "1. Try Your luck\n"
                          "2. Make a miserable escape\n"
                          "3. Credits" + Style.RESET_ALL)
        answer = input("<<< ")
        match answer.upper():
            case "TRY LUCK" | "TRY" | "1":
                game_class.game()
            case "ESCAPE" | "2":
                goodbye_func()
            case "CREDITS" | "3":
                credits()
            case _:
                print(Fore.LIGHTRED_EX + "Select one of the options shown above!\n" + Style.RESET_ALL)

main_menu()
