from kivy.app import App
from kivy.uix.boxlayout import BoxLayout



class MainWidget(BoxLayout):

    @staticmethod
    def play_btn():
        print("Clicked!")


class MyApp(App):

    @staticmethod
    def build():
        return MainWidget()


if __name__ == "__main__":
    MyApp().run()
