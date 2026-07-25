from secrets import token_bytes


class Encrypt:

    def __init__(self, data: str):
        self.__data = data
        self.__bitstring = None
        self.__key = None
        self.__cryptogram = None

    @property
    def key(self):
        return self.__key

    @property
    def cryptogram(self):
        return self.__cryptogram

    def set_bits(self):
        data_bytes = self.__data.encode("utf-8")
        self.__bitstring = ''.join(f"{b:08b}" for b in data_bytes)

    def set_key(self):
        key_bytes = token_bytes(len(self.__bitstring) // 8)
        self.__key = ''.join(f"{b:08b}" for b in key_bytes)

    def encrypt(self):
        self.__cryptogram = list()

        for i, j in zip(self.__bitstring, self.__key):
            bit = 0 if i == j else 1
            self.__cryptogram.append(str(bit))

        self.__cryptogram = "".join(self.__cryptogram)

    def __call__(self):
        self.set_bits()
        self.set_key()
        self.encrypt()

    def __repr__(self):
        return (f"\n__REPR__ ENCRYPTING:\n\n"
                f"- data:       {self.__data}\n"
                f"- bitstring:  {self.__bitstring}\n"
                f"- key:        {self.__key}\n"
                f"- cryptogram: {self.__cryptogram}\n")

    def __str__(self):
        return (f"\nENCRYPTING:\n\n"
                f"data:       {self.__data}\n"
                f"key:        {self.__key}\n"
                f"cryptogram: {self.__cryptogram}\n")


class Decrypt:

    def __init__(self, cryptogram: str, key: str):
        self.__cryptogram = cryptogram
        self.__key = key
        self.__data = None
        self.__bitstring = None

    @property
    def data(self):
        return self.__data

    def set_bits(self):
        self.__bitstring = list()

        for i, j in zip(self.__cryptogram, self.__key):
            bit = 0 if i == j else 1
            self.__bitstring.append(str(bit))

        self.__bitstring = "".join(self.__bitstring)

    def decrypt(self):
        bytes_list = [self.__bitstring[i:i + 8] for i in range(0, len(self.__bitstring), 8)]
        data = bytes(int(b, 2) for b in bytes_list)
        self.__data = data.decode("utf-8")

    def __call__(self):
        self.set_bits()
        self.decrypt()

    def __repr__(self):
        return (f"\n__REPR__ DECRYPTING:\n\n"
                f"- cryptogram: {self.__cryptogram}\n"
                f"- key:        {self.__key}\n"
                f"- bitstring:  {self.__bitstring}\n"
                f"- data:       {self.__data}\n")

    def __str__(self):
        return (f"\nDECRYPTING:\n\n"
                f"cryptogram: {self.__cryptogram}\n"
                f"key:        {self.__key}\n"
                f"data:       {self.__data}\n")


encrypting = Encrypt(data="Hello World!")

encrypting()
print(encrypting)

decrypting = Decrypt(cryptogram=encrypting.cryptogram, key=encrypting.key)

decrypting()
print(decrypting)
