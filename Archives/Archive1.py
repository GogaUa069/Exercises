from random import randint


def game():
    num = 0
    random_num = randint(1, 100)
    last_num = 0
    counter = 0

    def where_is_number():
        nonlocal num, random_num, last_num, counter
        a = last_num
        b = num
        c = random_num
        if counter != 0:
            if a < b < c:
                print(f"Look for number that is bigger than {b}\n")
                last_num = num
            elif a < c < b:
                print(f"Look for number in the range {a}-{b}\n")
            elif b < a < c:
                print(f"Look for number that is bigger than {a}\n")
                last_num = num
            elif b < c < a:
                print(f"Look for number in range {b}-{a}\n")
            elif c < a < b:
                print(f"Look for number that is smaller than {a}\n")
                last_num = num
            elif c < b < a:
                print(f"Look for number that is smaller than {b}\n")
                last_num = num
        else:
            if b < c:
                print(f"Look for number that is bigger than {b}\n")
            elif b > c:
                print(f"Look for number that is smaller than {b}\n")
            last_num = num
        counter += 1

    while num != random_num:
        try:
            num = int(input("-----> "))
            if num not in range(1, 101):
                print("Please use digits in range 1-100\n")
            elif num > random_num:
                print("Your number is BIGGER than hidden number.")
                where_is_number()
            elif num < random_num:
                print("Your number is SMALLER than hidden number.")
                where_is_number()
            else:
                print("Yey! You found the hidden number!")
                break
        except ValueError:
            print("Please, use DIGITS.\n")


game()
