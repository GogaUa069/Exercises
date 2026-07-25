from random import shuffle, randint
from time import sleep
from colorama import Fore, Style


def communicate(text, color):
    return getattr(Fore, color) + text + Style.RESET_ALL


class Game:
    def __init__(self):
        self.live = randint(1, 3)
        self.blank = 6-self.live
        self.cylinder = [0]*self.blank + [1]*self.live
        shuffle(self.cylinder)
        self.player = self.dealer = True

    def is_over(self):
        return True if self.player and self.dealer and not all(chamber == 1 for chamber in self.cylinder) else False

    def player_shot(self):
        print(f"\nChance to die: {self.cylinder.count(1)}/{len(self.cylinder)}")
        input(communicate("Press ENTER to shot", "CYAN"))
        bullet = self.cylinder[0]
        del self.cylinder[0]
        if bullet:
            self.player = False
            print(communicate("You dead.", "LIGHTRED_EX"))
        else:
            print(communicate("You alive.", "LIGHTGREEN_EX"))
            shuffle(self.cylinder)

    def player_move(self):
        self.player_shot()
        while self.player:
            print(f"\nChance to die: {self.cylinder.count(1)}/{len(self.cylinder)}")
            print(communicate("Shot or stay?", "CYAN"))
            answer = input("<<< ")
            match answer:
                case "1" | "shot":
                    self.player_shot()
                case "2" | "stay":
                    break
                case _:
                    print(communicate("Select one of the options shown above!", "LIGHTRED_EX"))

    def dealer_move(self):
        print(f"\nChance to win: {self.cylinder.count(1)}/{len(self.cylinder)}")
        print(communicate("Dealers move...", "CYAN"))
        sleep(randint(1, 3))
        bullet = self.cylinder[0]
        del self.cylinder[0]
        if bullet:
            self.dealer = False
            print(communicate("Dealer is out...", "LIGHTGREEN_EX"))
            input(communicate("\nPress ENTER to leave", "LIGHTRED_EX"))
        else:
            print(communicate("Dealer alive.", "LIGHTRED_EX"))
            shuffle(self.cylinder)

    def __call__(self):
        while True:
            self.player_move()
            if not self.is_over():
                break
            self.dealer_move()
            if not self.is_over():
                break


game = Game()
game()
