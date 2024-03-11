# Importing the necessary libraries and functions from other files
import tkinter as tk
from src.initial_setup import initial_setup

# Creating the root window
root = tk.Tk()
root.title("Queer Security International")
root.geometry("650x450")

initial_setup(root)

root.mainloop()
