import os
import sys
import yaml

BASE_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))
data_path = os.path.join(BASE_DIR, "UTILS", "data_exp.yaml")
encoding = "utf-8"


class Human:
    def __init__(self):
        self.name = self.last_name = self.age = None
        self.data = dict().fromkeys(("name", "last_name", "age"), 0)
        #self.set_save_data()

    def set_save_data(self):
        self.data["name"] = self.name
        self.data["last_name"] = self.last_name
        self.data["age"] = self.age

    def set_load_data(self):
        self.name = self.data["name"]
        self.last_name = self.data["last_name"]
        self.age = self.data["age"]

    def load_data(self):
        with open(data_path, "r", encoding=encoding) as file:
            self.data = yaml.safe_load(file)
        self.set_load_data()

    def save_data(self):
        self.set_save_data()
        with open(data_path, "w", encoding=encoding) as file:
            yaml.safe_dump(self.data, file, sort_keys=False)

    def __str__(self):
        return (f"\n*** INFO ***\n"
                f"- NAME: {self.name}\n"
                f"- LAST NAME: {self.last_name}\n"
                f"- AGE: {self.age}")

    def __call__(self):
        print("\n"
              "2. Load\n"
              "3. Info\n"
              "4. New")

        match input("<<< ").lower():
            case "2" | "load":
                print("Loading data...")
                self.load_data()
                print("Data successfully loaded!")
                print(self)
            case "3" | "info":
                print(self)
            case "4" | "new":
                print()
                self.name = input("name: ")
                self.last_name = input("last_name: ")
                self.age = int(input("age: "))
                print("\nSaving data...")
                self.save_data()
                print("Data successfully saved!\n")

human1 = Human()
human1()
