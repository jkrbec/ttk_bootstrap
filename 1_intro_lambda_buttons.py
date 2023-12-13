from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename="solar")
#root = Tk()
root.title("TTK Bootstrap")
root.geometry("500x360")

counter = 0
def changer():
    global counter
    counter += 1
    if counter % 2 == 0:
        my_label.config(text="Hello World")
    else:
        my_label.config(text="Goodbye World")


# Create a label
my_label = tb.Label(root, text="Hello World", font=("Helvetica", 24), 
                    bootstyle="default")

my_label.pack(pady=50)

# Create a button
my_button = tb.Button(root, text="Click Me!", 
                      command=changer,
                      bootstyle="success, outline")
my_button.pack(pady=20)

# Create a lambda button
lambda_button = tb.Button(root, text="Lambda",
                          command=lambda: my_label.config(text="Lambda"),
                          bootstyle="danger")
lambda_button.pack(pady=20)





root.mainloop()