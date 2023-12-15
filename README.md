# TTK Bootstrap Repository (under construction)

Welcome to the TTK Bootstrap Repository! This repository is designed for students to learn and work with the ttkbootstrap library in Python. Below is an example file to get you started.

## Getting Started

To begin using this repository for your learning and development:

1. **Clone or Download the Repository**
   - Use Git to clone the repository or download it as a ZIP file to your local machine.

2. **Install Python**
   - If you don't have Python installed, download and install it from [python.org](https://www.python.org/).

3. **Install ttkbootstrap**
   - Open your terminal or command prompt and install the ttkbootstrap library using pip:
     ```bash
     pip install ttkbootstrap
     ```

4. **Run the Example Scripts**
   - Navigate to the directory where you cloned or downloaded the repository.
   - Run the example Python scripts to see ttkbootstrap in action.

5. **Explore and Experiment**
   - Modify the example scripts or create new ones to experiment with different ttkbootstrap features and widgets.

By following these steps, you'll be well on your way to creating impressive GUI applications using ttkbootstrap!


## Example Usage

Here's a basic example of how to use ttkbootstrap in a Python application:

```python
from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename="solar")
root.title("TTK Bootstrap")
root.geometry("500x500")

def doit():
    my_label.config(text=f"You typed: {my_entry.get()}")

my_frame = tb.Frame(root)
my_frame.pack(pady=40)

my_entry = tb.Entry(my_frame, font=("Helvetica", 18))
my_entry.pack(pady=20, padx=20)

my_button = tb.Button(my_frame, 
                      text="Submit", 
                      bootstyle="success",
                      command=doit)
my_button.pack(pady=20, padx=20)

my_label = tb.Label(root, text="Enter something", font=("Helvetica", 18))
my_label.pack(pady=20, padx=20)

root.mainloop()
```

## Course Reference

This repository is a practical extension of the knowledge provided in John Elder's course: "Python Tkinter GUI Design Using ttkbootstrap - Complete Course". This comprehensive course is an excellent resource for anyone looking to deepen their understanding of GUI development in Python using the ttkbootstrap library.

For more information about the course and to enroll, visit [Python Tkinter GUI Design Using ttkbootstrap - Complete Course](https://www.codemy.com/).