# v6.0 alpha

from random import shuffle
import time
import sys
import os
from colorama import Fore, Style
import pyfiglet

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame.mixer.music

pygame.init()


def communicate(text, color):
    return getattr(Fore, color) + text + Style.RESET_ALL
