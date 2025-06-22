import random
import time
import pygame


def step_stop(num):
    print()
    time.sleep(num)


def jazz():
    pygame.init()
    pygame.mixer.music.load(r"C:\Users\Егор\OneDrive\Рабочий стол\music_program\electro_jazz.wav")
    pygame.mixer.music.play(-1)


def intro():
    t0 = "..."
    text = [f"Dealer: Ohh, welcome! I thought...You won't come", t0,
            f"Dealer: Well...Lets plaaay?!", t0,
            f"Dealer: Hmm...You're so taciturn.", t0]
    for i in text:
        for j in i:
            time.sleep(0.21)
            if j == ".":
                print(j, end="", flush=True)
                time.sleep(0.5)
            else:
                print(j, end="", flush=True)
        print(sep='\n')
        time.sleep(1.5)
    time.sleep(3)


jazz()
pygame.mixer.music.set_volume(0.8)
time.sleep(0.5)


class Music:

    def __init__(self):
        pass

    def shotgun_load(self, a):
        pygame.init()
        pygame.mixer.music.load(r"C:\Users\Егор\OneDrive\Рабочий стол\music_program\shotgun_load.wav")
        pygame.mixer.music.play()
        pygame.mixer.music.set_pos(1.06)
        time.sleep(a)
        pygame.mixer.music.stop()

    def shotgun_shoot(self):
        pygame.init()
        pygame.mixer.music.load(r"C:\Users\Егор\OneDrive\Рабочий стол\music_program\shotgun_shoot.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)


my_music = Music()


class AllItems:

    items = ["cigarettes", "beer", "knife", "loupe", "manacles", "phone"]
    value_items = {"cigarettes": "Adds 1hp. If player has full health, nothing will happen.",
                   "beer": "Removes next bullet.",
                   "knife": "Gives double damage. (-2hp)",
                   "loupe": "Shows next bullet.",
                   "manacles": "Allows to shoot twice in a row.",
                   "phone": "Gives 1 hint"}
    bullet_combos = [(1, 1), (2, 1), (2, 2), (3, 2), (3, 3), (4, 3), (4, 4)]
    bullets = list()

    def __init__(self, dealer_items, player_items, dealer_health, player_health, max_health):
        self.dealer_items = dealer_items
        self.player_items = player_items
        self.dealer_health = dealer_health
        self.player_health = player_health
        self.max_health = max_health

        self.dealer_items = list()
        self.player_items = list()
        self.dealer_health = max_health
        self.max_health = max_health

    def get_dealer_items(self):
        for _ in range(4):
            random_item = random.choice(AllItems.items)
            self.dealer_items.append(random_item)
        self.dealer_items = sorted(self.dealer_items, key=lambda x: AllItems.items.index(x))

    def get_player_items(self):
        for _ in range(4):
            random_item = random.choice(AllItems.items)
            self.player_items.append(random_item)
        self.player_items = sorted(self.player_items, key=lambda x: AllItems.items.index(x))

    def get_bullets(self):
        random_combo = random.choice(AllItems.bullet_combos)
        pygame.mixer.music.stop()
        my_music.shotgun_load(sum(random_combo))
        jazz()

        for _ in range(random_combo[0]):
            AllItems.bullets.append("blank")
        for _ in range(random_combo[1]):
            AllItems.bullets.append("live")
        random.shuffle(self.bullets)

        print()
        print(f"Bullets info:\n\nBlank: {self.bullets.count("blank")}\nLive: {self.bullets.count("live")}")
        step_stop(0.5)


get_item = AllItems("", "", 5, 5, 5)


def getting_items():
    get_item.get_dealer_items()
    get_item.get_player_items()
    get_item.get_bullets()


getting_items()


class Moves(AllItems):

    dealer_win_counter = 0
    player_win_counter = 0

    def __init__(self, who_shoot_at, person_health, person):
        self.who_shoot_at = who_shoot_at
        self.person_health = person_health
        self.person = person
        AllItems.__init__(self, "", "", "", "", 5)

    def shot_info(self, person):
        bullet = self.bullets[0]
        print(f"Shot info:\nShot at: {person}\n"
              f"Type of bullet: {bullet}\n"
              f"{person} -{0 if bullet == "blank" else 1}xp\n"
              f"{person}'s health: {self.person_health-0 if bullet == "blank" else self.person_health-1}")
        step_stop(1)

    def backwash_of_shot(self):
        del self.bullets[0]
        if self.person == "Dealer":
            self.person_health -= 1
            print(self.person_health, "hi")
            if self.person_health == 0:
                Moves.player_win_counter += 1
                print(f"Player won this round!")
                step_stop(1)
        elif self.person_health == "Player":
            self.person_health -= 1
            if self.person_health == 0:
                Moves.dealer_win_counter += 1
                print(f"Dealer won this round!")
                step_stop(1)

    def player_shotgun_shot(self):
        self.who_shoot_at = 0
        while self.who_shoot_at not in (1, 2):
            print("Who to shoot at?\n1. Dealer\n2. You")
            step_stop(0.5)
            try:
                self.who_shoot_at = int(input("-----> "))
                if self.who_shoot_at not in (1, 2):
                    print("Please, enter 1 or 2")
                    step_stop(0.5)
            except ValueError:
                print("Please, use only NUMBERS. Enter 1 or 2")
                step_stop(0.5)

        self.person_health = ""
        if self.who_shoot_at == 1:
            self.person_health = self.dealer_health
            self.person = "Dealer"
            my_music.shotgun_shoot()
            time.sleep(1.5)
            self.shot_info(self.person)
        elif self.who_shoot_at == 2:
            self.person_health = self.player_health
            self.person = "Player"
            my_music.shotgun_shoot()
            time.sleep(1.5)
            self.shot_info(self.person)
            self.backwash_of_shot()


my_move = Moves("", "", "")
my_move.player_shotgun_shot()
