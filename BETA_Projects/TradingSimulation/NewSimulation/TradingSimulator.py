from colorama import Fore, Style
from secrets import choice, randbelow
from string import ascii_letters as letters, digits

INPUT = Fore.LIGHTWHITE_EX + "<<< " + Style.RESET_ALL


class Account:
    CHARS = letters + digits

    def __init__(self, name: str, last_name: str, phone_number: str, email: str):
        self.name = name.strip().capitalize()
        self.last_name = last_name.strip().capitalize()
        self.phone_number = phone_number.strip()
        self.email = email.strip()

    @staticmethod
    def _get_privacy_agreement(encoding="utf-8"):
        try:
            with open("PrivacyAgreement", "r", encoding=encoding) as file:
                for line in file:
                    print(Fore.LIGHTWHITE_EX + line + Style.RESET_ALL, end="")
            print()
        except FileNotFoundError:
            print("PrivacyAgreement file not found.")
            return

    def _privacy_agreement_acceptation(self):
        while True:
            code = "".join([choice(self.CHARS) for _ in range(4+randbelow(12))])
            print(Fore.CYAN + f">>> Repeat the code to confirm consent: {code}" + Style.RESET_ALL)
            if input(INPUT) == code:
                break

    def confirm_privacy_agreement(self):
        self._get_privacy_agreement()
        self._privacy_agreement_acceptation()

    def first_entry_menu(self):
        print(Fore.CYAN + ">>> Welcome to Trading Simulator!" + Style.RESET_ALL)
        while True:
            print(Fore.LIGHTWHITE_EX + "\n1. LogIn\n"
                                       "2. SignUp\n"
                                       "3. Quit" + Style.RESET_ALL)
            answer = input(INPUT)
            match answer.upper():
                case "1" | "LOGIN":
                    self.log_in()
                    break
                case "2" | "SIGNUP":
                    self.sign_up()
                    break
                case "3" | "QUIT":
                    break
                case _:
                    print(Fore.LIGHTRED_EX + ">>> Select one of the options shown above." + Style.RESET_ALL)

    def sign_up(self):
        self.confirm_privacy_agreement()
        ...
        print(Fore.LIGHTRED_EX + "\n>>> Congratulations! You can now leave the application and continue by logging in.")
        input(">>> Press ENTER to quit.\n")

    def log_in(self):
        ...

    def log_out(self):
        ...

    def delete_account(self):
        ...

    def change_account_info(self):
        ...

    def get_account_info(self):
        ...


# account = Account("Goga", "Pavlenko", "508980881", "pavlenkoegor1412@gmail.com")
# account.first_entry_menu()
