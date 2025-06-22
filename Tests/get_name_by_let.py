from time import sleep


class StringValidator:
    def __init__(self, string):
        self.__string = string

    @property
    def string(self):
        return f"Hello! My name is {self.__string.lower().capitalize()}.\n"

    @string.setter
    def string(self, value):
        self.__string = value

    def get_string_by_letters(self):
        for let in self.__string:
            sleep(0.21)
            print(let, end="")


validator_1 = StringValidator("Goga")
print(validator_1.string)
