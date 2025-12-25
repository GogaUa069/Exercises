from AppPrompt import system
from secrets import choice, randbelow


class App:
    @staticmethod
    def _get_privacy_policy():
        try:
            with open(system.PRIVACY_POLICY_FILE, "r", encoding=system.FILE_ENCODING) as file:
                for line in file:
                    print(system.communicate(line, "LIGHTWHITE_EX", False), end="")
                print()
        except FileNotFoundError:
            print(system.communicate(f"Privacy Policy file with path {system.PRIVACY_POLICY_FILE} not found!", "LIGHTRED_EX"))

    @staticmethod
    def _repeat_agreement_code():
        while True:
            agreement_code = "".join([choice(system.AGREEMENT_CODE_CHARS) for _ in range(4+randbelow(12))])
            print(system.communicate(f"Repeat the code to confirm you agree with privacy policy: {agreement_code}", "CYAN"))
            if input(system.INPUT) == agreement_code:
                break

    def privacy_policy_agreement(self):
        self._get_privacy_policy()
        self._repeat_agreement_code()

    def sign_up(self):
        self.privacy_policy_agreement()
        ...

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
