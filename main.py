import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Greeter")

""" console output """
# def greet_handler(*args):
#     name = namefield.get()
#     message = f"Hello, {name}"
#     print(message)
#     """clear text from the input field"""
#     namefield.delete(0,tk.END)

"""pop-up output -> notice messagebox in place of print(message)"""
# def greet_handler(*args):
#     name = namefield.get()
#     message = f"Hello, {name}"
#     messagebox.showinfo("Greetings",message)
#     """clear text from the input field"""
#     namefield.delete(0,tk.END)

"""Use stringVar in Event Handler"""
name = tk.StringVar()
namefield = tk.Entry(root, width=20, textvariable=name)

def greet_handler(*args):
    try:
        message = f"Hello, {name.get()}"
        if name.get() != "":
            messagebox.showinfo("Greetings", message)
            """clear text from the input field"""
            name.set("")
    except ValueError:
        pass

label = tk.Label(root, text="Your name?")
namefield = tk.Entry(root, width=20)
greet_button = tk.Button(root, text="Greet me",command=greet_handler)

padding = {'padx': 5, 'pady': 5}

"""cannot use at the same time as pack"""
label.grid(row=0, column=0,**padding)
namefield.grid(row=0, column=1, **padding)
greet_button.grid(row=0, column=2)

namefield.bind('<Return>', greet_handler)
namefield['foreground'] = 'blue'
namefield['font'] = ('Monospace', 16)

options = {'font': ('Arial', 14)}
label.configure(**options)
greet_button.configure(**options)

"""cannot use at the same time as grid"""
# label.pack(side=tk.LEFT,**padding)
# namefield.pack(side=tk.LEFT, **padding, expand=True, fill=tk.X)
# greet_button.pack(side=tk.RIGHT, **padding)

root.columnconfigure(1,weight=1)
namefield.grid(sticky=tk.EW) #EW = east-west sides

root.mainloop()
