import sys, os


def resource_path(path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, path)
    return path


from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button

Window.maximize()


class ClickButton(Button):
    def on_press(self):
        app = App.get_running_app()
        if app.click_sound:
            app.click_sound.play()
        return super().on_press()


class MainMenu(Screen):

    @staticmethod
    def play():
        pass

    @staticmethod
    def settings():
        app = App.get_running_app()
        app.root.transition.direction = "left"
        app.root.current = "settings"

    @staticmethod
    def credits():
        app = App.get_running_app()
        app.root.transition.direction = "down"
        app.root.current = "credits"

    @staticmethod
    def quit():
        App.get_running_app().stop()


class Settings(Screen):

    @staticmethod
    def tutorial():
        pass

    @staticmethod
    def audio():
        pass

    @staticmethod
    def from_settings_to_mm():
        app = App.get_running_app()
        app.root.transition.direction = "right"
        app.root.current = "main_menu"


class Credits(Screen):

    @staticmethod
    def from_credits_to_mm():
        app = App.get_running_app()
        app.root.transition.direction = "up"
        app.root.current = "main_menu"


class MyApp(App):
    title = "Predict the Shot 2D"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.assets_images = resource_path("../UTILS/IMAGES/")

    def build(self):
        self.click_sound = SoundLoader.load(resource_path("../UTILS/AUDIO/SOUNDS/click.mp3"))
        self.music = SoundLoader.load(resource_path("../UTILS/AUDIO/SOUNDTRACKS/background_soundtrack_main.wav"))

        if self.music:
            self.music.loop = True
            self.music.volume = 0.5
            self.music.play()

        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(MainMenu(name="main_menu"))
        sm.add_widget(Credits(name="credits"))
        sm.add_widget(Settings(name="settings"))
        return sm

    def play_click(self):
        if self.click_sound:
            self.click_sound.play()


if __name__ == "__main__":
    MyApp().run()
