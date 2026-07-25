import pygame

pygame.init()
pygame.mixer.init()

music1 = pygame.mixer.Sound("MyGames/GuessCode/GAME/Music/CasualJazz.wav")
music2 = pygame.mixer.Sound("MyGames/GuessCode/GAME/Music/EpicCreditsSoundtrack.wav")

main_channel = pygame.mixer.Channel(0)
second_channel = pygame.mixer.Channel(1)


def main_menu():
    main_channel.play(music1, loops=-1)
    playing_main = True
    print("Welcome! Press Enter to toogle music.")
    print("Playing first music")
    while True:
        input("<<< ")
        if playing_main:
            main_channel.pause()
            second_channel.play(music2, loops=-1)
            playing_main = False
            print("Playing second music.")
        else:
            second_channel.pause()
            playing_main = True
            main_channel.unpause()
            print("Playing first music")


main_menu()
