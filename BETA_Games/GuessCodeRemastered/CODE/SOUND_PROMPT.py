from SYSTEM_PROMPT import system, pygame


class SoundPrompt:
    VICTORY_SOUND = pygame.mixer.Sound("../AUDIO/SOUNDS/VICTORY_SOUND.wav")  # MAXTIME: 2350
    DEFEAT_SOUND = pygame.mixer.Sound("../AUDIO/SOUNDS/DEFEAT_SOUND.wav")    # MAXTIME: 2500
    ABLE_TO_PLAY = True

    def __call__(self, *args, **kwargs):
        self.ABLE_TO_PLAY = not self.ABLE_TO_PLAY
        match self.ABLE_TO_PLAY:
            case True:
                self.VICTORY_SOUND.play(maxtime=2350)
                print(system.communicate("Sounds are turned ON", "LIGHTGREEN_EX"))
            case False:
                self.DEFEAT_SOUND.play(maxtime=2500)
                print(system.communicate("Sounds are turned OFF", "LIGHTRED_EX"))


sound_prompt = SoundPrompt()
