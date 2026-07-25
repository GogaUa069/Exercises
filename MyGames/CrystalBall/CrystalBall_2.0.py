from tqdm import tqdm
from random import choice
import time
from colorama import Style, Fore
import pygame
import os

pygame.init()

outstanding_answers = ["It's certain", "It's decidedly so", "Without a doubt", "Yes - definitely", "You may rely on it"]
good_answers = ["As I see it, yes", "Most likely", "Outlook good", "Signs point to yes", "Yes"]
average_answers = ["Reply hazy, try again", "Ask again later", "Better not tell You now", "Cannot predict now", "Concentrate and ask again"]
bad_answers = ["Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

answer_dict = {Fore.LIGHTGREEN_EX + "outstanding!": outstanding_answers,
               Fore.GREEN + "good!": good_answers,
               Fore.LIGHTYELLOW_EX + "average": average_answers,
               Fore.LIGHTRED_EX + "bad...": bad_answers}


class CrystalBall:
    CRYSTAL_BALL_SOUND = pygame.mixer.Sound("Audio/MagicCircleSound.wav")

    @staticmethod
    def greetings():
        print(Fore.LIGHTCYAN_EX + "Hello! I'm a Crystal Ball, and I know the answer to Your every question.\n" + Style.RESET_ALL)
        time.sleep(0.5)

    @staticmethod
    def get_answer():
        answer_type = choice(list(answer_dict))
        answer = choice(answer_dict[answer_type])
        print(Fore.LIGHTWHITE_EX + f"My answer is {answer_type} - {answer}\n" + Style.RESET_ALL)

    @staticmethod
    def loading():
        with tqdm(total=100) as pbar:
            for i in range(100):
                color = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA][i % 6]
                pbar.set_description_str(color + "Please wait, I'm thinking..." + Style.RESET_ALL)
                pbar.update(1)
                time.sleep(0.03)

    def get_question(self):
        print(Fore.LIGHTBLUE_EX + "\nWhat's Your question?")
        input("<<< " + Style.RESET_ALL)
        print()
        self.CRYSTAL_BALL_SOUND.play()
        self.loading()
        self.get_answer()

    def crystal_ball(self):
        self.greetings()
        answer = ""
        while answer.upper() not in ("LEAVE", "2"):
            print(Fore.LIGHTWHITE_EX + "1. Ask a question\n""2. Leave")
            answer = input("<<< " + Style.RESET_ALL)
            match answer.upper():
                case "ASK" | "QUESTION" | "1":
                    os.system("cls")
                    self.get_question()
                case "LEAVE" | "2":
                    os.system("cls")
                    print(Fore.LIGHTCYAN_EX + "Goodbye!")
                    time.sleep(1.5)
                case _:
                    print(Fore.LIGHTRED_EX + "Please, enter 1 or 2\n" + Style.RESET_ALL)


cristal_ball = CrystalBall()
cristal_ball.crystal_ball()
