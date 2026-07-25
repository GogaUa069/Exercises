from System import system, choice, sleep, tqdm
from Soundtracks import intro_soundtrack


class GameIntro:
    GitHub_URL = "https://github.com/GogaUa069"
    Instagram_URL = "https://www.instagram.com/gogaua096/"

    def get_accounts(self):
        print(system.communicate(f"Follow me on Instagram -> {self.Instagram_URL}", "CYAN"))
        print(system.communicate(f"Check my GitHub -> {self.GitHub_URL}\n", "CYAN"))

    @staticmethod
    def loading():
        with tqdm(total=100) as pbar:
            for _ in range(100):
                color = choice(system.COLORS)
                pbar.set_description_str(system.communicate("Loading", color))
                pbar.update(1)
                sleep(0.04)

    @staticmethod
    def show_game_banner(banner):
        sleep(0.5)
        print(system.communicate("Welcome to:", "CYAN"))
        sleep(1.5)
        system.set_ascii_text(banner)
        print(system.communicate("Made by GogaUa\n", "WHITE"))
        sleep(1)

    def __call__(self):
        intro_soundtrack()
        self.get_accounts()
        self.show_game_banner("Guess Code v.7.1.0")
        self.loading()


game_intro = GameIntro()