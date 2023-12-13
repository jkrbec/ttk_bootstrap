from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
#root = Tk()
root.title("TTK Bootstrap")
root.geometry("500x360")


# tvorba entry funkce
def speak():
    my_label.config(text=f'You typed: {my_entry.get()}')

# tvorba entry widgetu
my_entry = tb.Entry(root, width=50, font=("Helvetica", 24), bootstyle="success")
my_entry.pack(pady=50)


# tvorba tlačítka
my_button = tb.Button(
    root,
    bootstyle="success",
    text="Submit",
    command=speak
)
my_button.pack(pady=50)

# tvorba labelu
my_label = tb.Label(root, text="")
my_label.pack(pady=20)

root.mainloop()
