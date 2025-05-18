import tkinter as tk
from tkinter import messagebox
import math

def add():
    try:
        result.set(float(entry1.get()) + float(entry2.get()))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

def subtract():
    try:
        result.set(float(entry1.get()) - float(entry2.get()))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

def multiply():
    try:
        result.set(float(entry1.get()) * float(entry2.get()))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

def divide():
    try:
        if float(entry2.get()) == 0:
            raise ZeroDivisionError
        result.set(float(entry1.get()) / float(entry2.get()))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero")

def square():
    try:
        num = float(entry1.get())
        result.set(num ** 2)
    except ValueError:
        messagebox.showerror("Invalid input", "Enter a number in the first field only")

def square_root():
    try:
        num = float(entry1.get())
        if num < 0:
            raise ValueError
        result.set(math.sqrt(num))
    except ValueError:
        messagebox.showerror("Invalid input", "Enter a non-negative number in the first field")

# GUI Window
root = tk.Tk()
root.title("Simple Calculator")

tk.Label(root, text="Number 1:").grid(row=0, column=0)
tk.Label(root, text="Number 2:").grid(row=1, column=0)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

# Operation buttons
tk.Button(root, text="Add", command=add).grid(row=2, column=0)
tk.Button(root, text="Subtract", command=subtract).grid(row=2, column=1)
tk.Button(root, text="Multiply", command=multiply).grid(row=3, column=0)
tk.Button(root, text="Divide", command=divide).grid(row=3, column=1)
tk.Button(root, text="Square", command=square).grid(row=4, column=0)
tk.Button(root, text="Square Root", command=square_root).grid(row=4, column=1)

result = tk.StringVar()
tk.Label(root, text="Result:").grid(row=5, column=0)
tk.Entry(root, textvariable=result, state='readonly').grid(row=5, column=1)

root.mainloop()
