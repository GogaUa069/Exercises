from string import ascii_letters as letters, digits
import re
from colorama import Fore, Style
from secrets import choice, randbelow


class SystemPrompt:
    PATTERNS = {"full_name": re.compile(r"^[a-zA-Z-' ]{9}$"),
                "phone_number": re.compile(r"^\+\d{1,3} \d{9}$"),
                "email": re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")}

    def __init__(self):
        self.INPUT = self.communicate("<<< ", "LIGHTWHITE_EX")

    @staticmethod
    def communicate(text: str, color: str) -> str:
        return getattr(Fore, color) + text + Style.RESET_ALL

    def validator(self, value: str, pattern: str) -> bool:
        return self.PATTERNS[pattern].fullmatch(value) is not None


system = SystemPrompt()
