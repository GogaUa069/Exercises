# Rewatch SHIELD in human and bot.
# Errors to SYSTEM

from system import *


class Option(ABC):
    def __init__(self, name: str, energy: int):
        self.NAME = name.upper()
        self.ENERGY = energy

    @abstractmethod
    def validate_player(self, player, is_human=True):
        pass


class Shot(Option):
    def validate_player(self, player, is_human=True):
        if player.BULLETS != 0:
            return True
        else:
            if is_human:
                system.error("No bullets remaining.")
            return False

    def __call__(self, player):
        player.OPTION = shot
        player.ENERGY += player.OPTION.ENERGY if player.ENERGY + player.OPTION.ENERGY <= system.MAX_ENERGY else 0
        player.BULLETS -= 1


class Load(Option):
    def validate_player(self, player, is_human=True):
        if player.BULLETS != system.MAX_BULLETS:
            if is_human:
                form = "bullets" if player.BULLETS + 1 > 1 else "bullet"
                print(system.communicate(f">>> +1 bullet. You now have {player.BULLETS + 1} {form}.", "CYAN"))

            return True
        else:
            if is_human:
                system.error("Ammo is already full.")
            return False

    def __call__(self, player):
        player.OPTION = load
        player.ENERGY += player.OPTION.ENERGY if player.ENERGY + player.OPTION.ENERGY <= system.MAX_ENERGY else 0
        player.BULLETS += 1


class Block(Option):
    def validate_player(self, player, is_human=True):
        if player.ENERGY + self.ENERGY >= 0:
            if is_human:
                print(system.communicate(">>> Shield activated.", "CYAN"))
            return True
        else:
            if is_human:
                system.error("You do not have enough energy. Required: 2.")
            return False

    def __call__(self, player):
        player.OPTION = block
        player.ENERGY += player.OPTION.ENERGY


class Deflect(Option):
    def validate_player(self, player, is_human=True):
        if player.ENERGY + self.ENERGY >= 0:
            if is_human:
                print(system.communicate(">>> Shield activated.", "CYAN"))
            return True
        else:
            if is_human:
                system.error("You do not have enough energy. Required: 3.")
            return False

    def __call__(self, player):
        player.OPTION = deflect
        player.ENERGY += player.OPTION.ENERGY


shot = Shot(name="shot", energy=1)
load = Load(name="load", energy=1)
block = Block(name="block", energy=-2)
deflect = Deflect(name="deflect", energy=-3)


class Player(ABC):
    def __init__(self, name: str):
        self.NAME = name.capitalize()
        self.LIVES = system.MAX_LIVES
        self.ENERGY = system.MAX_ENERGY
        self.BULLETS = 0
        self.OPTION = None

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def reset(self):
        pass


class Human(Player):
    def __validate_answer(self, option):
        match option.upper():
            case "1" | "SHOT":
                self.OPTION = shot if shot.validate_player(self) else None
            case "2" | "LOAD":
                self.OPTION = load if load.validate_player(self) else None
            case "3" | "BLOCK":
                self.OPTION = block if block.validate_player(self) else None
            case "4" | "DEFLECT":
                self.OPTION = deflect if deflect.validate_player(self) else None
            case _:
                system.error("Select one of the options shown above.")

    def move(self):
        print(system.communicate("\n>>> Your move...\n", "LIGHTRED_EX"))
        print(self)
        while self.OPTION is None:
            print(system.communicate("\nSelect one of the options shown below:", "CYAN"))
            print(system.communicate("1. SHOT\n2. LOAD\n3. BLOCK\n4. DEFLECT", "LIGHTWHITE_EX"))
            self.__validate_answer(input(system.INPUT))
        self.OPTION(self)

    def reset(self):
        self.LIVES = system.MAX_LIVES
        self.ENERGY = system.MAX_ENERGY
        self.BULLETS = 0
        self.OPTION = None

    def __str__(self):
        return system.communicate(f"*** INFO ***\n"
                                  f"- LIVES: {self.LIVES}/{system.MAX_LIVES}\n"
                                  f"- ENERGY: {self.ENERGY}/{system.MAX_ENERGY}\n"
                                  f"- BULLETS: {self.BULLETS}/{system.MAX_BULLETS}\n"
                                  f"* DEALER LIVES: {bot.LIVES}/{system.MAX_LIVES}", "LIGHTWHITE_EX")


