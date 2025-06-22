import time


def creators():
    t0 = " "
    t1 = f"{t0*5}Developers"
    t2 = "Main creator: Pavlenko Egor"
    t3 = "All developers: 1. Pavlenko Egor"
    t4 = "Music operator: Pavlenko Egor"
    t5 = "All music was taken from the site: Freesound.org"
    t6 = "Thank you for playing this game!"
    mylist = [t1, t0, t2, t0, t3, t0, t4, t0, t5, t0, t6]
    for i in mylist:
        for j in i:
            time.sleep(0.21)
            print(j, end='', flush=True)
        print(sep='\n')
        time.sleep(1.5)


creators()
