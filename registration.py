import tkinter as tk
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random
import os
import cv2
from subprocess import run # Changed to run

window = tk.Tk()
w,h = window.winfo_screenwidth(),window.winfo_screenheight()
window.geometry("%dx%d+0+0"%(w,h))
window.title("REGISTRATION FORM")
window.configure(background="blue")
img = Image.open(r"D:\project\Sem 2\Images\111.ico") # Replace with your image path
if img.size != (32, 32):
    img = img.resize((32, 32), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)
window.iconphoto(False, photo)


Fullname = tk.StringVar()
username = tk.StringVar()
Email = tk.StringVar()
password = tk.StringVar()
password1 = tk.StringVar()

value = random.randint(1, 1000)
print(value)

# database code
db = sqlite3.connect(r"D:\project\Sem 2\evaluation.db")
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS registration"
                "(Fullname TEXT, username TEXT, Email TEXT, password TEXT)")
db.commit()



def password_check(passwd): 
    
    SpecialSym =['$', '@', '#', '%'] 
    val = True
    
    if len(passwd) < 6: 
        print('length should be at least 6') 
        val = False
        
    if len(passwd) > 20: 
        print('length should be not be greater than 8') 
        val = False
        
    if not any(char.isdigit() for char in passwd): 
        print('Password should have at least one numeral') 
        val = False
        
    if not any(char.isupper() for char in passwd): 
        print('Password should have at least one uppercase letter') 
        val = False
        
    if not any(char.islower() for char in passwd): 
        print('Password should have at least one lowercase letter') 
        val = False
        
    if not any(char in SpecialSym for char in passwd): 
        print('Password should have at least one of the symbols $@#') 
        val = False
    if val: 
        return val 

def insert():
    fname = Fullname.get()
    un = username.get()
    email = Email.get()
    pwd = password.get()
    cnpwd = password1.get()

    with sqlite3.connect(r"D:\project\Sem 2\evaluation.db") as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    find_user = ('SELECT * FROM registration WHERE username = ?')
    c.execute(find_user, [(username.get())])

    # to check mail
    regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        a = True
    else:
        a = False
    
    # validation
    if (fname.isdigit() or (fname == "")):
        ms.showinfo("Message", "please enter valid name")
    elif (email == "") or (a == False):
        ms.showinfo("Message", "Please Enter valid email")
    elif (c.fetchall()):
        ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
    elif (pwd == ""):
        ms.showinfo("Message", "Please Enter valid password")
    elif(pwd=="")or(password_check(pwd))!=True:
        ms.showinfo("Message", "password must contain atleast 1 Uppercase letter,1 symbol,1 number")
    elif (pwd != cnpwd):
        ms.showinfo("Message", "Password Confirm password must be same")
    else:
        conn = sqlite3.connect('evaluation.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO registration(Fullname, username, Email, password) VALUES(?,?,?,?)',
                (fname, un, email, pwd))

            conn.commit()
            db.close()
            ms.showinfo('Success!', 'Account Created Successfully !')
            
            # --- Corrected logic ---
            # This will close the current window and open the new one
            window.destroy()
            run(["python", r"D:\project\Sem 2\login.py"])
            # --- End corrected logic ---

# Function for the "Sign in" button
def log():
    window.destroy()
    run(["python", "login.py"])


# GUI elements
image2 =Image.open(r"D:\project\Sem 2\Images\2.jpg")
image2 =image2.resize((w,h), Image.LANCZOS)
background_image=ImageTk.PhotoImage(image2)
background_label = tk.Label(window, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

frame = tk.LabelFrame(window, text="", width=370, height=579, bd=0, font=('times', 14, ' bold '),bg="#B1B1B1")
frame.grid(row=0, column=0, sticky='nw')
frame.place(x=900, y=88)

lbl = tk.Label(window, text="Register your account", font=('times', 20,' bold '), height=1, width=18,bg="#B1B1B1",fg="black")
lbl.place(x=950, y=35)

l2 = tk.Label(frame, text="Name", width=4, font=("Times new roman", 15, "bold"), bg="#B1B1B1",bd=5, fg="black")
l2.place(x=25, y=5)
t1 = tk.Entry(frame, textvar=Fullname, width=26, font=('', 15),bd=1, bg="white")
t1.place(x=26, y=35)

l4 = tk.Label(frame, text="Username", width=7, font=("Times new roman", 15, "bold"), bg="#B1B1B1")
l4.place(x=25, y=95)
t3 = tk.Entry(frame, textvar=username, width=26, font=('', 15),bd=1,  bg="white")
t3.place(x=26, y=125)

l5 = tk.Label(frame, text="E-mail", width=5, font=("Times new roman", 15, "bold"), bg="#B1B1B1")
l5.place(x=23, y=185)
t4 = tk.Entry(frame, textvar=Email, width=26, font=('', 15),bd=1, bg="white")
t4.place(x=26, y=215)

l9 = tk.Label(frame, text="Password", width=7, font=("Times new roman", 15, "bold"), bg="#B1B1B1")
l9.place(x=24, y=275)
t9 = tk.Entry(frame, textvar=password, width=26, font=('', 15), show="*",bd=1,  bg="white")
t9.place(x=26, y=305)

l10 = tk.Label(frame, text="Confirm Password", width=13, font=("Times new roman", 15, "bold"), bg="#B1B1B1")
l10.place(x=26, y=365)
t10 = tk.Entry(frame, textvar=password1, width=26, font=('', 15), show="*",bd=1,  bg="white")
t10.place(x=26, y=395)

btn = tk.Button(frame, text="Sign up", bg="#B1B1B1",font=("times",17),fg="black", width=22,bd=0,  command=insert)
btn.place(x=25, y=455)

l10 = tk.Label(frame, text="Already have an account?", width=20, font=("Times new roman", 13), bg="#B1B1B1")
l10.place(x=35, y=525)

btn = tk.Button(frame, text="Sign in.", bg="#B1B1B1",font=('times 15 bold underline'),fg="blue", bd=0, command=log)
btn.place(x=218, y=518)

window.mainloop()