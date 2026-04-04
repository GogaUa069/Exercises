import os
from abc import ABC, abstractmethod
from time import sleep
from random import randint, choice, choices
from colorama import Fore, Style


class System:
    MAX_BULLETS = 6
    MAX_ENERGY = 6
    MAX_LIVES = 3

    def __init__(self):
        self.promo_flag = False

    @staticmethod
    def communicate(text, color):
        return getattr(Fore, color) + text + Style.RESET_ALL


system = System()


class Option(ABC):
    def __init__(self, name, energy):
        self.NAME = name
        self.ENERGY = energy

    @abstractmethod
    def validate_profile(self, player):
        pass


class Shot(Option):
    def validate_profile(self, player, is_human=True):
        if player.bullets != 0:
            return True
        else:
            if is_human:
                print(system.communicate("ERROR: No bullets remaining.\n", "LIGHTRED_EX"))
            return False

    def __call__(self, player):
        player.option = shot
        player.energy += player.option.ENERGY if player.energy + player.option.ENERGY <= system.MAX_ENERGY else 0
        player.bullets -= 1


class Load(Option):
    def validate_profile(self, player, is_human=True):
        if player.bullets != system.MAX_BULLETS:
            if is_human:
                print(system.communicate(f">>> +1 bullet. You now have {player.bullets + 1} bullet(s).", "CYAN"))
            return True
        else:
            if is_human:
                print(system.communicate("ERROR: Ammo is already full.\n", "LIGHTRED_EX"))
            return False

    def __call__(self, player):
        player.option = load
        player.energy += player.option.ENERGY if player.energy + player.option.ENERGY <= system.MAX_ENERGY else 0
        player.bullets += 1


class Block(Option):
    def validate_profile(self, player, is_human=True):
        if player.energy - abs(self.ENERGY) >= 0:
            if is_human:
                print(system.communicate(">>> Shield activated.", "CYAN"))
            return True
        else:
            if is_human:
                print(system.communicate("ERROR: You do not have enough energy! Required: 2.\n", "LIGHTRED_EX"))
            return False

    def __call__(self, player):
        player.option = block
        player.energy += player.option.ENERGY
        player.shield = True


class Deflect(Option):
    def validate_profile(self, player, is_human=True):
        if player.energy - abs(self.ENERGY) >= 0:
            if is_human:
                print(system.communicate(">>> Shield activated.", "CYAN"))
            return True
        else:
            if is_human:
                print(system.communicate("ERROR: You do not have enough energy! Required: 3.\n", "LIGHTRED_EX"))
            return False

    def __call__(self, player):
        player.option = deflect
        player.energy += player.option.ENERGY
        player.shield = True


shot = Shot(name="SHOT", energy=1)
load = Load(name="LOAD", energy=1)
block = Block(name="BLOCK", energy=-2)
deflect = Deflect(name="DEFLECT", energy=-3)


class Player(ABC):
    def __init__(self, name):
        self.name = name
        self.lives = system.MAX_LIVES
        self.energy = system.MAX_ENERGY
        self.bullets = 0
        self.shield = False
        self.option = None

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def reset(self):
        pass


class Human(Player):
    def validate_option(self, option):
        match option.lower():
            case "1" | "shot":
                    self.option = shot if shot.validate_profile(self) else None
            case "2" | "load":
                    self.option = load if load.validate_profile(self) else None
            case "3" | "block":
                    self.option = block if block.validate_profile(self) else None
            case "4" | "deflect":
                    self.option = deflect if deflect.validate_profile(self) else None
            case "096":
                print(system.communicate("Promotion code is activated.\n", "LIGHTYELLOW_EX"))
                system.promo_flag = True
            case "l":
                quit()
            case _:
                print(system.communicate("ERROR: Select one of the options shown above!\n", "LIGHTRED_EX"))

    def random_move(self):
        while self.option is None:
            option = choice((shot, load, block, deflect))
            self.option = option if option.validate_profile(self, False) else None
        print(system.communicate(f">>> Too many wrong answers. Your answer is {self.option.NAME}.", "LIGHTRED_EX"))
        sleep(1.5)

    def move(self):
        wrong_counter = 0
        print(system.communicate(">>> Your move...\n", "LIGHTRED_EX"))
        print(self)
        while self.option is None:
            wrong_counter += 1
            if wrong_counter < 4:
                print(system.communicate(f"Select one of the options shown below: ({wrong_counter}/3)", "CYAN"))
                print(system.communicate("1. Shot\n2. Load\n3. Block\n4. Deflect", "LIGHTWHITE_EX"))
                self.validate_option(input(system.communicate("<<< ", "LIGHTWHITE_EX")))
            else:
                self.random_move()
        self.option(self)

    def reset(self):
        self.lives = system.MAX_LIVES
        self.energy = system.MAX_ENERGY
        self.bullets = 0
        self.shield = False
        self.option = None

    def __str__(self):
        info = system.communicate(f"*** INFO ***\n"
                                  f"- Lives: {self.lives}/{system.MAX_LIVES}\n"
                                  f"- Energy: {self.energy}\n"
                                  f"- Bullets: {self.bullets}\n"
                                  f"* Dealer lives: {bot.lives}/{system.MAX_LIVES}\n",
                                  "LIGHTWHITE_EX")
        return info if not system.promo_flag else info + f"* Dealer energy: {bot.energy}\n* Dealer bullets: {bot.bullets}\n"


