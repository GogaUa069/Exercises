from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button

Window.maximize()

# vvv SOUNDS vvv

click_sound = SoundLoader.load("audio/click.mp3")

_old_on_press = Button.on_press


def _new_on_press(self):
    if click_sound:
        click_sound.play()
    _old_on_press(self)


Button.on_press = _new_on_press

# ^^^ SOUNDS ^^^


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

    def build(self):
        self.music = SoundLoader.load("audio/soundtrack1.wav")
        if self.music:
            self.music.loop = True
            self.music.volume = 0.5
            self.music.play()

        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(MainMenu(name="main_menu"))
        sm.add_widget(Credits(name="credits"))
        sm.add_widget(Settings(name="settings"))
        return sm


if __name__ == "__main__":
    MyApp().run()
