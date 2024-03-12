from PIL import Image,ImageTk
import tkinter as tk


def set_background(root, file_path):

    img = Image.open(file_path)

    # Resize the image
    img = img.resize((650, 450), Image.LANCZOS)

    photo = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=photo)
    label.image = photo  # To prevent garbage collection
    label.place(x=0, y=0, relwidth=1, relheight=1)

    # Set the height and width as separate parameters to give you more flexibility
    screen_width = 600
    screen_height = 400

    # Use the minsize function
    root.minsize(screen_width, screen_height)


def clear_widgets(root):
    for i in root.winfo_children():
        i.destroy()