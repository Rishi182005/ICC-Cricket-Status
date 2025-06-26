import tkinter as tk
from tkinter import *
import random
from PIL import Image, ImageTk
import mysql.connector as x
import subprocess
import smtplib

# Note d,e,f cant be used from now

y = x.connect(host="localhost", user="root", password="Rishi2005", database="icc")
z = y.cursor()

# Create a custom color palette
primary_color = "#007ACC"
secondary_color = "#00A3D9"
bg_color = "#F5F5F5"
font_color = "#333333"
otp = ""
generated_otp = ""  # Initialize generated_otp


def send_otp_email(receiver_email, otp):
    try:
        loading_label = Label(root, text="Generating OTP", font=("Arial", 14), fg=font_color, bg='SystemButtonFace')
        loading_label.pack(pady=10)
        smtp_server = "smtp.gmail.com"
        smtp_port = 587  
        sender_email = "cricninja18@gmail.com"
        sender_password = "cqng pgus axxa zemu"

        subject = "OTP Verification"
        message = f"Your OTP for verification is {otp}"  

        # Create an SMTP connection
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, f"Subject: {subject}\n\n{message}")

        # Close the SMTP server
        server.quit()
        return True
    except Exception as e:
        print("Error sending email:", e)
        return False

def otp_user_verification(otp):
    clear_widgets()
    otp_label = Label(root, text="Enter the OTP", font=("Arial", 14), fg=font_color, bg=bg_color)
    otp_label.pack(pady=10)
    otp_entry = Entry(root, font=("Arial", 14), textvariable=user_otp)
    otp_entry.pack(pady=10)
    validate_button = Button(root, text="Validate OTP", font=("Calibri", 14, "bold"), command=Otp_user_verify)
    validate_button.place(x=750, y=600)
    back_button = Button(root, text="Go Back", font=("Calibri", 14, "bold"), command=show_user_login_fields)
    back_button.place(x=600, y=600)

def Otp_user_verify():
    entered_otp = user_otp.get()  # Get entered OTP from the user
    if entered_otp == otp:
        verified_label = Label(root, text="Success", font=("Arial", 14), fg=font_color, bg=bg_color)
        verified_label.pack(pady=10)
        if k==1:
            subprocess.run(["python", "User_homepage.py"])
        if k==2:
            show_user_login_fields()
        if k==3:
            subprocess.run(["python", "Admin_homepage.py"])
        
    else:
        verified_label = Label(root, text="Enter Valid OTP", font=("Arial", 14), fg=font_color, bg=bg_color)
        verified_label.pack(pady=10)

def User_details():
    global k
    k=1
    a = user_username.get()
    b = user_email.get()
    c = user_password.get()

    z.execute("SELECT * FROM user WHERE Username = %s AND Email = %s AND Password = %s;", (a, b, c))
    result = z.fetchone()

    if result:
        Success_label = Label(root, text="Login successful", font=("Arial", 14), fg=primary_color)
        Success_label.pack(pady=10)
        otp_value = str(random.randint(1000, 9999))  # Generate a new OTP
        global otp
        otp = otp_value
        if send_otp_email(b, otp):
            otp_label = Label(root, text="OTP has been sent", font=("Arial", 14), fg=font_color, bg=bg_color)
            otp_label.pack(pady=10)
            otp_user_verification(otp)
        else:
            otp_label = Label(root, text="Error in sending OTP", font=("Arial", 14), fg=font_color, bg=bg_color)
            otp_label.pack(pady=10)
    else:
        Error_label = Label(root, text="Invalid username, email, or password", font=("Arial", 14), fg="red")
        Error_label.pack(pady=10)

    y.commit()

def is_valid_email(email):
    return email.endswith("@gmail.com")

