"""Greeter App Class"""
import tkinter as tk
from tkinter import messagebox

class GreeterApp(tk.Tk):
    def __init__(self):
        """call the superclass constructor FIRST"""
        super().__init__()
        self.title("Greeter")
        """Create components in a seperate method"""
        self.init_components()

    def init_components(self):
        """Define components and layout"""
        self.name = tk.StringVar()
        label = tk.Label(self, text="Your name?")
        namefield = tk.Entry(self, width=20, textvariable=self.name)
        greet_button = tk.Button(self, text="Greet me", command=self.greet_handler)

        Layout = 'grid'

        padding = {'padx': 5, 'pady': 5}

        """cannot use at the same time as pack"""
        if Layout == 'grid':
            label.grid(row=0, column=0, **padding)
            namefield.grid(row=0, column=1, **padding)
            greet_button.grid(row=0, column=2)

            self.columnconfigure(1, weight=1)
            namefield.grid(sticky=tk.EW)  # EW = east-west sides

        namefield.bind('<Return>', self.greet_handler)
        namefield['foreground'] = 'blue'
        namefield['font'] = ('Monospace', 16)

        options = {'font': ('Arial', 14)}
        label.configure(**options)
        greet_button.configure(**options)

        """cannot use at the same time as grid"""
        if Layout == 'pack':
            label.pack(side=tk.LEFT, **padding)
            namefield.pack(side=tk.LEFT, **padding, expand=True, fill=tk.X)
            greet_button.pack(side=tk.RIGHT, **padding)

        self.mainloop()

    def greet_handler(self, *args):
        try:
            message = f"Hello, {self.name.get().strip()}"
            if self.name.get().strip() != "":
                messagebox.showinfo("Greetings", message)
                """clear text from the input field"""
                self.name.set("")
        except ValueError:
            pass