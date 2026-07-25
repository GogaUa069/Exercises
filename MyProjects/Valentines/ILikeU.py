import tkinter as tk
from random import randint

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

def move_no_button(event):
    new_x = randint(0, WINDOW_WIDTH - 100)
    new_y = randint(200, WINDOW_HEIGHT - 50)
    no_button.place(x=new_x, y=new_y)

def yes_clicked():
    result_label.config(text="I'm so happy!\nThanks for acceptation", fg="light pink")

root = tk.Tk()
root.title("Love confession")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.configure(bg="black")

title = tk.Label(root, text="Question of the life", font=("Arial", 24), fg="red", bg="black")
title.pack(pady=30)

question = tk.Label(root, text="I like you. Do you like me?", font=("Arial", 18), fg="white", bg="black")
question.pack(pady=10)

yes_button = tk.Button(root, text="YES", font=("Arial", 14), width=10, command=yes_clicked)
yes_button.place(x=200, y=400)

no_button = tk.Button(root, text="NO", font=("Arial", 14), width=10)
no_button.place(x=500, y=400)

no_button.bind("<Enter>", move_no_button)

result_label = tk.Label(root, text="", font=("Arial", 16), fg="white", bg="black")
result_label.pack(pady=20)

root.mainloop()
