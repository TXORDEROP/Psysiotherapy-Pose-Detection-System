import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import cv2

##############################################+=============================================================
root = tk.Tk()
root.configure(background="skyblue")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Login Form")

# App icon - replace with a real image (NOT .mp4)
from PIL import Image
img = Image.open(r"D:\project\Sem 2\Images\1.webp")
img = img.resize((32, 32), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)
root.iconphoto(False, photo)

username = tk.StringVar()
password = tk.StringVar()

# ====== VIDEO BACKGROUND START ======
video_path = r"D:\project\Sem 2\Images\111.ico"
cap = cv2.VideoCapture(video_path)

background_label = tk.Label(root)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def play_video():
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (w, h))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = ImageTk.PhotoImage(Image.fromarray(frame))
        background_label.config(image=img)
        background_label.image = img
        root.after(30, play_video)
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        play_video()

play_video()
# ====== VIDEO BACKGROUND END ======

def registration():
    from subprocess import call
    call(["python", r"D:\project\Sem 2\registration.py"])
    root.destroy()

def login():
    with sqlite3.connect(r'D:\project\Sem 2\evaluation.db') as db:
        c = db.cursor()
        db = sqlite3.connect(r'D:\project\Sem 2\evaluation.db')
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS registration"
                       "(Fullname TEXT, username TEXT, Email TEXT, password TEXT)")
        db.commit()
        find_entry = ('SELECT * FROM registration WHERE username = ? and password = ?')
        c.execute(find_entry, [(username.get()), (password.get())])
        result = c.fetchall()
        if result:
            ms.showinfo("messege", "LogIn sucessfully")
            from subprocess import call
            call(["python", r"D:\project\Sem 2\Home.py"])
            root.destroy()
        else:
            ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')

Login_frame = tk.Frame(root, bg="#A5ABA0")
Login_frame.place(x=505, y=250)

logolbl = tk.Label(Login_frame, text="Login Here", font=("Algerian", 30, "bold", "italic"), bd=5, bg="#A5ABA0", fg="black")
logolbl.grid(row=0, columnspan=2, pady=20)

lbluser = tk.Label(Login_frame, text="Username", compound=LEFT, font=("Times new roman", 20, "bold"), bg="#A5ABA0")
lbluser.grid(row=1, column=0, padx=20, pady=10)
txtuser = tk.Entry(Login_frame, bd=0, textvariable=username, font=("", 15))
txtuser.grid(row=1, column=1, padx=20)

lblpass = tk.Label(Login_frame, text="Password", compound=LEFT, font=("Times new roman", 20, "bold"), bg="#A5ABA0")
lblpass.grid(row=2, column=0, padx=50, pady=10)
txtpass = tk.Entry(Login_frame, bd=0, textvariable=password, show="*", font=("", 15))
txtpass.grid(row=2, column=1, padx=20)

btn_log = tk.Button(Login_frame, text="Login", command=login, width=15, font=("Times new roman", 14, "bold"), bg="#A5ABA0", fg="black", bd=1)
btn_log.grid(row=3, column=1, pady=10)
btn_reg = tk.Button(Login_frame, text="Create Account", command=registration, width=15, font=("Times new roman", 14, "bold"), bg="#A5ABA0", fg="black", bd=1)
btn_reg.grid(row=3, column=0, pady=10)

root.mainloop()
