from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename="solar")
#root = Tk()
root.title("TTK Bootstrap")
root.geometry("500x500")

def change(x):
    my_label.config(text=x)
    my_menu.config(bootstyle=x)

my_menu = tb.Menubutton(root, 
                        text="Menu",
                        bootstyle="success",
                        )
my_menu.pack(pady=20, padx=20)

#create a basic menu
inside_menu = tb.Menu(my_menu)

#add items to our menu
itemVar = StringVar()

for x in ['primary', 'secondary', 'success', 'info', 
          'warning', 'danger', 'light', 'dark']:
    inside_menu.add_radiobutton(label=x, 
                                variable=itemVar,
                                command=lambda x=x: change(x),)

#associate the inside menu with the button
my_menu['menu'] = inside_menu

#create a label
my_label = tb.Label(root, text="Enter something", font=("Helvetica", 18),)
my_label.pack(pady=20, padx=20)

root.mainloop()