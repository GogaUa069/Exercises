# v6.0 alpha

from system import *


class DataSaverTXT:
    PATH = "../UTILS/data"
    ENCODING = "utf-8"

    @staticmethod
    def resource_path(relative_path):
        base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def save_data(self, data):
        with open(self.PATH, "w", encoding=self.ENCODING) as file:
            file.writelines([str(val)+"\n" for val in data.values()])

    def get_data(self):
        with open(self.PATH, "r", encoding=self.ENCODING) as file:
            return {key: value for key, value in zip(("win_streak", "good_endings", "bad_endings"), [int(i) for i in file.readlines()])}


data_saver_txt = DataSaverTXT()
