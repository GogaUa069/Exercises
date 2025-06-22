import random
import time


def step_stop():
    print()
    time.sleep(0.5)


class PasswordParameter:

    digits = [str(i) for i in range(10)]
    lowercase = [chr(i) for i in range(97, 123)]
    uppercase = [chr(i) for i in range(65, 91)]
    symbols = "! # $ & * + - ? @ ^ _".split()

    def __init__(self, amount, length):
        self.amount = amount
        self.length = length

    def get_params(self):
        self.amount = 0
        self.length = 0

        print("Please, enter number of passwords. (Min-1, Max-10)")
        while self.amount not in range(1, 11):
            try:
                self.amount = int(input("-----> "))
                if self.amount not in range(1, 11):
                    print("Number is out of range!\nPlease, enter number in range 1-10")
                    step_stop()

            except ValueError:
                print("Please, enter NUMBER, in range 1-10")
                step_stop()
        step_stop()

        print("Please, enter length of one password. (Min-5, Max-15)")
        while self.length not in range(5, 16):
            try:
                self.length = int(input("-----> "))
                if self.length not in range(5, 16):
                    print("Number is out of range!\nPlease, enter number in range 5-15")
                    step_stop()

            except ValueError:
                print("Please, enter NUMBER, in range 5-15")
                step_stop()
        step_stop()


class WhichChars:

    options = ["y", "n"]

    def __init__(self, chars):
        self.chars = chars

    def get_chars(self):
        self.chars = list()

        def is_digit():
            answer = ""
            print(f"Whether to include NUMBERS? {"".join(PasswordParameter.digits)}\nEnter Y or N")
            while answer.lower() not in WhichChars.options:
                answer = input("-----> ")
                if answer not in WhichChars.options:
                    print("Please, enter Y or N")
                    step_stop()
            if answer.lower() == "y":
                self.chars.append(" ".join(PasswordParameter.digits).split())

        def is_lowercase():
            answer = ""
            print(f"Whether to include LOWERCASE LETTERS? {"".join(PasswordParameter.lowercase)}\nEnter Y or N")
            while answer.lower() not in WhichChars.options:
                answer = input("-----> ")
                if answer not in WhichChars.options:
                    print("Please, enter Y or N")
                    step_stop()
            if answer.lower() == "y":
                self.chars.append(" ".join(PasswordParameter.lowercase).split())

        def is_uppercase():
            answer = ""
            print(f"Whether to include UPPERCASE LETTERS? {"".join(PasswordParameter.uppercase)}\nEnter Y or N")
            while answer.lower() not in WhichChars.options:
                answer = input("-----> ")
                if answer not in WhichChars.options:
                    print("Please, enter Y or N")
                    step_stop()
            if answer.lower() == "y":
                self.chars.append(" ".join(PasswordParameter.uppercase).split())

        def is_symbol():
            answer = ""
            print(f"Whether to include SYMBOLS? {"".join(PasswordParameter.symbols)}\nEnter Y or N")
            while answer.lower() not in WhichChars.options:
                answer = input("-----> ")
                if answer not in WhichChars.options:
                    print("Please, enter Y or N")
                    step_stop()
            if answer.lower() == "y":
                self.chars.append(" ".join(PasswordParameter.symbols).split())

        is_digit()
        step_stop()
        is_lowercase()
        step_stop()
        is_uppercase()
        step_stop()
        is_symbol()
        step_stop()


class GenPassword(PasswordParameter, WhichChars):
    def __init__(self, password):
        self.password = password

        PasswordParameter.__init__(self, amount="", length="")
        WhichChars.__init__(self, chars="")

    def gen_password(self):
        for j in range(self.amount):
            if len(self.chars) == 0:
                print("\033[31m{}".format("Error: Can't generate password(s). No arguments were given."))
                time.sleep(1)
                print("\033[31m{}".format("Tip: Try to add something"))
                break
            else:
                self.password = list()
                while len(self.password) != self.length:
                    for i in range(len(self.chars)):
                        self.password.append(random.choice(self.chars[i]))
                        if len(self.password) == self.length:
                            break
                random.shuffle(self.password)
                print(f"{j+1}. {"".join(self.password)}")

        step_stop()
        print("\033[0m{}".format("You can also change these passwords to suit yourself."))


my_password = GenPassword(password="")


def generation():
    my_password.get_params()
    my_password.get_chars()
    my_password.gen_password()


generation()
