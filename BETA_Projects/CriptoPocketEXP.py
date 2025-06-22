from colorama import Fore, Style
from accessify import private, protected


class App:

    @classmethod
    def start_menu(cls):
        while True:
            print("Start menu\n"
                  "1. Login\n"
                  "2. Sign up\n"
                  "3. Exit\n")
            answer = input("-----> ")
            match answer.upper():
                case "LOGIN" | "1":
                    ...
                case "SIGN UP" | "2":
                    ...
                case "EXIT" | "3":
                    ...
                case _:
                    print(Fore.RED + "Enter number in range 1-3" + Style.RESET_ALL)

    @classmethod
    def main_menu(cls):
        while True:
            print("Main menu:\n"
                  "1. Account info\n"  # <--------- Shows account info: Name, password, Balance
                  "2. Balance\n"  # <---------- You can deposit money here
                  "3. Settings\n")  # < -------- Settings: Log out, exit, change info
            answer = input("-----> ")
            match answer.upper():
                case "ACCOUNT INFO" | "1":
                    ...
                case "BALANCE":
                    ...
                case "EXIT":
                    ...
                case _:
                    print(Fore.RED + "Enter number in range 1-3" + Style.RESET_ALL)


application = App()


class Pocket:
    def __init__(self, name="", password="", balance=0):
        self.__NAME = name
        self.__PASSWORD = password
        self.__BALANCE = balance

