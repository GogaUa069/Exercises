# v5.0.0 REMASTERED

import random
import time

# import sys
# import os
#
# os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import colorama
import pyfiglet
import pygame

colorama.init()
pygame.init()


class System:
    def __init__(self):
        self.INPUT = self.communicate("<<< ", "LIGHTWHITE_EX")

    @staticmethod
    def communicate(text, color):
        return getattr(colorama.Fore, color) + text + colorama.Style.RESET_ALL

    def quit_game(self):
        print(self.communicate("Goodbye! :)", "LIGHTCYAN_EX"))
        time.sleep(0.5)


system = System()


class Soundtrack:
    def __init__(self, name, repeats):
        self.PATH = f"SOUNDTRACKS/{name.upper()}_SOUNDTRACK.wav"
        self.REPEATS = repeats

    def __call__(self):
        pygame.mixer.music.load(self.PATH)
        pygame.mixer.music.play(self.REPEATS)


alive_soundtrack = Soundtrack("alive", 1)
credits_soundtrack = Soundtrack("credit", -1)
end_soundtrack = Soundtrack("end", -1)
forest_soundtrack = Soundtrack("forest", -1)


class Sound:
    def __init__(self, name, maxtime=None):
        self.PATH = f"SOUNDS/{name.upper()}_SOUND.wav"
        self.SOUND = pygame.mixer.Sound(self.PATH)
        self.MAXTIME = maxtime

    def __call__(self):
        match self.MAXTIME:
            case None:
                self.SOUND.play()
            case _:
                self.SOUND.play(maxtime=self.MAXTIME)


cave_screamer_sound = Sound("cave_screamer")
death_sound = Sound("death")
end_game_sound = Sound("end_game")
heart_beat_sound = Sound("heart_beat", 3500)
intrigue_sound = Sound("intrigue", 4000)
intro_sound = Sound("intro", 1000)
laugh_sound = Sound("laugh")
steps_sound = Sound("steps", 2670)


class Intro:
    ...
