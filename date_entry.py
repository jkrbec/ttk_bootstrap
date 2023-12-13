from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from datetime import date
from ttkbootstrap.dialogs import Querybox

root = tb.Window(themename="solar")
#root = Tk()
root.title("TTK Bootstrap")
root.geometry("500x500")

def datey():
    my_label.config(text=f"Date: {my_date.entry.get()}")

def thing():
    cal = Querybox()
    my_label.config(text=f"Date: {cal.get_date()}")

my_date = tb.DateEntry(
    root,
    bootstyle="success",
   # startdate=date()
   firstweekday=6,
)
my_date.pack(pady=50, fill= X, padx=20)


my_button = tb.Button(
    root,
    text="Get Date",
    bootstyle="danger outline",
    command=datey
)
my_button2 = tb.Button(
    root,
    text="Get Calendar",
    bootstyle="success outline",
    command=thing
)
my_button.pack()
my_button2.pack()

my_label = tb.Label(
    root,
    text="Date: ",
)
my_label.pack(pady=20)


root.mainloop()