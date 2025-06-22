import time
import pygame

pygame.init()
pygame.mixer.music.load(r"C:\Users\Егор\OneDrive\Рабочий стол\music_program\happy_birthday_jazz.wav")
pygame.mixer.music.play(-1)


t1 = "\033[34m{}".format("Happy Birthday to You!")
t2 = "\033[32m{}".format("Happy Birthday to You!")
t3 = "\033[33m{}".format("Happy Birthday Dear Alex...")
t4 = "\033[31m{}".format("Happy Birthday to You.")
t5 = '***************'
t6 = "\033[31m{}".format("From good friends and true,")
t7 = "\033[33m{}".format("From old friends and new,")
t8 = "\033[32m{}".format("May good luck go with you,")
t9 = "\033[34m{}".format("And happiness too...")
mylist = [t1, t2, t3, t4, t5, t6, t7, t8, t9]
for i in mylist:
    for j in i:
        time.sleep(0.24)
        print(j, end='', flush=True)
    print(sep='\n')
    time.sleep(0.5)
print("***************")
print("\033[31m{}".format("Happy birthday DADDY!!!"))
time.sleep(2)
pygame.mixer.music.stop()
