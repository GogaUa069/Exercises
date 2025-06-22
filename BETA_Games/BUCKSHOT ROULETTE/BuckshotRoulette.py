import time
import random
from pygame import mixer, init
import pygame


def step_stop():
    print()
    time.sleep(0.5)


def music():
    init()
    mixer.music.load(r"C:\Users\Егор\OneDrive\Рабочий стол\music_program\electro_jazz.wav")
    mixer.music.play(-1)


music()


def shotgun_load(a):
    init()
    mixer.music.load(r"C:\Users\Егор\OneDrive\Рабочий стол\music_program\shotgun_load.wav")
    mixer.music.play()
    mixer.music.set_pos(1.06)
    time.sleep(a)
    mixer.music.stop()


def shotgun_shoot():
    init()
    mixer.music.load(r"C:\Users\Егор\OneDrive\Рабочий стол\music_program\shotgun_shoot.wav")
    mixer.music.play()
    while mixer.music.get_busy():
        pygame.time.Clock().tick(10)


class Game:

    items = ["cigarettes", "beer", "loupe", "knife", "manacles", 'phone']
    value_dict = {"cigarettes": "After smoking +1xp; If max xp, nothing happens", "beer": "Removes next bullet",
                  "loupe": "shows type of next bullet", "knife": "gets double damage -2xp", "manacles": "You can shoot twice in a row",
                  "phone": "gets 1 hint"}
    dealer_items = list()
    player_items = list()
    bullets = list()

    def __init__(self, dealer_hearts, player_hearts):
        self.dealer_hearts = dealer_hearts
        self.player_hearts = player_hearts

        self.dealer_hearts = 5
        self.player_hearts = 5

    print()
    print("Please, wait. Items are dealt...")
    print()
    time.sleep(3)
    mixer.music.set_volume(0.1)

    def get_dealer_items(self):
        for _ in range(4):
            Game.dealer_items.append(random.choice(Game.items))
        sorted(Game.dealer_items, key=lambda x: Game.items.index(x))

    def get_player_items(self):
        for _ in range(4):
            Game.player_items.append(random.choice(Game.items))
        sorted(Game.player_items, key=lambda x: Game.items.index(x))
        print(Game.player_items)

    def get_bullets(self):
        Game.bullets.append("blank")
        Game.bullets.append("live")
        num = random.randint(2, 8)
        if num == 2:
            pass
        else:
            for _ in range(num-2):
                Game.bullets.append(random.choice(["live", "blank"]))
        random.shuffle(Game.bullets)

        print(Game.bullets)
        shotgun_load(num)
        print(f"Blank bullets: {Game.bullets.count("blank")}")
        print(f"Live bullets: {Game.bullets.count("live")}")
        step_stop()
        music()
        mixer.music.set_volume(0.1)

    def player_move(self):

        def shotgun_func():
            print("Dealer: 1\nYou: 2")
            while True:
                try:
                    answer2 = int(input("-----> "))
                    mixer.music.stop()
                    shotgun_shoot()
                    if answer2 == 1:
                        if Game.bullets[0] == "live":
                            self.dealer_hearts -= 1
                            print(f"Info:\nBullet: {Game.bullets[0]}\nDealer -1xp\nDealer lives: {self.dealer_hearts}")
                            del Game.bullets[0]
                            break
                        elif Game.bullets[0] == "blank":
                            print(f"Info:\nBullet: {Game.bullets[0]}\nDealer -0xp\nDealer lives: {self.dealer_hearts}")
                            del Game.bullets[0]
                            break
                    elif answer2 == 2:
                        if Game.bullets[0] == "live":
                            self.player_hearts -= 1
                            print(f"Info:\nBullet: {Game.bullets[0]}\nPlayer -1xp\nPlayer lives: {self.player_hearts}")
                            del Game.bullets[0]
                            break
                        elif Game.bullets == "blank":
                            print(f"Info:\nBullet: {Game.bullets[0]}\nPlayer -0xp\nPlayer lives: {self.player_hearts}")
                            del Game.bullets[0]
                            break
                    elif answer2 not in [1, 2]:
                        print("Please, enter 1 or 2")
                except ValueError:
                    print("Please, enter NUMBER")

        def items_func():
            print("Your items:")
            if len(self.player_items) == 0:
                print("Ohh..what a pity! You haven't items.")
            else:
                item_list = sorted(set(self.player_items), key=lambda x: self.items.index(x))
                for i in range(len(item_list)):
                    print(f"{i+1}. {item_list[i]}: x{self.player_items.count(item_list[i])}; {Game.value_dict[item_list[i]]}")
                    step_stop()
                print(f"Enter numbers in range 1-{len(item_list)}, or enter 'L' to leave")
                step_stop()
                answer3 = ""
                while answer3.lower() != "l":
                    answer3 = input("-----> ")
                    if (answer3.isdigit() and int(answer3) not in range(1, len(item_list)+1)) and answer3.lower() != "l":
                        continue
                    elif str(answer3).lower() == "l":
                        break
                    else:
                        if item_list[int(answer3)-1] == "cigarettes":
                            if self.player_hearts == 5:
                                print("You have max health, nothing happened")
                                self.player_items.remove("cigarettes")
                                continue
                            else:
                                self.player_hearts += 1
                                print(f"Info:\nPlayer health +1xp\nPlayer health: {self.player_hearts}xp")
                                self.player_items.remove("cigarettes")
                                continue
                        elif item_list[int(answer3)-1] == "beer":
                            last_bullet = Game.bullets[0]
                            del Game.bullets[0]
                            print(f"Info:\nWas deleted next bullet\nBullet: {last_bullet}")
                            self.player_items.remove("beer")
                            continue

        answer1 = 0
        while answer1 != 1:
            print("Shotgun: 1\nItems: 2")
            try:
                answer = int(input("-----> "))
                if answer == 1:
                    shotgun_func()
                    break
                elif answer == 2:
                    items_func()
            except ValueError:
                print("Please, enter NUMBER")


my_game = Game("", "")
my_game.get_dealer_items()
my_game.get_player_items()
my_game.get_bullets()
my_game.player_move()









