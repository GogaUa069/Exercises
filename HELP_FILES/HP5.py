import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("600x800")

img = Image.open("button.png")
img = img.resize((100, 100), Image.LANCZOS)
img_tk = ImageTk.PhotoImage(img)

# Przycisk dokładnie 200x100
button = tk.Button(
    root,
    image=img_tk,
    bd=0,
    highlightthickness=0,
    padx=0,
    pady=0,
    relief="flat"
)

# Wyśrodkowanie
button.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
