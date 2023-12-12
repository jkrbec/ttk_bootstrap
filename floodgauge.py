from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
#root = Tk()
root.title("TTK Bootstrap")
root.geometry("500x500")


def starter():
    my_gauge.start()

def stopper():
    my_gauge.stop()

def incrementer():
    my_gauge.step(10)
    my_label.config(text=f'Position: {my_gauge.variable.get()}%')

my_gauge = tb.Floodgauge(
    root,
    bootstyle="success",
    font=("Helvetica", 18),
    mask="Pos: {}%",
    maximum=80,
    orient="horizontal",
    value=10,
    mode="indeterminate", # or "determinate"
)

my_gauge.pack(pady=50, fill= X, padx=20)

start_button = tb.Button(
    root,
    text="Start",
    bootstyle="danger outline",
    command=starter
)

start_button.pack(pady=20)

stop_button = tb.Button(
    root,
    text="Stop",
    bootstyle="danger outline",
    command=stopper
)
stop_button.pack(pady=20)


inc_button = tb.Button(
    root,
    text="Increment",
    bootstyle="danger outline",
    command=incrementer
)

inc_button.pack(pady=20)

my_label = Label(root,
    text="Position: ",)

my_label.pack(pady=20)


root.mainloop()