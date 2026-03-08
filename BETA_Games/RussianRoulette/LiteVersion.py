import os
from random import shuffle, randint
from time import sleep
from colorama import Fore, Style
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame

pygame.init()


def play_audio(name="texting.wav", delay=1000):
    pygame.mixer.music.load(rf"audio/{name}")
    pygame.mixer.music.play()
    pygame.time.delay(delay)
    pygame.mixer.music.stop()


def communicate(text, color="LIGHTRED_EX", is_man=True):
    if is_man:
        text = f"[noname]: {text}"
    return getattr(Fore, color) + text + Style.RESET_ALL


class Game:
    def __init__(self):
        self.live = randint(1, 3)
        self.blank = 6-self.live
        self.cylinder = [0]*self.blank + [1]*self.live
        shuffle(self.cylinder)
        self.player = self.dealer = True

    @staticmethod
    def clear_cmd():
        os.system("cls")

    def is_over(self):
        return True if self.player and self.dealer and not all(chamber == 1 for chamber in self.cylinder) else False

    def player_dead(self):
        self.clear_cmd()
        sleep(3)
        print(communicate("He's dead..."))
        play_audio()
        sleep(3)
        print(communicate("Come on, we need to dispose of him."))
        play_audio()
        sleep(3)
        self.clear_cmd()

    def player_won(self):
        print(communicate("Oops. Dealer is out..."))
        play_audio()
        sleep(3)
        self.clear_cmd()
        sleep(3)
        print(communicate("An eye for an eye..."))
        play_audio()
        sleep(3)

    def player_shot(self):
        print(f"\nChance to die: {self.cylinder.count(1)}/{len(self.cylinder)}")
        input(communicate("Press ENTER to shot", "CYAN", False))
        bullet = self.cylinder[0]
        del self.cylinder[0]
        if bullet:
            self.player = False
            self.player_dead()
        else:
            print(communicate("You alive."))
            play_audio()
            shuffle(self.cylinder)

    def player_move(self):
        self.player_shot()
        while self.player:
            print(f"\nChance to die: {self.cylinder.count(1)}/{len(self.cylinder)}")
            print(communicate("Shot or stay?", "CYAN", False))
            answer = input("<<< ")
            match answer:
                case "1" | "shot":
                    self.player_shot()
                case "2" | "stay":
                    break
                case _:
                    print(communicate("Select one of the options shown above!"))

    def dealer_move(self):
        print(f"\nChance to win: {self.cylinder.count(1)}/{len(self.cylinder)}")
        print(communicate("Dealers move...", "CYAN", False))
        sleep(randint(1, 3))
        bullet = self.cylinder[0]
        del self.cylinder[0]
        if bullet:
            self.dealer = False
            self.player_won()
        else:
            print(communicate("Dealer alive!"))
            play_audio()
            shuffle(self.cylinder)

    def __call__(self):
        while True:
            self.player_move()
            if not self.is_over():
                break
            self.dealer_move()
            if not self.is_over():
                break


game = Game()
game()
