from colorama import Fore, Style
from string import ascii_letters as letters, digits
from random import randint
from pathlib import Path


class SignUp:
    def __init__(self):
        self.name = ""
        self.password = ""
        self.login = None

    def set_name(self):
        while True:
            print(Fore.CYAN + "\n>>> Enter Your name: (Length: 3–10; Only letters)" + Style.RESET_ALL)
            self.name = input("<<< ")

            if len(self.name) not in range(3, 11) or not all(let in letters for let in self.name):
                print(Fore.LIGHTRED_EX + ">>> Error! Invalid name." + Style.RESET_ALL)
            else:
                break

    def set_password(self):
        while True:
            print(Fore.CYAN + "\n>>> Create Your password: (Length: 5–10; Only digits)" + Style.RESET_ALL)
            self.password = input("<<< ")

            if len(self.password) not in range(5, 11) or not all(num in digits for num in self.password):
                print(Fore.LIGHTRED_EX + ">>> Error! Invalid password." + Style.RESET_ALL)
            else:
                break

    def set_login(self):
        datas_folder = Path("Datas")
        while True:
            self.login = f"{self.name}{str(randint(1, 9999)).rjust(4, '0')}"
            file_path = datas_folder / f"{self.login}.txt"
            if not file_path.exists():
                break

    def get_login(self):
        print(Fore.CYAN + f"\nYOUR LOGIN (Don't forget it!): {self.login}" + Style.RESET_ALL)

    def create_account_file(self, encoding="utf-8"):
        with open(f"Datas/{self.login}.txt", "w", encoding=encoding) as file:
            file.write(f"{self.name}\n{self.password}")

    def get_account_info(self):
        with open(f"Datas/{self.login}.txt", encoding="utf-8") as file:
            print(Fore.CYAN + "\nAccount INFO:" + Style.RESET_ALL)
            for key, value in zip(("Name", "Password"), file.readlines()):
                print(f"{key}: {value.strip()}")

    def __call__(self):
        self.set_name()
        self.set_password()
        self.set_login()
        self.get_login()
        self.create_account_file()
        self.get_account_info()


signup = SignUp()
signup()
