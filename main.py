from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

import random


# Color changing function
def change_color():
    color = random_color()
    root.config(bg=color)
    label.config(text=f"Background Color: {color}")


# Generate random colot
def random_color():
    r = lambda: random.randint(0, 255)
    return "#%02X%02X%02X" % (r(), r(), r())


# Copy to clipboard
def copy_to_clipboard():
    color = root.cget("bg")
    root.clipboard_clear()
    root.clipboard_append(color)


# main window
root = ThemedTk(theme="yaru")
root.config(bg="white")
root.geometry("700x500")
root.title("Color Flipper")

# color variable
color_var = StringVar()

# config button
btn = ttk.Button(root, text="Change Color", command=change_color)

# label
label = Label(root, text="Background Color: ", bg="white", foreground="black")
label.pack()

# Copy button
copy_button = ttk.Button(root, text="Copy", command=copy_to_clipboard)
copy_button.pack(pady=5)

# Widget placement
label.place(relx=0.5, rely=0.5, anchor=CENTER)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)
copy_button.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()
