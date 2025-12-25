import re
from string import ascii_letters as letters, digits
from colorama import Fore, Style


class SystemConfig:
    __ex_counter = 1

    AGREEMENT_CODE_CHARS = letters + digits
    ACCOUNT_DIRECTORY_PATH = "TradingSimulator/Accounts/"
    PRIVACY_POLICY_FILE = "../Utils/PrivacyPolicy"
    FILE_ENCODING = "utf-8"
    PATTERNS = {"full_name": re.compile(r"^[a-zA-Z-' ]{9}$"),
                "email": re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")}

    def __new__(cls, *args, **kwargs):
        if cls.__ex_counter == 1:
            cls.__ex_counter += 1
            return super().__new__(cls)
        return None

    def __init__(self):
        self.INPUT = self.communicate("<<< ", "LIGHTWHITE_EX")

    @staticmethod
    def communicate(text: str, color: str, is_system: bool=True) -> str:
        text = f">>> {text}" if is_system else text
        return getattr(Fore, color) + text + Style.RESET_ALL

    def validator(self, value: str, pattern: str) -> bool:
        return self.PATTERNS[pattern].fullmatch(value) is not None


system = SystemConfig()
