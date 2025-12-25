from SystemConfig import system
import uuid
from secrets import choice, randbelow
import yaml


class PrivacyPolicyAgreement:
    __ex_counter = 1

    def __new__(cls, *args, **kwargs):
        if cls.__ex_counter == 1:
            cls.__ex_counter += 1
            return super().__new__(cls)
        return None

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

    @classmethod
    def privacy_policy_agreement(cls):
        cls._get_privacy_policy()
        cls._repeat_agreement_code()


privacy_policy_agreement = PrivacyPolicyAgreement()


class App:
    __ex_counter = 1

    def __new__(cls, *args, **kwargs):
        if cls.__ex_counter == 1:
            cls.__ex_counter += 1
            return super().__new__(cls)
        return None

    @staticmethod
    def _upload_account_data(data: dict):
        account_id = str(uuid.uuid4())[:8]
        account_file = f"User_{account_id}"
        with open(f"{system.ACCOUNT_DIRECTORY_PATH}{account_file}.yaml", "w", encoding=system.FILE_ENCODING) as file:
            yaml.dump(data, file, default_flow_style=False)

    # @staticmethod
    # def _set_user_field(field_name: str, pattern: str) -> str:
    #     while True:
    #         value = input(system.INPUT)
    #         if system.validator(value, pattern):
    #             return value
    #         print(system.communicate(f"Invalid {field_name}, try again!", "LIGHTRED_EX"))

    # def _register_account(self):
    #     fields = {
    #         "name": "full_name",
    #         "last_name": "full_name",
    #         "email": "email"
    #     }
    #     return {field: self._set_user_field(field, pattern) for field, pattern in fields.items()}

    # def sign_up(self):
    #     privacy_policy_agreement.privacy_policy_agreement()
    #     account_data = self._register_account()
    #     self._upload_account_data(account_data)
    #     print(system.communicate("Congratulations! You have just created your own account!", "LIGHTRED_EX"))

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


app = App()
app.welcome()
