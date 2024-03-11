# Import the necessary libraries
from PIL import Image,ImageTk
import tkinter as tk

# function to add the background image
def set_background(root, image_file_path):
    img = Image.open(image_file_path)

    # Resize the image
    img = img.resize((650, 450), Image.LANCZOS)

    photo = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=photo)
    label.image = photo  # To prevent garbage collection
    label.place(x=0, y=0, relwidth=1, relheight=1)

# Function to clear all widgets
def clear_widgets(root):
    for i in root.winfo_children():
        i.destroy()