class Bot(Player):
    def __init__(self, name):
        super().__init__(name)
        self.move_counter = 0
        self.last_moves = list()

    def move(self):
        print(system.communicate("\n>>> Dealer's move...\n", "LIGHTRED_EX"))
        sleep(randint(1, 3))

        self.move_counter += 1
        # weights = [25, 25, 25, 25]  # for debugging

        while self.option is None:
            options = (shot, load, block, deflect)
            weights = [[25, 25, 25, 25]]

            if self.move_counter == 1:
                weights.append([0, 100, 0, 0])
                weights.remove([25, 25, 25, 25])
            else:
                if self.energy == 0:
                    if self.bullets == 0:
                        weights.append([0, 100, 0, 0])
                    else:
                        weights.append([50, 50, 0, 0])
                if human.energy == 0:
                    if human.bullets == 1:
                        weights.append([90, 5, 3, 2])
                    else:
                        weights.append([65, 5, 15, 15])
                else:
                    if human.bullets > 0:
                        weights.append([15, 10, 35, 40])
                    else:
                        weights.append([40, 10, 50, 0])
                if (self.energy >= 3 or self.bullets == 0) and human.bullets > 1:
                    weights.append([0, 10, 40, 50])
                if self.bullets != 0 and human.bullets != 0:
                    weights.append([40, 10, 25, 25])
                if self.lives == 1:
                    weights.append([10, 10, 40, 40])
                if self.lives == 2:
                    weights.append([25, 25, 25, 25])
                if self.lives == 3:
                    weights.append([35, 35, 15, 15])
                if human.lives == 1:
                    weights.append([25, 30, 25, 20])
                if human.lives == 2:
                    weights.append([25, 25, 25, 25])
                if human.lives == 3:
                    weights.append([30, 30, 20, 20])
                if self.bullets >= 2:
                    weights.append([50, 10, 20, 20])
                if self.move_counter > 1 and self.last_moves[-2:] == [("shot", "shot"), ("shot", "shot")]:
                    weights.append([5, 5, 45, 45])
                if self.move_counter > 1 and self.last_moves[-2:] == [("load", "load"), ("load", "load")]:
                    weights.append([45, 5, 5, 45])
                if self.move_counter > 1 and self.last_moves[-1] != ("shot", "shot") and "shot" in self.last_moves[-1]:
                    weights.append([5, 5, 45, 45])
                if self.move_counter > 1 and self.last_moves[-1] == ("shot", "shot"):
                    weights.append([15, 5, 35, 45])
                if self.move_counter > 2 and "shot" not in (self.last_moves[-1], self.last_moves[-2]):
                    weights.append([45, 5, 5, 45])
                if self.move_counter > 2 and "shot" in self.last_moves[-1] and "shot" in self.last_moves[-2]:
                    weights.append([15, 10, 40, 35])

            option = choices(options, weights=choice(weights))[0]
            self.option = option if option.validate_profile(self, False) else None
        self.option(self)
        # print(weights)  # for debugging
        # print(self.last_moves)  # for debugging

    def reset(self):
        self.lives = system.MAX_LIVES
        self.energy = system.MAX_ENERGY
        self.bullets = 0
        self.shield = False
        self.option = None

        self.move_counter = 0
        self.last_moves = list()

    def __repr__(self):
        return (f"Dealer __repr__:\n"
                f"lives: {self.lives}, energy: {self.energy}, bullets: {self.bullets}, option: {self.option.NAME}\n")


human = Human("You")
bot = Bot("Dealer")


class Game:
    @staticmethod
    def is_end():
        if human.lives == 0:
            print(system.communicate(">>> You have 0 lives. You lost.\n", "LIGHTRED_EX"))
            input(system.communicate("Press ENTER to quit", "LIGHTRED_EX"))
            sleep(0.5)
            return True
        elif bot.lives == 0:
            print(system.communicate(">>> Dealer has 0 lives. You won.\n", "LIGHTGREEN_EX"))
            input(system.communicate("Press ENTER to quit", "LIGHTRED_EX"))
            sleep(0.5)
            return True
        return False

    @staticmethod
    def validate_move(pl1, pl2):
        flag = False
        communicates = (">>> Nothing happened.\n", f">>> {pl2.name} -1HP.\n", f">>> {pl2.name} blocked the shot.\n", f">>> {pl2.name} deflected the shot. {pl1.name} -1HP.\n")
        communicate = None

        if pl1.option == shot and pl2.option == shot:
            pl1.bullets += 1
            pl2.bullets += 1
            communicate = communicates[0]
        elif pl1.option == shot and pl2.option == load:
            pl2.lives -= 1
            communicate = communicates[1]
        elif pl1.option == shot and pl2.option == block:
            communicate = communicates[2]
        elif pl1.option == shot and pl2.option == deflect:
            pl1.lives -= 1
            communicate = communicates[3]
        elif pl1.option in (load, block, deflect) and pl2.option != shot:
            communicate = communicates[0]
        else:
            flag = True

        if not flag:
            os.system("cls")
            print(system.communicate(f"\n*** MOVE #{bot.move_counter} INFO ***\n", "LIGHTWHITE_EX"))
            print(system.communicate(f"- {pl1.name}: {pl1.option.NAME}\n- {pl2.name}: {pl2.option.NAME}","LIGHTWHITE_EX"))
            print(system.communicate(communicate, "LIGHTWHITE_EX"))

        return flag

    def __call__(self):
        os.system("cls")
        print(system.communicate("The duel has begun.\n", "LIGHTRED_EX"))

        human.reset()
        bot.reset()

        while not self.is_end():
            human.move()
            bot.move()

            bot.last_moves.append((human.option.NAME, bot.option.NAME))
            if len(bot.last_moves) >= 5:
                del bot.last_moves[-1]

            if self.validate_move(human, bot):
                self.validate_move(bot, human)
            human.option = bot.option = None


game = Game()
