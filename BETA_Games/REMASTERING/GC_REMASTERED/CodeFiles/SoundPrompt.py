from System import system, pygame


class SoundPrompt:
    YOU_WIN_SOUND = pygame.mixer.Sound(system.resource_path("../Sounds/YouWinSound.wav"))  # MAXTIME = 2350
    YOU_LOST_SOUND = pygame.mixer.Sound(system.resource_path("../Sounds/YouLostSound.wav"))  # MAXTIME = 2500
    ABLE_TO_PLAY = True

    def __call__(self):
        self.ABLE_TO_PLAY = not self.ABLE_TO_PLAY
        match self.ABLE_TO_PLAY:
            case True:
                self.YOU_WIN_SOUND.play(maxtime=2350)
                print(system.communicate("Sound is turned ON", "LIGHTGREEN_EX"))
            case False:
                self.YOU_LOST_SOUND.play(maxtime=2500)
                print(system.communicate("Sound is turned OFF", "LIGHTRED_EX"))


sound_prompt = SoundPrompt()
