from System import system, sleep, pygame
from Soundtracks import credits_soundtrack


class Credits:
    def __init__(self, *args):
        self.CREDITS = list(args)

    def get_credits(self):
        for indx, credit in enumerate(self.CREDITS, 1):
            system.get_text_by_let(f"{indx}. {credit}")
            print()
        sleep(1)
        print()

    @staticmethod
    def close_credits_menu():
        print(system.communicate("All audio was taken from freesound.org", "LIGHTWHITE_EX"))
        input(system.communicate(">>> Press ENTER to leave", "LIGHTRED_EX"))
        pygame.mixer.music.stop()

    def __call__(self):
        credits_soundtrack()
        system.set_ascii_text("CREDITS:")
        self.get_credits()
        self.close_credits_menu()


credits_menu = Credits("Egor Pavlenko - CEO")
