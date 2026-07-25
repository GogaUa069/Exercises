import pygame
import tkinter as tk

pygame.init()

class Audio:
    SOUNDTRACK = r"Audio/DoYouLoveMeSoundtrack.wav"
    QUESTION1_PART = (1.0, 8000)
    QUESTION2_PART = (8.0, 7000)
    BAD_ENDING = (15.0, 3000)

    def __call__(self, root, start, duration):
        pygame.mixer.music.load(self.SOUNDTRACK)
        pygame.mixer.music.play(start=start)
        root.after(duration, pygame.mixer.music.stop)


audio = Audio()


class SystemPrompt:
    IMAGES = {"GOGA": r"Photos/GOGA1.png",
              "CUTE_GOGA": ...,
              "ANGRY_GOGA": r"Photos/ANGRY_GOGA1.png",
              "BAD_BOY_GOGA": ...,
              "HAPPY_GOGA": ...}

    @staticmethod
    def hello():
        print("Hello World!")


system = SystemPrompt()


class Screen:
    WIDTH, HEIGHT = 800, 600
    TITLE = "Do You love me?!"
    FILL = "black"

    def __init__(self, root, image):
        self.IMAGE = image
        self.ROOT = root

        self.set_root()
        self.load_image()

    def set_root(self):
        self.ROOT.title(self.TITLE)
        self.ROOT.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.ROOT.configure(bg=self.FILL)

    def load_image(self):
        label = tk.Label(self.ROOT, image=self.IMAGE)
        label.image = self.IMAGE
        label.place(relx=0, rely=1, anchor="sw")
        label.lower()

    def __call__(self, *args, **kwargs):
        self.ROOT.after(100, lambda: audio(self.ROOT, *audio.QUESTION1_PART))
        self.ROOT.mainloop()


screen1_root = tk.Tk()
screen1 = Screen(screen1_root, system.IMAGES["GOGA"])

question1 = tk.Label(screen1.ROOT, text="Do You love me?!", font=("Arial", 24), fg="red", bg="black")
question1.place(relx=0.5, rely=0.4, anchor="center")

yes_button = tk.Button(screen1.ROOT, text="YES", font=("Arial", 14), width=10, command=system.hello)
yes_button.place(relx=0.4, rely=0.6, anchor="e")

no_button = tk.Button(screen1.ROOT, text="NO", font=("Arial", 14), width=10, command=system.hello)
no_button.place(relx=0.6, rely=0.6, anchor="w")

screen1()