def is_valid_password(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    special_characters = "!@#$%^&*()-_+=<>?/"
    if not any(char in special_characters for char in password):
        return False
    return True

def selection():
    global radio
    submit_text = "Submit"
    temp = str(radio.get())
    if temp == '1':
        submit_text += " (User)"
        submit_button.config(command=show_user_login_fields)
    else:
        submit_text += " (Admin)"
        submit_button.config(command=show_admin_login_fields)
    submit_button.config(text=submit_text)

def show_user_login_fields():
    global email_entry, password_entry, submit_login_button

    clear_widgets()

    username_label = Label(root, text="Username:", font=("Arial", 14), fg=font_color, bg=bg_color)
    username_label.pack(pady=10)

    username_entry = Entry(root, font=("Arial", 14), textvariable=user_username)
    username_entry.pack(pady=10)

    email_label = Label(root, text="Email:", font=("Arial", 14), fg=font_color, bg=bg_color)
    email_label.pack(pady=10)

    email_entry = Entry(root, font=("Arial", 14), textvariable=user_email)
    email_entry.pack(pady=10)

    password_label = Label(root, text="Password:", font=("Arial", 14), fg=font_color, bg=bg_color)
    password_label.pack(pady=10)

    password_entry = Entry(root, show="*", font=("Arial", 14), textvariable=user_password)
    password_entry.pack(pady=10)

    register_button = Button(root, text="Register", font=("Calibri", 14, "bold"), command=show_registration_form)
    register_button.place(x=600, y=600)

    submit_login_button = Button(root, text="Login", font=("Calibri", 14, "bold"), command=User_details, state=DISABLED)
    submit_login_button.place(x=750, y=600)

    def validate_login_fields(event=None):
        if is_valid_email(user_email.get()) and is_valid_password(user_password.get()):
            submit_login_button.config(state=NORMAL)
        else:
            submit_login_button.config(state=DISABLED)

    email_entry.bind("<KeyRelease>", validate_login_fields)
    password_entry.bind("<KeyRelease>", validate_login_fields)

    back_button = Button(root, text="Go Back", font=("Calibri", 14, "bold"), command=login_page)
    back_button.place(x=900, y=600)

def show_registration_form():
    clear_widgets()

    registration_label = Label(root, text="User Registration", font=("Arial", 24), fg=primary_color, bg=bg_color)
    registration_label.pack(pady=20)

    username_label = Label(root, text="Username:", font=("Arial", 14), fg=font_color, bg=bg_color)
    username_label.pack(pady=10)

    username_entry = Entry(root, font=("Arial", 14), textvariable=reg_username)
    username_entry.pack(pady=10)

    email_label = Label(root, text="Email:", font=("Arial", 14), fg=font_color, bg=bg_color)
    email_label.pack(pady=10)

    email_entry = Entry(root, font=("Arial", 14), textvariable=reg_email)
    email_entry.pack(pady=10)

    password_label = Label(root, text="Password:", font=("Arial", 14), fg=font_color, bg=bg_color)
    password_label.pack(pady=10)

    password_entry = Entry(root, show="*", font=("Arial", 14), textvariable=reg_password)
    password_entry.pack(pady=10)

    register_button = Button(root, text="Register", font=("Calibri", 14, "bold"), command=register_user, state=DISABLED)
    register_button.pack(pady=20)

    def validate_login_fields(event=None):
        if is_valid_email(reg_email.get()) and is_valid_password(reg_password.get()):
            register_button.config(state=NORMAL)
        else:
            register_button.config(state=DISABLED)

    email_entry.bind("<KeyRelease>", validate_login_fields)
    password_entry.bind("<KeyRelease>", validate_login_fields)

    back_button = Button(root, text="Go Back", font=("Calibri", 14, "bold"), command=show_user_login_fields)
    back_button.place(x=600, y=600)

def show_admin_login_fields():
    clear_widgets()

    admin_id_label = Label(root, text="Admin ID:", font=("Arial", 14), fg=font_color, bg=bg_color)
    admin_id_label.pack(pady=10)

    admin_id_entry = Entry(root, font=("Arial", 14), textvariable=admin_id)
    admin_id_entry.pack(pady=10)

    email_label = Label(root, text="Email:", font=("Arial", 14), fg=font_color, bg=bg_color)
    email_label.pack(pady=10)

    email_entry = Entry(root, font=("Arial", 14), textvariable=admin_email)
    email_entry.pack(pady=10)

    password_label = Label(root, text="Password:", font=("Arial", 14), fg=font_color, bg=bg_color)
    password_label.pack(pady=10)

    password_entry = Entry(root, show="*", font=("Arial", 14), textvariable=admin_password)
    password_entry.pack(pady=10)

    submit_login_button = Button(root, text="Login", font=("Calibri", 14, "bold"), command=Admin_details, state=DISABLED)
    submit_login_button.place(x=750, y=600)

    def validate_admin_login_fields(event=None):
        if is_valid_password(admin_password.get()) and is_valid_email(admin_email.get()):
            submit_login_button.config(state=NORMAL)
        else:
            submit_login_button.config(state=DISABLED)

    password_entry.bind("<KeyRelease>", validate_admin_login_fields)
    email_entry.bind("<KeyRelease>", validate_admin_login_fields)

    back_button = Button(root, text="Go Back", font=("Calibri", 14, "bold"), command=goback)
    back_button.place(x=900, y=600)

def goback():
    clear_widgets()
    login_page()

def login_page():
    clear_widgets()
    global radio, r1, r2, submit_button

    radio = IntVar()
    Label(text="Select your login", font=('Arial', 31), fg=primary_color, bg=bg_color).pack(pady=100)

    r1 = Radiobutton(root, text=" User ", font=('Arial', 31), variable=radio, value=1, command=selection)
    r1.pack(padx=100, pady=80)

    r2 = Radiobutton(root, text="Admin", font=('Arial', 31), variable=radio, value=2, command=selection)
    r2.pack(padx=100)

    submit_button = Button(root, text="Submit", font=("Calibri", 14, "bold"), command=None)
    submit_button.pack(pady=100)

def Admin_details():
    global k
    k=3
    a = admin_id.get().lower()
    b = admin_email.get()
    c = admin_password.get()
    z.execute("SELECT * FROM admin WHERE Admin_ID = %s AND Email = %s AND Password = %s;", (a,b,c))
    result = z.fetchone()

    if result:
        Success_label = Label(root, text="Login successful", font=("Arial", 14), fg=primary_color)
        Success_label.pack(pady=10)
        otp_value = str(random.randint(1000, 9999))  # Generate a new OTP
        global otp
        otp = otp_value
        if send_otp_email(b, otp):
            otp_label = Label(root, text="OTP has been sent", font=("Arial", 14), fg=font_color, bg=bg_color)
            otp_label.pack(pady=10)
            otp_user_verification(otp)
        else:
            otp_label = Label(root, text="Error in sending OTP", font=("Arial", 14), fg=font_color, bg=bg_color)
            otp_label.pack(pady=10)
    else:
        Error_label = Label(root, text="Invalid username, email, or password", font=("Arial", 14), fg="red")
        Error_label.pack(pady=10)

    y.commit()

def clear_widgets():
    for widget in root.winfo_children():
        widget.destroy()
    bg_label = Label(root, image=bg_photo)
    bg_label.place(x=0, y=0)

def register_user():
    global k
    k=2
    a = reg_username.get()
    b = reg_email.get()
    c = reg_password.get()
    z.execute("SELECT Username, Email FROM user")
    existing_users = z.fetchall()

    for username, email in existing_users:
        if username == a:
            Error_label = Label(root, text="Username Already registered", font=("Arial", 14), fg="red")
            Error_label.place(x=20)
            return
        if email == b:
            Error_label = Label(root, text="Email Already registered", font=("Arial", 14), fg="red")
            Error_label.place(x=20)
            return

    if (b.endswith("@gmail.com")
        and len(c) >= 8
        and any(char.isupper() for char in c)
        and any(char.islower() for char in c)
        and any(char.isdigit() for char in c)
        and any(char in "!@#$%^&*()-_+=<>?/" for char in c)):
        z.execute("INSERT INTO user(Username, Email, Password) VALUES (%s, %s, %s)", (a, b, c))
        y.commit()
        otp_value = str(random.randint(1000, 9999))  # Generate a new OTP
        global otp
        otp = otp_value
        if send_otp_email(b, otp):
            otp_label = Label(root, text="OTP has been sent", font=("Arial", 14), fg=font_color, bg=bg_color)
            otp_label.pack(pady=10)
            otp_user_verification(otp)
        else:
            otp_label = Label(root, text="Error in sending OTP", font=("Arial", 14), fg=font_color, bg=bg_color)
            otp_label.pack(pady=10)

root = tk.Tk()
root.title("LIVE CRICKET SCORE")
root.geometry("1920x1080")
root.resizable(width=True, height=True)
root.configure(bg=bg_color)

# Load a background image
bg_image = Image.open("cricket.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a frame for better organization
frame = Frame(root, bg=bg_color)
frame.pack(expand=YES, fill=BOTH)

# Create a label for the title
title_label = Label(frame, text="Cricket Score App", font=("Arial", 36), fg=primary_color, bg=bg_color)
title_label.pack(pady=20)

login_page()
user_otp = tk.StringVar()
reg_otp=tk.StringVar()
admin_otp = tk.StringVar()
user_username = tk.StringVar()
user_password = tk.StringVar()
user_email = tk.StringVar()
admin_id = tk.StringVar()
admin_email = tk.StringVar()
admin_password = tk.StringVar()
reg_username = tk.StringVar()
reg_email = tk.StringVar()
reg_password = tk.StringVar()

label = Label(root)
label.pack()

root.mainloop()
