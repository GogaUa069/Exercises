from colorama import Fore, Style
from time import sleep
from random import choice, randint, shuffle
from pygame import mixer, init, time

init()


class Music:

    @staticmethod
    def main_music():
        mixer.music.load(r"C:\Users\Егор\OneDrive\Рабочий стол\music_program\electro_jazz.wav")
        mixer.music.play(-1)

    @staticmethod
    def shotgun_load(secs):
        mixer.music.load(r"C:\Users\Егор\OneDrive\Рабочий стол\music_program\shotgun_load.wav")
        mixer.music.play()
        mixer.music.set_pos(1.06)
        sleep(secs)
        mixer.music.stop()

    @staticmethod
    def shotgun_shoot():
        mixer.music.load(r"C:\Users\Егор\OneDrive\Рабочий стол\music_program\shotgun_shoot.wav")
        mixer.music.play()
        while mixer.music.get_busy():
            time.Clock().tick(10)


music = Music()
music.main_music()


class GameData:
    def __init__(self):
        self.items = ["cigarettes", "beer", "loupe", "knife", "manacles", "phone"]
        self.item_values = {"cigarettes": "+1HP; If MAX HP, nothing will happen.",
                            "beer": "Removes the next bullet.",
                            "loupe": "Shows the type of the next bullet.",
                            "knife": "Gives double damage.",
                            "manacles": "You can shoot twice in a row.",
                            "phone": "Gives one hint."}
        self.bullets = list()
        self.bullet_values = ["blank", "live"]
        self.MAX_HEALTH = 5

    def get_items(self, firstly, pl):
        print(Fore.RED + "\nPlease wait. Items are dealing..." + Style.RESET_ALL)
        sleep(3)
        if firstly:
            for _ in range(4):
                pl.ITEMS.append(choice(self.items))
        else:
            pl.ITEMS.append(choice(self.items))
        sorted(pl.ITEMS, key=lambda x: self.items.index(x))

    def get_bullets(self):
        print(Fore.RED + "\nPlease wait for the ammo to load..." + Style.RESET_ALL)
        sleep(3)
        self.bullets.extend(self.bullet_values)
        bullet_counter = randint(3, 8)

        for _ in range(bullet_counter-2):
            self.bullets.append(choice(self.bullet_values))
        shuffle(self.bullets)

        music.shotgun_load(bullet_counter)
        print(f"Blank bullets: {self.bullets.count("blank")}")
        print(f"Live bullets: {self.bullets.count("live")}\n")
        music.main_music()
        mixer.music.set_volume(0.1)


class Player(GameData):
    def __init__(self):
        self.NAME = "Player"
        self.ITEMS = list()
        self.ANSWER = str()
        GameData.__init__(self)
        self.HEALTH = self.MAX_HEALTH


class PlayerMove(Player):
    def __init__(self):
        self.next_bullet = self.bullets[0]
        self.damage = 0 if self.next_bullet == "blank" else 1
        Player.__init__(self)
    print("Your move\n")

    def shot_info(self, shooter, shot_at):
        print("Shot info:")
        print(f"Shooter: {shooter.NAME}\n"
              f"Shot at: {shot_at.NAME}\n"
              f"Type of bullet: {self.next_bullet}\n"
              f"{shot_at.NAME} -{self.damage}HP\n"
              f"{shot_at.NAME}'s health: {shot_at.HEALTH - self.damage}HP\n")
        if shot_at.HEALTH == 0:
            if shot_at.NAME == "Player":
                print("Dealer wins!")
            else:
                print("Player wins!")

    def shot(self):
        print("Who do you want ot shoot?\n")
        print("DEALER - 1\n"
              "YOU - 2\n")

        def person_shot(person):
            music.shotgun_shoot()
            del self.bullets[0]
            person.HEALTH -= self.damage

        while True:
            self.ANSWER = input("-----> ")
            match self.ANSWER.lower():
                case "dealer" | "1":
                    self.shot_info(player, dealer)
                    person_shot(dealer)
                case "you" | "2":
                    self.shot_info(player, dealer)
                    person_shot(player)
                case _:
                    print("Please, enter DEALER or YOU")
                    continue
            self.ANSWER = str()

    def show_items(self):
        if len(self.ITEMS) == 0:
            print("You have not items...")
        else:
            print("Your items:")
            self.ITEMS = sorted(set(self.ITEMS), key=lambda x: self.items.index(x))
            for indx in range(len(self.ITEMS)):
                item = self.ITEMS[indx]
                print(f"{indx+1}. {item} x{self.ITEMS.count(item)}; {self.item_values[item]}")
            print("L - leave")
            print(f"\nEnter number in range 1-{len(self.ITEMS)} or L to leave")
            while self.ANSWER.lower() != "l":
                try:
                    self.ANSWER = input("-----> ")
                except self.ANSWER == "l":
                    break
                else:
                    item = self.items[int(self.ANSWER)+1]
                    pass

    def shot_or_items(self):
        print("SHOT - 1\n"
              "ITEMS - 2\n")
        while True:
            self.ANSWER = input("-----> ")
            match self.ANSWER.lower():
                case "shot" | "1":
                    self.shot()
                    break
                case "items" | "2":
                    self.show_items()
                case _:
                    print("Please, enter SHOT or ITEMS")
                    continue
        self.ANSWER = str()


# TESTS **************************************


player = Player()
dealer = Dealer()
