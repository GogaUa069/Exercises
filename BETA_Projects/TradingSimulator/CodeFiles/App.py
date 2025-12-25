from SystemConfig import system
from secrets import choice, randbelow
import yaml


class App:
    @staticmethod
    def _get_privacy_policy():
        try:
            with open(system.PRIVACY_POLICY_FILE, "r", encoding=system.FILE_ENCODING) as file:
                for line in file:
                    print(system.communicate(line, "LIGHTWHITE_EX", False), end="")
                print()
        except FileNotFoundError:
            print(system.communicate(f"Privacy Policy file with path {system.PRIVACY_POLICY_FILE} not found!",
                                     "LIGHTRED_EX"))

    @staticmethod
    def _repeat_agreement_code():
        while True:
            agreement_code = "".join([choice(system.AGREEMENT_CODE_CHARS) for _ in range(4 + randbelow(12))])
            print(system.communicate(f"Repeat the code to confirm you agree with privacy policy: {agreement_code}",
                                     "CYAN"))
            if input(system.INPUT) == agreement_code:
                break

    def _privacy_policy_agreement(self):
        self._get_privacy_policy()
        self._repeat_agreement_code()

    @staticmethod
    def _upload_account_data(data: dict):
        account_id = str(randbelow(10000))
        account_file = "User" + account_id.rjust(5, "0")
        with open(f"{system.ACCOUNT_DIRECTORY_PATH}{account_file}", "w", encoding=system.FILE_ENCODING) as file:
            yaml.dump(data, file, default_flow_style=False)

    @staticmethod
    def _set_user_field(field_name: str, pattern: str) -> str:
        while True:
            value = input(system.INPUT)
            if system.validator(value, pattern):
                return value
            print(system.communicate(f"Invalid {field_name}, try again!", "LIGHTRED_EX"))

    def _register_account(self):
        fields = {
            "name": "full_name",
            "last_name": "full_name",
            "email": "email"
        }
        return {field: self._set_user_field(field, pattern) for field, pattern in fields.items()}

    def sign_up(self):
        self._privacy_policy_agreement()
        account_data = self._register_account()
        self._upload_account_data(account_data)

    def sign_in(self):
        ...

    def welcome(self):
        print(system.communicate("Welcome to Trading Simulator!\n", "CYAN"))
        while True:
            print(system.communicate("1. Sign In\n"
                                     "2. Sign Up\n"
                                     "3. Quit", "LIGHTWHITE_EX", False))
            match input(system.INPUT).upper():
                case "1" | "SIGNIN" | "SIGN IN":
                    self.sign_in()
                case "2" | "SIGNUP" | "SIGN UP":
                    self.sign_up()
                case "3" | "QUIT":
                    break
                case _:
                    print(system.communicate("Please, select one of the options shown above!", "LIGHTRED_EX"))
