import time

import pygame


def short_beep():
    pygame.init()
    pygame.mixer.music.load(r"C:\Users\Егор\OneDrive\Рабочий стол\music_program\beep.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def long_beep():
    pygame.init()
    pygame.mixer.music.load(r"C:\Users\Егор\OneDrive\Рабочий стол\music_program\long_beep.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_code = ("•- -••• -•-• -•• • ••-• --• •••• •• •--- -•- •-•• -- -• --- •--• --•- •-• ••• - ••- •••- •-- -••-"
                 " -•-- --••").split()
numbers = "012345689"
numbers_code = ["-----", "•----", "••---", "•••--", "••••-", "•••••", "-••••", "--•••", "---••", "----•"]

symbols = "?/@"
symbols_code = ["••--••", "-••-•", "•--•-•"]


def morse_code(string):
    mylist = list()
    for j in string:
        for i in j:
            low_i = i.lower()
            if low_i in alphabet:
                mylist.append("\033[0m{}".format(alphabet_code[alphabet.index(low_i)]))
            elif i in numbers:
                mylist.append("\033[0m{}".format(numbers_code[numbers.index(i)]))
            elif i in symbols:
                mylist.append("\033[0m{}".format(symbols_code[symbols.index(i)]))
            elif i == " " or i in "_.":
                mylist.append("\033[31m{}".format("/"))
            else:
                mylist.append(i)
    print(" ".join(mylist))
    for i in mylist:
        time.sleep(1)
        for j in i:
            if j == "•":
                short_beep()
                time.sleep(0.35)
            elif j == "-":
                long_beep()
            else:
                continue


def morse_decode(string):
    mylist = list()
    for i in string.split():
        if i in alphabet_code:
            mylist.append(alphabet[alphabet_code.index(i)])
        elif i in numbers_code:
            mylist.append(numbers[numbers_code.index(i)])
        elif i in symbols_code:
            mylist.append(symbols[symbols_code.index(i)])
        elif i == "|":
            mylist.append(" ")
        else:
            mylist.append(i)
    print("".join(mylist).title())


def which_morse():
    answer = ""
    print("Please, enter 'coding'/'decoding'")
    while answer.lower() not in ("coding", "decoding", ):
        answer = input("-----> ")
    if answer.lower() == "coding":
        print("Enter string")
        morse_code(input("-----> "))
    elif answer.lower() == "decoding":
        print("Enter string")
        morse_decode(input("-----> "))


which_morse()
