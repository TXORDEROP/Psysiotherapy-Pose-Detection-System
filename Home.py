import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
from subprocess import run # Added this import

# Global variable
fn = ""

# Create root window
root = tk.Tk()
root.configure(background="brown")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Physiotherapy Pose Detection Using Machine Learning")

# Set window icon
img = Image.open(r"D:\project\Sem 2\Images\111.ico")
if img.size != (32, 32):
    img = img.resize((32, 32), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)
root.iconphoto(False, photo)

# Background image setup
image2 = Image.open(r'D:\project\Sem 2\Images\a1.jpg')
image2 = image2.resize((1600, 1000), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

# Title label
label_l1 = tk.Label(root, text="Physiotherapy Pose Detection Using Machine Learning",
                    font=("Times New Roman", 28, 'bold'),
                    background="#C0C2D1", fg="black", width=65, height=1)
label_l1.place(x=0, y=0)

# Pose help window
def help():
    frame_alpr = tk.LabelFrame(root, text=" Yoga Poses ", width=900, height=550, bd=0, font=('times', 14, ' bold '), bg="#C0C2D1")
    frame_alpr.grid(row=0, column=0, sticky='nw')
    frame_alpr.place(x=450, y=120)

    pose_paths = [
        ("WRIST EXTENSION", r"D:\project\Sem 2\NEW IMAGES\WRIST EXTENSION.png", 500, 150),
        ("FINGER TIP TOUCHES", r"D:\project\Sem 2\NEW IMAGES\FINGER TIP TOUCHES.png", 700, 150),
        ("Grip", r"D:\project\Sem 2\NEW IMAGES\GRIP.jpg", 900, 150),
        ("CAT COW", r"D:\project\Sem 2\NEW IMAGES\CAT COW.png", 1100, 150),
        ("SPINAL TWIST", r"D:\project\Sem 2\NEW IMAGES\SPINAL TWIST.png", 500, 400),
        ("SHOULDER ROTATION", r"D:\project\Sem 2\NEW IMAGES\SHOULDER ROTATION.png", 700, 400),
        ("ARM ROTATION", r"D:\project\Sem 2\NEW IMAGES\ARM ROTATION.png", 900, 400)
    ]

    for pose_name, path, x, y in pose_paths:
        img = Image.open(path).resize((200, 200), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        label = tk.Label(root, image=photo, text=pose_name, compound='bottom')
        label.image = photo
        label.place(x=x, y=y)

# Corrected Navigation function
def action():
    """Launches the pose detection script."""
    try:
        # Change the path to point to your GUI_Master.py script
        run(["python", r"D:\project\Sem 2\GUI_Master.py"], check=True)
    except FileNotFoundError:
        ms.showerror("Error", "GUI_Master.py not found at the specified path.")
    except Exception as e:
        ms.showerror("Error", f"An error occurred: {e}")

# Exit window
def window():
    root.destroy()

# UI Buttons
button1 = tk.Button(root, text="Pose Recognization", command=action, width=22, height=1, bd=0,
                     bg="#C0C2D1", fg="black", font=('times', 20, ' bold '))
button1.place(x=100, y=220)

button2 = tk.Button(root, text="Pose Type", command=help, width=20, height=1, bd=0,
                     bg="#C0C2D1", fg="black", font=('times', 20, ' bold '))
button2.place(x=100, y=320)

exit_btn = tk.Button(root, text="Exit", command=window, width=14, height=1, bd=0,
                      font=('times', 20, ' bold '), bg="#C0C2D1", fg="black")
exit_btn.place(x=140, y=420)

# If you want to add a semi-transparent card overlay
card = tk.Canvas(root, width=500, height=300, highlightthickness=0, bg="white")
card.place(x=100, y=550)
card.create_rectangle(0, 0, 500, 300, fill="white", outline="", stipple="gray50")

root.mainloop()