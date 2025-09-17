import tkinter as tk
from tkinter import messagebox as ms
from PIL import Image, ImageTk
from subprocess import run
from pathlib import Path

# === Base directory (project root) ===
BASE_DIR = Path(__file__).resolve().parent

# === Root window setup ===
root = tk.Tk()
root.title("AI-Enabled Pose Detection System for Automated Physiotherapy Feedback")
root.state("zoomed")
root.configure(bg="white")

# === Set app icon ===
icon_path = BASE_DIR / "yoga_app" / "static" / "images" / "logo-lotus.png"
if icon_path.exists():
    root.iconphoto(False, ImageTk.PhotoImage(Image.open(icon_path).resize((32, 32))))

# === Screen dimensions ===
w, h = root.winfo_screenwidth(), root.winfo_screenheight()

# === Background Image ===
bg_path = BASE_DIR / "yoga_app" / "static" / "images" / "bg-image.jpg"
if bg_path.exists():
    bg_image = Image.open(bg_path).resize((w, h), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    tk.Label(root, image=bg_photo).place(x=0, y=0, relwidth=1, relheight=1)

# === Buttons ===
def create_top_button(text, command, bg, fg):
    return tk.Button(
        root,
        text=text,
        command=command,
        font=("Helvetica", 14, "bold"),
        bg=bg,
        fg=fg,
        bd=2,
        relief="solid",
        padx=20,
        pady=10,
        activebackground=bg,
        activeforeground=fg,
        cursor="hand2",
        highlightthickness=0
    )

# --- Corrected Button Placement ---
# Create a frame to hold the buttons, placed in the top-right corner
button_frame = tk.Frame(root, bg="white")
button_frame.pack(side="top", anchor="ne", padx=20, pady=20)

btn_login = create_top_button("LOGIN", lambda: run(["python", str(BASE_DIR / "login.py")]), "#d4cfc9", "black")
btn_login.pack(side="left", padx=5)

btn_register = create_top_button("REGISTER", lambda: run(["python", str(BASE_DIR / "registration.py")]), "white", "black")
btn_register.pack(side="left", padx=5)
# --- End Corrected Placement ---

# === Logo & Title ===
logo_path = BASE_DIR / "yoga_app" / "static" / "images" / "logo-lotus.png"
if logo_path.exists():
    logo_img = Image.open(logo_path).resize((65, 65), Image.LANCZOS)
    logo_photo = ImageTk.PhotoImage(logo_img)
    tk.Label(root, image=logo_photo, bg="white").place(x=150, y=92)

tk.Label(
    root,
    text="Yoga\nStudio",
    font=("Helvetica", 20, "bold"),
    fg="black",
    justify="left"
).place(x=210, y=90)

# === Taglines ===
tk.Label(
    root,
    text="Yoga, Uncomplicated",
    font=("Helvetica", 20),
    fg="black",
).place(x=60, y=540)

tk.Label(
    root,
    text="Start Your Journey",
    font=("Helvetica", 42, "bold"),
    fg="black",
).place(x=60, y=600)

tk.Label(
    root,
    text="to Inner Peace",
    font=("Helvetica", 42, "bold"),
    fg="black",
).place(x=60, y=660)

# === Social Media Icons ===
icon_paths = {
    "facebook": BASE_DIR / "yoga_app" / "static" / "icons" / "facebook.png",
    "youtube": BASE_DIR / "yoga_app" / "static" / "icons" / "yt.png",
    "instagram": BASE_DIR / "yoga_app" / "static" / "icons" / "insta.png",
    "linkedin": BASE_DIR / "yoga_app" / "static" / "icons" / "ln.png"
}

x_icon = 60
for path in icon_paths.values():
    if path.exists():
        icon_img = Image.open(path).resize((45, 45), Image.LANCZOS)
        icon_photo = ImageTk.PhotoImage(icon_img)
        icon_label = tk.Label(root, image=icon_photo, bg="white", cursor="hand2")
        icon_label.image = icon_photo
        icon_label.place(x=x_icon, y=730)
    x_icon += 60

# === Footer ===
tk.Label(
    root,
    text="Your Body, Your Ritual!",
    font=("Helvetica", 18, "bold"),
    fg="black",
    bg="white"
).place(x=108, y=913)

root.mainloop()