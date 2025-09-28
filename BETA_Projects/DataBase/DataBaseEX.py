class DataManager:
    ENCODING = "utf-8"

    def __init__(self):
        self.data = self.path = str()

    def set_path(self):
        print("\n>>> Enter file name:")
        self.path = input("<<< ")

    def set_data(self):
        print("\n>>> Enter data:")
        self.data = input("<<< ")

    def clear_file(self):
        with open(f"Datas/{self.path}", "w", encoding=self.ENCODING):
            pass

    def move_data_to_file(self):
        with open(f"Datas/{self.path}", "w", encoding=self.ENCODING) as file:
            file.write(self.data)

    def get_data_from_file(self):
        with open(f"Datas/{self.path}", "r", encoding=self.ENCODING) as file:
            print("\n>>> Data:")
            for line in file.readlines():
                print(line, end="")
            print()

    def __call__(self, *args, **kwargs):
        self.set_path()
        self.clear_file()
        self.set_data()
        self.move_data_to_file()
        self.get_data_from_file()


data_manager = DataManager()
data_manager()
