#import necessary libraries
import tkinter as tk
from src.initial_setup import initial_setup

#Initialize GUI Window
root = tk.Tk()
initial_setup(root)

root.title("Queer Security International")
root.geometry("650x450")

root.mainloop()