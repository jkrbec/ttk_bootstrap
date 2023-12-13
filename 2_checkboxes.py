from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
###
root = tb.Window(themename="superhero")
#root = Tk()
root.title("TTK Bootstrap")
root.geometry("500x360")

def checker():
    print(var1.get())

my_label = tb.Label(root, text="Click the checkboxes", font=("Helvetica", 24),
    bootstyle="default")
my_label.pack(pady=(40, 10))

# checkbutton
var1 = IntVar()
my_check = tb.Checkbutton(root, text="Check me out!", 
                          variable=var1,
                       onvalue=1, 
                          offvalue=0,
                          bootstyle="success",
                          command = checker)

my_check.pack(pady=10)


# toolbutton
var2 = IntVar()
my_check2 = tb.Checkbutton(
                           text="Tool button!",
                           bootstyle="danger, toolbutton",
                           variable=var2,
                           onvalue=1,
                           offvalue=0,
                           command=lambda: print(var2.get()))
my_check2.pack(pady=10)

# round toggle
var3 = IntVar()
my_check3 = tb.Checkbutton(
                           text="Round toggle!",
                           bootstyle="success, roundtoggle",
                           variable=var3,
                           onvalue=1,
                           offvalue=0,
                           command=lambda: print(var3.get()))
my_check3.pack(pady=10)

# square toggle button
var4 = IntVar()
my_check4 = tb.Checkbutton(
                           text="Square toggle!",
                           bootstyle="warning, squaretoggle",
                           variable=var4,
                           onvalue=1,
                           offvalue=0,
                           command=lambda: print(var4.get()))
my_check4.pack(pady=10)





root.mainloop()