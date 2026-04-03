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


class Option:
    def __init__(self, name, energy):
        self.NAME = name
        self.ENERGY = energy

    def validate_profile(self, player):
        raise NotImplementedError("No method 'validate_profile' in the class.")


class Shot(Option):
    def validate_profile(self, player):
        if player.bullets != 0:
            return True
        else:
            print(system.communicate("ERROR: You have 0 bullets!\n", "LIGHTRED_EX"))
            return False

    def __call__(self, player):
        player.option = shot
        player.energy += player.option.ENERGY
        player.bullets -= 1


class Load(Option):
    def validate_profile(self, player):
        if player.bullets != system.MAX_BULLETS:
            print(system.communicate(f">>> +1 bullet. Now you have {player.bullets+1} bullet(s).\n", "CYAN"))
            return True
        else:
            print(system.communicate("ERROR: You have maximum amount of bullets!\n", "LIGHTRED_EX"))
            return False

    def __call__(self, player):
        player.option = load
        player.energy += player.option.ENERGY
        player.bullets += 1


class Block(Option):
    def validate_profile(self, player):
        if player.energy in range(1, 7):
            print(system.communicate(">>> Shield is activated.", "CYAN"))
            return True
        else:
            print(system.communicate("ERROR: You don not have enough energy!\n", "LIGHTRED_EX"))
            return False

    def __call__(self, player):
        player.option = block
        player.energy += player.option.ENERGY
        player.shield = True


class Deflect(Option):
    def validate_profile(self, player):
        if player.energy in range(3, 7):
            print(system.communicate(">>> Shield is activated.\n", "CYAN"))
            return True
        else:
            print(system.communicate("ERROR: You do not have enough energy!\n", "LIGHTRED_EX"))
            return False

    def __call__(self, player):
        player.option = deflect
        player.energy += player.option.ENERGY
        player.shield = True


shot = Shot(name="shot", energy=1)
load = Load(name="load", energy=1)
block = Block(name="block", energy=-1)
deflect = Deflect(name="deflect", energy=-3)


class Player:
    def __init__(self, name):
        self.name = name
        self.lives = system.MAX_LIVES
        self.energy = system.MAX_ENERGY
        self.bullets = 0
        self.shield = False
        self.option = None

    def move(self):
        raise NotImplementedError("No method 'move' in the class.")


class Human(Player):
    def __match_option(self, option):
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
                print(system.communicate("ERROR: Select one of the options show above!\n", "LIGHTRED_EX"))

    def move(self):
        print(system.communicate("Your move:\n", "CYAN"))
        print(self)
        while self.option is None:
            print(system.communicate("Select one of the options:", "CYAN"))
            print(system.communicate("1. Shot\n2. Load\n3. Block\n4. Deflect", "LIGHTWHITE_EX"))
            self.__match_option(input(system.communicate("<<< ", "LIGHTWHITE_EX")))
        self.option(self)

    def __str__(self):
        return system.communicate(f"*** INFO ***\n"
                                  f"- Your lives: {self.lives}\n"
                                  f"- Your energy: {self.energy}\n"
                                  f"- Your bullets: {self.bullets}\n"
                                  f"* Dealer lives: {bot.lives}\n",
                                  "LIGHTWHITE_EX")


class Bot(Player):
    def move(self):
        ...


human = Human("You")
bot = Bot("Dealer")
