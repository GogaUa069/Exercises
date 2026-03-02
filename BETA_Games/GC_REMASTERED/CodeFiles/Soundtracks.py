from System import system, pygame

class Soundtrack:
    def __init__(self, name, repeats=1):
        self.NAME = name
        self.REPEATS = repeats

    @staticmethod
    def turn_off_soundtrack():
        pygame.mixer.music.stop()
        print(system.communicate("Music is turned off.", "LIGHTRED_EX"))

    def __call__(self):
        pygame.mixer.music.load(system.resource_path(f"../Soundtracks/{self.NAME}"))
        pygame.mixer.music.play(self.REPEATS)


intro_soundtrack = Soundtrack("IntroSoundtrack.wav")
credits_soundtrack = Soundtrack("CreditsSoundtrack.wav", -1)
jazz1 = Soundtrack("Jazz1.wav", -1)
jazz2 = Soundtrack("Jazz2.mp3", -1)
jazz3 = Soundtrack("Jazz3.wav", -1)
