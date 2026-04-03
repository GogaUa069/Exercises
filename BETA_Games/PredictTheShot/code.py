import os
from abc import ABC, abstractmethod
from time import sleep
from random import randint, choice
from colorama import Fore, Style


class System:
    MAX_BULLETS = 6
    MAX_ENERGY = 6
    MAX_LIVES = 3

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
        if player.energy in range(1, 7):
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
        if player.energy in range(3, 7):
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
            case _:
                print(system.communicate("ERROR: Select one of the options shown above!\n", "LIGHTRED_EX"))

    def move(self):
        print(system.communicate(">>> Your move...\n", "LIGHTRED_EX"))
        print(self)
        while self.option is None:
            print(system.communicate("Select one of the options shown below:", "CYAN"))
            print(system.communicate("1. Shot\n2. Load\n3. Block\n4. Deflect", "LIGHTWHITE_EX"))
            self.validate_option(input(system.communicate("<<< ", "LIGHTWHITE_EX")))
        self.option(self)

    def __str__(self):
        return system.communicate(f"*** INFO ***\n"
                                  f"- Lives: {self.lives}/{system.MAX_LIVES}\n"
                                  f"- Energy: {self.energy}\n"
                                  f"- Bullets: {self.bullets}\n"
                                  f"* Dealer lives: {bot.lives}/{system.MAX_LIVES}\n",
                                  "LIGHTWHITE_EX")


class Bot(Player):
    def move(self):
        print(system.communicate("\n>>> Dealer's move...\n", "LIGHTRED_EX"))
        sleep(randint(1, 3))
        while self.option is None:
            option = choice((shot, load, block, deflect))
            self.option = option if option.validate_profile(self, False) else None
        self.option(self)

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
            return True
        elif bot.lives == 0:
            print(system.communicate(">>> Dealer has 0 lives. You won.\n", "LIGHTGREEN_EX"))
            input(system.communicate("Press ENTER to quit", "LIGHTRED_EX"))
            return True
        return False

    @staticmethod
    def validate_move(pl1, pl2):
        flag = False
        communicates = (">>> Nothing happened.\n", f">>> {pl2.name} -1HP.\n", f">>> {pl2.name} blocked the shot.\n", f">>> {pl2.name} deflected the shot. {pl1.name} -1 HP.\n")
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
            print(system.communicate("\n*** MOVE INFO ***\n", "LIGHTWHITE_EX"))
            print(system.communicate(f"- {pl1.name}: {pl1.option.NAME}\n- {pl2.name}: {pl2.option.NAME}","LIGHTWHITE_EX"))
            print(system.communicate(communicate, "LIGHTWHITE_EX"))

        return flag

    def __call__(self):
        while not self.is_end():
            human.move()
            bot.move()
            if self.validate_move(human, bot):
                self.validate_move(bot, human)
            human.option = bot.option = None


game = Game()
game()
