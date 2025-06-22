from random import shuffle
import pygame
import time


class MusicClass:

    def __init__(self):
        pass

    def birds_sound(self):
        pygame.init()
        pygame.mixer.music.load(r"C:\Users\Егор\OneDrive\Рабочий стол\music_program\birds.wav")
        pygame.mixer.music.play(-1)

    def drums_sound(self):
        pygame.init()
        pygame.mixer.music.load(r"C:\Users\Егор\OneDrive\Рабочий стол\music_program\drums.wav")
        pygame.mixer.music.play()

    def kill_sound(self):
        pygame.init()
        pygame.mixer.music.load(r"C:\Users\Егор\OneDrive\Рабочий стол\music_program\kill.wav")
        pygame.mixer.music.play()

    def scary_piano_sound(self):
        pygame.init()
        pygame.mixer.music.load(r"C:\Users\Егор\OneDrive\Рабочий стол\music_program\scary piano.wav")
        pygame.mixer.music.play()

    def end_music(self):
        pygame.init()
        pygame.mixer.music.load(
            r"C:\Users\Егор\OneDrive\Рабочий стол\music_program\end_music.wav")
        pygame.mixer.music.play(-1)

    def steps(self):
        pygame.init()
        pygame.mixer.music.load(
            r"C:\Users\Егор\OneDrive\Рабочий стол\music_program\steps.wav")
        pygame.mixer.music.play()
        time.sleep(2.67)
        pygame.mixer.music.stop()

    def heart_beat_sound(self):
        pygame.init()
        pygame.mixer.music.load(
            r"C:\Users\Егор\OneDrive\Рабочий стол\music_program\heart_beat.wav")
        pygame.mixer.music.play()
        time.sleep(3.5)
        pygame.mixer.music.stop()

    def horror_cinema_sound(self):
        pygame.init()
        pygame.mixer.music.load(
            r"C:\Users\Егор\OneDrive\Рабочий стол\music_program\horror_cinema.wav")
        pygame.mixer.music.play()
        time.sleep(4)
        pygame.mixer.music.stop()


my_music = MusicClass()


class GameClass(MusicClass):
    def __init__(self):
        MusicClass.__init__(self)
    endings = ["\033[32m{}".format("...делится с вами своими сокровищами!"),
               "\033[31m{}".format("...моментально вас съедает!")]
    shuffle(endings)
    end1 = endings[0]
    end2 = endings[1]
    num = 0

    def start_game(self):
        print()
        print("\033[31m{}".format("*Please, always click enter to continue!"))
        time.sleep(1)
        input()
        self.birds_sound()
        print("\033[34m{}".format("Вы находитесь в землях, заселенных драконами."))
        input()
        print("Перед собой вы видите две пещеры.")
        input()
        print("В одной из них - дружелюбный дракон,")
        input()
        print("который готов поделиться с вами своими сокровищами.")
        input()
        print("Во второй - жадный и голодный дракон, который мигом вас съест.")
        input()
        pygame.mixer.music.stop()

    def question(self):
        self.scary_piano_sound()
        print("В какую пещеру вы войдете?")
        print()
        while True:
            try:
                GameClass.num = int(input("\033[0m{}".format("(нажмите клавишу 1 или 2): ")))
                if GameClass.num in [1, 2]:
                    break
                else:
                    print("Пожалуйста, введите 1 или 2.")
            except ValueError:
                print("Пожалуйста, введите число.")
        time.sleep(1.5)
        print()
        print(f"\033[1m {'Вы приближаетесь к пещере...'}\033[0m")
        self.steps()
        time.sleep(1.36)
        print(f"\033[1m {'Ее темнота заставляет вас дрожать от страха...'}\033[0m")
        self.heart_beat_sound()
        time.sleep(1)
        print(f"\033[1m {'Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...'}\033[0m")
        self.horror_cinema_sound()

    def answer(self):
        if GameClass.num == 1 and GameClass.end1 == "\033[32m{}".format("...делится с вами своими сокровищами!"):
            print(GameClass.end1)
            self.drums_sound()
        elif GameClass.num == 1 and GameClass.end1 == "\033[31m{}".format("...моментально вас съедает!"):
            print(GameClass.end1)
            self.drums_sound()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            self.kill_sound()
        elif GameClass.num == 2 and GameClass.end2 == "\033[32m{}".format("...делится с вами своими сокровищами!"):
            print(GameClass.end2)
            self.drums_sound()
        elif GameClass.num == 2 and GameClass.end2 == "\033[31m{}".format("...моментально вас съедает!"):
            print(GameClass.end2)
            self.drums_sound()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            self.kill_sound()
        print()
        time.sleep(2)
        print(f"{" " * 10}THE END!")
        time.sleep(3)


my_game = GameClass()

my_game.start_game()
my_game.question()
my_game.answer()


def creators():
    t0 = " "
    text = [f"{t0 * 5}Developers", t0, "Main creator: Pavlenko Egor", t0, "All developers: 1. Pavlenko Egor",
            t0, "Music operator: Pavlenko Egor", t0, "All music was taken from the site: Freesound.org",
            t0, f"{t0 * 5}Thank you for playing this game!"]
    for i in text:
        for j in i:
            time.sleep(0.21)
            print(j, end='', flush=True)
        print(sep='\n')
        time.sleep(1.5)


def game():
    my_game.start_game()
    my_game.question()
    my_game.answer()


my_music.end_music()


class RestartClass(GameClass):
    def __init__(self):
        GameClass.__init__(self)

    def restart(self):
        while True:
            print()
            print("*I'm so sorry for some problems with music!")
            pygame.mixer.music.unpause()
            while True:
                time.sleep(2)
                print()
                print("\033[0m{}".format("Попытаете удачу еще раз?"))
                print("\033[32m{}".format("да: 1"))
                print("\033[31m{}".format("нет: 2"))
                print("\033[0m{}".format("создатели: 3"))
                try:
                    answer = int(input("\033[0m{}".format("---> ")))
                    if answer == 1:
                        pygame.mixer.music.pause()
                        game()
                    elif answer == 3:
                        creators()
                    elif answer == 2:
                        print()
                        print("До встречи!")
                        pygame.mixer.music.stop()
                        time.sleep(1.5)
                        break
                    else:
                        print("Пожалуйста, введите 1, 2 или 3.")
                except ValueError:
                    print("Пожалуйста, введите число.")
            break


my_restart = RestartClass()

my_restart.restart()
