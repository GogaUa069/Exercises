from colorama import Fore, Style
from random import shuffle
from pygame import init, mixer
import pygame
import time

init()


class Music:

    @staticmethod
    def birds():
        mixer.music.load(r"C:\Users\Егор\OneDrive\Рабочий стол\music_program\birds.wav")
        mixer.music.play(-1)

    @staticmethod
    def drums():
        mixer.music.load(r"C:\Users\Егор\OneDrive\Рабочий стол\music_program\drums.wav")
        mixer.music.play()
        while mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    @staticmethod
    def death():
        mixer.music.load(r"C:\Users\Егор\OneDrive\Рабочий стол\music_program\kill.wav")
        mixer.music.play()
        while mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    @staticmethod
    def scary_piano():
        mixer.music.load(r"C:\Users\Егор\OneDrive\Рабочий стол\music_program\scary piano.wav")
        mixer.music.play()

    @staticmethod
    def end_music():
        mixer.music.load(r"C:\Users\Егор\OneDrive\Рабочий стол\music_program\end_music.wav")
        mixer.music.play(-1)

    @staticmethod
    def steps():
        mixer.music.load(r"C:\Users\Егор\OneDrive\Рабочий стол\music_program\steps.wav")
        mixer.music.play()
        time.sleep(2.67)
        mixer.music.stop()

    @staticmethod
    def heart_beat():
        mixer.music.load(r"C:\Users\Егор\OneDrive\Рабочий стол\music_program\heart_beat.wav")
        mixer.music.play()
        time.sleep(3.5)
        mixer.music.stop()

    @staticmethod
    def horror_cinema():
        mixer.music.load(r"C:\Users\Егор\OneDrive\Рабочий стол\music_program\horror_cinema.wav")
        mixer.music.play()
        time.sleep(4)
        mixer.music.stop()


music = Music()


class Game:

    def __init__(self):
        self.__endings = [Fore.GREEN + "...делится с вами своими сокровищами!",
                          Fore.RED + "...моментально вас съедает!"]
        self.answer = None

    @staticmethod
    def monologues():
        print(Fore.RED + "\nДля продолжения жмите Enter" + Style.RESET_ALL)
        input()
        music.birds()
        print(Fore.BLUE + "Вы находитесь в землях, заселенных драконами.")
        input()
        print("Перед собой вы видите две пещеры.")
        input()
        print("В одной из них - дружелюбный дракон, который готов поделиться с вами своими сокровищами.")
        input()
        print("Во второй - жадный и голодный дракон, который мигом вас съест.")
        input()
        print("Но вы не знаете какой дракон в какой пещере." + Style.RESET_ALL)
        input()
        mixer.music.stop()

    @staticmethod
    def ending_monologue():
        print()
        print(f"\033[1m {'Вы приближаетесь к пещере...'}\033[0m")
        music.steps()
        time.sleep(1.36)
        print(f"\033[1m {'Ее темнота заставляет вас дрожать от страха...'}\033[0m")
        music.heart_beat()
        time.sleep(1)
        print(f"\033[1m {'Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...'}\033[0m")
        music.horror_cinema()

    def get_ending(self):
        self.ending_monologue()
        shuffle(self.__endings)
        end = self.__endings[self.answer-1]
        print(end)
        music.drums()
        if end == "...моментально вас съедает!":
            music.death()
        print(f"\n{" "*10}КОНЕЦ\n" + Style.RESET_ALL)
        time.sleep(3)
        music.end_music()
        restart()

    def which_cave(self):
        music.scary_piano()
        print("В какую пещеру вы войдете?")
        print("Нажмите клавишу 1 или 2\n")

        while True:
            try:
                self.answer = int(input("-----> "))
                if self.answer not in (1, 2):
                    print(Fore.RED + "Нажмите клавишу 1 или 2\n" + Style.RESET_ALL)
                    continue
            except ValueError:
                print(Fore.RED + "Пожалуйста, введите число.\n" + Style.RESET_ALL)
                continue

            break

        self.get_ending()


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


def kod():
    game = Game()
    game.monologues()
    game.which_cave()


def restart():
    print("Попытаете удачу еще раз?")
    print(Fore.BLUE + "Да: 1" + Style.RESET_ALL)
    print(Fore.RED + "Нет: 2" + Style.RESET_ALL)
    print("Создатели: 3")

    while True:
        try:
            answer = int(input("-----> "))
            if answer == 1:
                kod()
            elif answer == 2:
                print("\nДо встречи!")
                mixer.music.stop()
                time.sleep(1.5)
                break
                break
                break
                break
            elif answer == 3:
                mixer.music.stop()
                creators()
            else:
                print("Введите 1, 2 или 3")
        except ValueError:
            print("Введите число.")


kod()