class Bot(Player):
    def __init__(self, name):
        super().__init__(name)
        self.move_counter = 0
        self.last_moves = list()
        self.human_moves = dict().fromkeys(("SHOT", "LOAD", "BLOCK", "DEFLECT"), 0)

    def set_weights(self):
        self.move_counter += 1
        weights = [(25, 25, 25, 25)]

        if self.move_counter == 1:
            weights = [(0, 100, 0, 0)]
        else:
            if human.ENERGY == 0 and human.BULLETS == 0:
                weights.append((80, 10, 5, 5))
            if human.ENERGY == 0 and human.BULLETS > 0:
                weights.append((40, 10, 25, 25))
            if human.ENERGY > 0 and human.BULLETS == 0:
                weights.append((25, 25, 25, 25))
            if human.ENERGY > 0 and human.BULLETS > 0:
                weights.append((25, 25, 25, 25))
            if human.LIVES == 1:
                weights.append((25, 30, 25, 20))
            if human.LIVES == 2:
                weights.append((25, 25, 25, 25))
            if human.LIVES == 3:
                weights.append((30, 30, 20, 20))
            if bot.ENERGY == 0 and bot.BULLETS > 0:
                weights.append((50, 50, 0, 0))
            if bot.ENERGY > 0 and bot.BULLETS == 0:
                weights.append((0, 10, 30, 30))
            if bot.ENERGY > 0 and bot.BULLETS > 0:
                weights.append((25, 25, 25, 25))
            if bot.LIVES == 1:
                weights.append((10, 10, 40, 40))
            if bot.LIVES == 2:
                weights.append((25, 25, 25, 25))
            if bot.LIVES == 3:
                weights.append((35, 35, 15, 15))
            if bot.BULLETS >= 2:
                weights.append((25, 10, 25, 25))
            if self.move_counter > 2 and self.last_moves[-2:] == [("SHOT", "SHOT"), ("SHOT", "SHOT")]:
                weights.append((5, 5, 45, 45))
            if self.move_counter > 2 and self.last_moves[-2:] == [("LOAD", "LOAD"), ("LOAD", "LOAD")]:
                weights.append((45, 5, 5, 45))
            if self.move_counter > 2 and all("LOAD" in pair for pair in self.last_moves[-2:]):
                weights.append((45, 5, 5, 45))
            if self.move_counter > 2 and not any("SHOT" in pair for pair in self.last_moves[-2:]):
                weights.append((15, 10, 40, 35))
            if self.move_counter > 2 and all("BLOCK" in pair for pair in self.last_moves[-2:]):
                weights.append((25, 25, 10, 10))
            if self.move_counter > 1 and "SHOT" in self.last_moves[-1]:
                weights.append((5, 5, 45, 45))
            match max(self.human_moves, key=lambda x: self.human_moves[x]):
                case "SHOT":
                    weights.append((20, 20, 30, 30))
                case "LOAD":
                    weights.append((40, 20, 20, 20))
                case "BLOCK" | "DEFLECT":
                    weights.append((20, 40, 20, 20))

        return weights

    def move(self):
        print(system.communicate(f"\n>>> {self.NAME}'s move...", "LIGHTRED_EX"))
        sleep(randint(1, 3))

        options = [shot, load, block, deflect]

        while self.OPTION is None:
            weights = self.set_weights()
            option = choices(options, weights=choice(weights))[0]
            self.OPTION = option if option.validate_player(self, False) else None

        self.OPTION(self)

        # print(self)  # Debugging.

    def reset(self):
        self.LIVES = system.MAX_LIVES
        self.ENERGY = system.MAX_ENERGY
        self.BULLETS = 0
        self.OPTION = None

        self.move_counter = 0
        self.last_moves = list()
        self.human_moves = dict().fromkeys(("shot", "load", "block", "deflect"), 0)

    def __repr__(self):
        return (f"Dealer __repr__:\n"
                f"- LIVES: {self.LIVES}/{system.MAX_LIVES}\n"
                f"- ENERGY: {self.ENERGY}/{system.MAX_ENERGY}\n"
                f"- BULLETS: {self.BULLETS}/{system.MAX_BULLETS}\n"
                f"- OPTION: {self.OPTION.NAME}")


human = Human("You")
bot = Bot("Dealer")


class Game:
    @staticmethod
    def is_end():
        if human.LIVES == 0:
            print(system.communicate("\n>>> You have 0 lives. You lost.", "LIGHTRED_EX"))
            input(system.communicate("\n[ENTER] to quit", "LIGHTRED_EX"))
            return True
        elif bot.LIVES == 0:
            print(system.communicate("\n>>> Dealer has 0 lives. You won.", "LIGHTGREEN_EX"))
            print(system.communicate("* PTS 2D?! *", "WHITE"))
            input(system.communicate("\n[ENTER] to quit", "LIGHTRED_EX"))
            return True
        return False

    @staticmethod
    def validate_move(pl1, pl2):
        flag = False
        communicates = (">>> Nothing happened.", f">>> {pl2.NAME} -1HP.", f">>> {pl2.NAME} blocked the shot.", f">>> {pl2.NAME} deflected the shot. {pl1.NAME} -1HP.")
        communicate = None

        if pl1.OPTION == shot and pl2.OPTION == shot:
            pl1.BULLETS += 1
            pl2.BULLETS += 1
            communicate = communicates[0]
        elif pl1.OPTION == shot and pl2.OPTION == load:
            pl2.LIVES -= 1
            communicate = communicates[1]
        elif pl1.OPTION == shot and pl2.OPTION == block:
            communicate = communicates[2]
        elif pl1.OPTION == shot and pl2.OPTION == deflect:
            pl1.LIVES -= 1
            communicate = communicates[3]
        elif pl1.OPTION in (load, block, deflect) and pl2.OPTION != shot:
            communicate = communicates[0]
        else:
            flag = True

        if not flag:
            system.clear_console()
            print(system.communicate(f"\n*** MOVE #{bot.move_counter} INFO ***\n", "LIGHTWHITE_EX"))
            print(system.communicate(f"- {pl1.NAME}: {pl1.OPTION.NAME}\n- {pl2.NAME}: {pl2.OPTION.NAME}","LIGHTWHITE_EX"))
            print(system.communicate(communicate, "LIGHTWHITE_EX"))

        return flag

    def __call__(self):
        system.clear_console()
        print(system.communicate("The duel has begun.", "LIGHTRED_EX"))

        human.reset()
        bot.reset()

        while not self.is_end():
            human.move()
            bot.move()

            bot.last_moves.append((human.OPTION.NAME, bot.OPTION.NAME))
            bot.human_moves[bot.last_moves[-1][0].lower()] += 1

            if len(bot.last_moves) == 5:
                del bot.last_moves[0]

            if self.validate_move(human, bot):
                self.validate_move(bot, human)

            human.OPTION = bot.OPTION = None


game = Game()
