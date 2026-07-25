# Kingdom of Dragons 1 v5.0 Remastered

# Add achieves
# Add win streak

# ***************************************************************************************************

from random import shuffle
from time import sleep
import sys
import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import colorama
import pyfiglet
import pygame

colorama.init()
pygame.init()
pygame.mixer.init()


class SystemPrompt:
    def __init__(self):
        self.INPUT = self.communicate("<<< ", "LIGHTWHITE_EX")

    @staticmethod
    def communicate(text=None, color=None, is_error=False, is_bold=False, is_underlined=False):
        if text is None and color is None:
            return None
        elif is_error:
            text = f"ERROR: {text}"
            color = "LIGHTRED_EX"

        colored_text = getattr(colorama.Fore, color) + text + colorama.Style.RESET_ALL

        if is_bold:
            colored_text = colorama.Style.BRIGHT + colored_text
        if is_underlined:
            colored_text = "\033[4m" + colored_text + "\033[0m"

        return colored_text

    @staticmethod
    def resource_path(relative_path: str):
        base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def get_text_by_let(self, text: str):
        for char in text:
            sleep(0.21)
            print(self.communicate(char, "LIGHTWHITE_EX"), end="")

    def get_ascii_text(self, text: str, color="LIGHTBLUE_EX", font="standard"):
        f = pyfiglet.Figlet(font=font)
        ascii_text = f.renderText(text)
        for line in ascii_text.splitlines():
            print(self.communicate(line, color, is_bold=True))
            sleep(0.25)

    def quit_game(self):
        print(self.communicate("Goodbye! :)", "LIGHTCYAN_EX"))
        sleep(0.5)


system = SystemPrompt()


class Soundtrack:
    def __init__(self, name: str, repeats=1):
        self.NAME = name
        self.REPEATS = repeats

    @staticmethod
    def turn_off_soundtrack():
        pygame.mixer.music.stop()
        print(system.communicate(">>> Music if turned Off", "LIGHTRED_EX"))

    def __call__(self):
        pygame.mixer.music.load(system.resource_path(f"Soundtracks/{self.NAME}"))
        pygame.mixer.music.play(self.REPEATS)


FOREST_SOUNDTRACK = Soundtrack("ForestSoundtrack.wav", -1)
CREDITS_SOUNDTRACK = Soundtrack("OldCreditsSoundtrack.wav", -1)
THE_END_SOUNDTRACK_DEATH = Soundtrack("EndMusic.wav", -1)
THE_END_SOUNDTRACK_LIVE = Soundtrack("LiveMusic.wav", -1)

EPIC_INTRO_SOUND = pygame.mixer.Sound(system.resource_path("Audio/EpicIntroSound.wav"))  # MAXTIME: 1000
CAVE_CHOICE_SCREAMER = pygame.mixer.Sound(system.resource_path("Audio/CaveChoiceScreamer.wav"))
STEPS = pygame.mixer.Sound(system.resource_path("Audio/Steps.wav"))  # MAXTIME: 2670
HEARTBEAT = pygame.mixer.Sound(system.resource_path("Audio/HeartBeat.wav"))  # MAXTIME: 3500
INTRIGUE_SOUND = pygame.mixer.Sound(system.resource_path("Audio/IntrigueSound.wav"))  # MAXTIME: 4000
DEATH_SOUND = pygame.mixer.Sound(system.resource_path("Audio/DeathSound.wav"))
END_GAME_SOUND = pygame.mixer.Sound(system.resource_path("Audio/EndGameSound.wav"))


class GameIntro:
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
