from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

Window.resizable = False
Window.maximize()

class MyApp(App):
    title = "Predict the Shot 2D"

    def build(self):
        return Label(text="Okno pełnoekranowe, ale bez skalowania!")

MyApp().run()
