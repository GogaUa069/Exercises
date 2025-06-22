class CesarCipherClass:
    small_rus_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    big_rus_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    small_eng_alphabet = "abcdefghijklmnopqrstuvwxyz"
    big_eng_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "123456789"

    def __init__(self, direction, language, shift_step=0, string="", cipher_str=""):
        self.direction = direction
        self.language = language
        self.shift_step = shift_step
        self.string = string
        self.cipher_str = cipher_str

    def get_parameters(self):
        def get_direction():
            print("Please, select direction: coding/decoding")
            while True:
                try:
                    self.direction = input("-----> ")
                    if self.direction.lower() in ["coding", "decoding"]:
                        break
                except:
                    print("Please, select direction: coding/decoding")

        def get_language():
            print("Please, select language: eng/rus")
            while True:
                try:
                    self.language = input("-----> ")
                    if self.language.lower() in ["eng", "rus"]:
                        break
                except:
                    print("Please, select language: eng/rus")

        get_direction()
        get_language()

    def rus_coding(self):
        self.cipher_str = []
        print("Please, select shift step")
        while True:
            try:
                self.shift_step = int(input("-----> "))
                if self.shift_step not in range(1, 100):
                    print("Please, enter number in range 1-99")
                else:
                    break
            except ValueError:
                print("Please, enter NUMBER in range 1-99")

        print("Please, enter string")
        self.string = input("-----> ")

        for i in self.string:
            if i in CesarCipherClass.big_rus_alphabet:
                wrapper = (CesarCipherClass.big_rus_alphabet.find(i) + self.shift_step) % 32
                self.cipher_str.append(CesarCipherClass.big_rus_alphabet[wrapper])
            elif i in CesarCipherClass.small_rus_alphabet:
                wrapper = (CesarCipherClass.small_rus_alphabet.find(i) + self.shift_step) % 32
                self.cipher_str.append(CesarCipherClass.small_rus_alphabet[wrapper])
            elif i.isdigit() and int(i) in range(0, 9):
                wrapper = (CesarCipherClass.digits.find(i) + self.shift_step) % 10
                self.cipher_str.append(CesarCipherClass.digits[wrapper])
            else:
                self.cipher_str.append(i)

        print(''.join(self.cipher_str))

    def rus_decoding(self):
        self.cipher_str = []
        print("Please, select shift step")
        while True:
            try:
                self.shift_step = int(input("-----> "))
                if self.shift_step not in range(1, 100):
                    print("Please, enter number in range 1-99")
                else:
                    break
            except ValueError:
                print("Please, enter NUMBER in range 1-99")

        print("Please, enter string")
        self.string = input("-----> ")

        for i in self.string:
            if i in CesarCipherClass.big_rus_alphabet:
                wrapper = (CesarCipherClass.big_rus_alphabet.find(i) - self.shift_step) % 32
                self.cipher_str.append(CesarCipherClass.big_rus_alphabet[wrapper])
            elif i in CesarCipherClass.small_rus_alphabet:
                wrapper = (CesarCipherClass.small_rus_alphabet.find(i) - self.shift_step) % 32
                self.cipher_str.append(CesarCipherClass.small_rus_alphabet[wrapper])
            elif i.isdigit() and int(i) in range(0, 9):
                wrapper = (CesarCipherClass.digits.find(i) - self.shift_step) % 10
                self.cipher_str.append(CesarCipherClass.digits[wrapper])
            else:
                self.cipher_str.append(i)

        print(''.join(self.cipher_str))

    def eng_coding(self):
        self.cipher_str = []
        print("Please, select shift step")
        while True:
            try:
                self.shift_step = int(input("-----> "))
                if self.shift_step not in range(1, 100):
                    print("Please, enter number in range 1-99")
                else:
                    break
            except ValueError:
                print("Please, enter NUMBER in range 1-99")

        print("Please, enter string")
        self.string = input("-----> ")

        for i in self.string:
            if i in CesarCipherClass.big_eng_alphabet:
                wrapper = (CesarCipherClass.big_eng_alphabet.find(i) + self.shift_step) % 26
                self.cipher_str.append(CesarCipherClass.big_eng_alphabet[wrapper])
            elif i in CesarCipherClass.small_eng_alphabet:
                wrapper = (CesarCipherClass.small_eng_alphabet.find(i) + self.shift_step) % 26
                self.cipher_str.append(CesarCipherClass.small_eng_alphabet[wrapper])
            elif i.isdigit() and int(i) in range(0, 9):
                wrapper = (CesarCipherClass.digits.find(i) + self.shift_step) % 10
                self.cipher_str.append(CesarCipherClass.digits[wrapper])
            else:
                self.cipher_str.append(i)

        print(''.join(self.cipher_str))

    def eng_decoding(self):
        self.cipher_str = []
        print("Please, select shift step")
        while True:
            try:
                self.shift_step = int(input("-----> "))
                if self.shift_step not in range(1, 100):
                    print("Please, enter number in range 1-99")
                else:
                    break
            except ValueError:
                print("Please, enter NUMBER in range 1-99")

        print("Please, enter string")
        self.string = input("-----> ")

        for i in self.string:
            if i in CesarCipherClass.big_eng_alphabet:
                wrapper = (CesarCipherClass.big_eng_alphabet.find(i) - self.shift_step) % 26
                self.cipher_str.append(CesarCipherClass.big_eng_alphabet[wrapper])
            elif i in CesarCipherClass.small_eng_alphabet:
                wrapper = (CesarCipherClass.small_eng_alphabet.find(i) - self.shift_step) % 26
                self.cipher_str.append(CesarCipherClass.small_eng_alphabet[wrapper])
            elif i.isdigit() and int(i) in range(0, 9):
                wrapper = (CesarCipherClass.digits.find(i) - self.shift_step) % 10
                self.cipher_str.append(CesarCipherClass.digits[wrapper])
            else:
                self.cipher_str.append(i)

        print(''.join(self.cipher_str))


my_cipher = CesarCipherClass("", "", 0, "", "")


def cipher():
    my_cipher.get_parameters()
    if my_cipher.direction == "coding" and my_cipher.language == "rus":
        my_cipher.rus_coding()
    elif my_cipher.direction == "decoding" and my_cipher.language == "rus":
        my_cipher.rus_decoding()
    elif my_cipher.direction == "coding" and my_cipher.language == "eng":
        my_cipher.eng_coding()
    elif my_cipher.direction == "decoding" and my_cipher.language == "eng":
        my_cipher.eng_decoding()


cipher()
