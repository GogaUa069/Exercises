import hashlib


class PasswordValidator:
    def __init__(self):
        self.password = None

    @staticmethod
    def hash_text(text):
        return hashlib.sha256(text.encode()).hexdigest()

    def set_password(self, text):
        self.password = self.hash_text(text)

    def validate_password(self):
        while True:
            answer = input("\n>>> Enter password: ")
            if self.hash_text(answer) == self.password:
                print("You have logged in!")
                break
            else:
                print("You have not authorized!")


password_validator = PasswordValidator()
password_validator.set_password("GogaUa096")
password_validator.validate_password()
