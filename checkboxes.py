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



root.mainloop()