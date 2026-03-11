from System import system, os, shutil, yaml


class WinStreakController:
    ENCODING = "utf-8"
    RESOURCE_NAME = SAVE_NAME = "Utils/WIN_STREAK_FILE"

    def __init__(self):
        self.SAVE_PATH = os.path.join(os.getcwd(), self.SAVE_NAME)
        self.__ensure_writable_copy()

    def __ensure_writable_copy(self):
        if not os.path.exists(self.SAVE_PATH):
            try:
                shutil.copyfile(system.resource_path(self.RESOURCE_NAME), self.SAVE_PATH)
            except Exception:
                with open(self.SAVE_PATH, "w", encoding=self.ENCODING) as file:
                    file.write("0")

    def get_win_streak(self, is_communicate=False):
        with open(self.SAVE_PATH, "r", encoding=self.ENCODING) as file:
            win_streak = file.read()
            match is_communicate:
                case True:
                    return win_streak
                case _:
                    return f"Your win streak: {win_streak}"

    def __call__(self, is_defeat=False):

        new_streak = 0 if is_defeat else int(self.get_win_streak()) + 1
        with open(self.SAVE_PATH, "w", encoding=self.ENCODING) as file:
            yaml.dump(data, file, sort_keys=False)


win_streak_controller = WinStreakController()
