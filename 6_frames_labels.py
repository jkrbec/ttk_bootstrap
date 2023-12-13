from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename="solar")
#root = Tk()
root.title("TTK Bootstrap")
root.geometry("500x500")


def doit():
    my_label.config(text=f"You typed: {my_entry.get()}")

my_frame = tb.Frame(root, 
                    #bootstyle="danger"
                     )
my_frame.pack(pady=40)

my_entry = tb.Entry(my_frame, font=("Helvetica", 18),)
my_entry.pack(pady=20, padx=20)

my_button = tb.Button(my_frame, 
                      text="Submit", 
                      bootstyle="success",
                      command=doit)
my_button.pack(pady=20, padx=20)

my_label = tb.Label(root, text="Enter something", font=("Helvetica", 18),)
my_label.pack(pady=20, padx=20)

root.mainloop()