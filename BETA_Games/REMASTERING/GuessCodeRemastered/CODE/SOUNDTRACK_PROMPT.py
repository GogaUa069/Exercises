from SYSTEM_PROMPT import system, pygame


class Soundtrack:
    def __init__(self, name, repeats=1):
        self.NAME = name
        self.REPEATS = repeats

    @staticmethod
    def turn_off_soundtrack():
        pygame.mixer.music.stop()
        print(system.communicate("Soundtracks are turned OFF", "LIGHTRED_EX"))

    def __call__(self):
        path = system.resource_path(f"../AUDIO/SOUNDTRACKS/{self.NAME}")
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()


intro_soundtrack = Soundtrack("INTRO_MENU_SOUNDTRACK.wav")
credits_soundtrack = Soundtrack("CREDITS_MENU_SOUNDTRACK.wav")
soundtrack1 = Soundtrack("SOUNDTRACK_1.wav")
soundtrack2 = Soundtrack("SOUNDTRACK_2.wav")
soundtrack3 = Soundtrack("SOUNDTRACK_3.wav")
