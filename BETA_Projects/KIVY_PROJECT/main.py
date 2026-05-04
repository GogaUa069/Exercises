from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.core.window import Window

Window.maximize()


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

    @staticmethod
    def build():
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(MainMenu(name="main_menu"))
        sm.add_widget(Credits(name="credits"))
        sm.add_widget(Settings(name="settings"))
        return sm


if __name__ == "__main__":
    MyApp().run()
