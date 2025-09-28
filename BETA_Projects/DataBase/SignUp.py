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
            print(Fore.CYAN + "\n>>> Create Your password: (Length: 5–20)" + Style.RESET_ALL)
            self.password = input("<<< ")

            if len(self.password) not in range(5, 21) or not all(num in digits+letters for num in self.password):
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
        print(Fore.CYAN + f"\n>>> YOUR LOGIN (Don't forget it!): {self.login}" + Style.RESET_ALL)

    def create_account_file(self, encoding="utf-8"):
        with open(f"Datas/{self.login}.txt", "w", encoding=encoding) as file:
            file.write(f"{self.name}\n{self.password}")

    def get_account_info(self):
        with open(f"Datas/{self.login}.txt", encoding="utf-8") as file:
            print(Fore.CYAN + "\n>>> Account INFO:" + Style.RESET_ALL)
            for key, value in zip(("Name", "Password"), file.readlines()):
                print(f"{key}: {value.strip()}")

    def __call__(self):
        print(Fore.CYAN + ">>> Signing Up" + Style.RESET_ALL)
        self.set_name()
        self.set_password()
        self.set_login()
        self.get_login()
        self.create_account_file()
        self.get_account_info()


# signup = SignUp()
# signup()


class LogIn:
    def __init__(self):
        self.login = self.password = ""

    @staticmethod
    def search_login(login):
        datas_path = Path("Datas")
        file_path = datas_path / f"{login}.txt"
        if not file_path.exists():
            print(Fore.LIGHTRED_EX + f"Not found account with login: {login}" + Style.RESET_ALL)
            return False
        return True

    def password_checking(self, password, encoding="utf-8"):
        with open(f"Datas/{self.login}.txt", "r", encoding=encoding) as file:
            for indx, line in enumerate(list(file.readlines())):
                if indx == 0:
                    name = line
                if indx == 1:
                    if password == line:
                        print(Fore.LIGHTCYAN_EX + f"WELCOME! {name}" + Style.RESET_ALL)
                        return True
            return False

    def check_login(self):
        while True:
            print(Fore.CYAN + "\n>>> Enter Your login:" + Style.RESET_ALL)
            self.login = input("<<< ")
            if self.search_login(self.login):
                break

    def check_password(self):
        while True:
            print(Fore.CYAN + "\n>>> Enter You password:" + Style.RESET_ALL)
            self.password = input("<<< ")
            if self.password_checking(self.password):
                break

    def __call__(self, *args, **kwargs):
        self.check_login()
        self.check_password()


login = LogIn()
signup = SignUp()


class App:

    @staticmethod
    def main_menu():
        answer = ""

        while answer not in ("QUIT", "3"):
            print(Fore.LIGHTRED_EX + ">>> Main Menu:" + Style.RESET_ALL)
            print(Fore.BLUE + "1. LogIn\n"
                              "2. SignUp\n"
                              "3. Quit" + Style.RESET_ALL)
            answer = input("<<< ")
            match answer.upper():
                case "LOGIN" | "1":
                    login()
                case "SIGNUP" | "2":
                    signup()
                case "QUIT" | "3":
                    print("Goodbye!")
                    break
                case _:
                    print("Enter LOGIN/SIGNUP/QUIT")


app = App()
app.main_menu()
