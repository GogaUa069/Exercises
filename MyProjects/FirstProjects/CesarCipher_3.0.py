from string import ascii_letters as letters, digits


class CesarCipher:
    def __init__(self, data, direction, step):
        self.data = data
        self.direction = direction
        self.step = step

    def coding(self):
        encrypted_data = list()

        for char in self.data:
            match char:
                case _ if char in letters:
                    indx = (letters.find(char) + self.step) % 26
                    encrypted_data.append(letters[indx])
                case _ if char in digits:
                    indx = (digits.find(char) + self.step) % 10
                    encrypted_data.append(digits[indx])
                case _:
                    encrypted_data.append(char)

        print("".join(encrypted_data))

    def decoding(self):
        decrypted_data = list()

        for char in self.data:
            match char:
                case _ if char in letters:
                    indx = (letters.find(char) - self.step) % 26
                    decrypted_data.append(letters[indx])
                case _ if char in digits:
                    indx = (digits.find(char) - self.step) % 10
                    decrypted_data.append(digits[indx])
                case _:
                    decrypted_data.append(char)

        print("".join(decrypted_data))

    def __call__(self):
        match self.direction:
            case "coding":
                self.coding()
            case "decoding":
                self.decoding()


cesar_cipher = CesarCipher("Hello World!", "coding", 15)
cesar_cipher()
