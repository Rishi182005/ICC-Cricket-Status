import tkinter as tk
from tkinter import *
import random
from PIL import Image, ImageTk
import mysql.connector as x
import subprocess
import smtplib

y = x.connect(host="localhost", user="root", password="Rishi2005", database="icc")
z = y.cursor()

primary_color = "#007ACC"
secondary_color = "#00A3D9"
bg_color = "#F5F5F5"
font_color = "#333333"
otp = ""
generated_otp = ""  # Initialize generated_otp

def admin_page():
    global table1, column1, data1, data2
    table1 = tk.StringVar()
    column1 = tk.StringVar()
    data1 = tk.StringVar()
    data2 = tk.StringVar()

    # Create a canvas with a scrollbar
    canvas = Canvas(root, bg=bg_color)
    canvas.pack(side=LEFT, fill="both", expand=True)

    scrollbar = Scrollbar(root, command=canvas.yview)
    scrollbar.pack(side=LEFT, fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame inside the canvas to hold your widgets
    frame = Frame(canvas, bg=bg_color)
    canvas.create_window((0, 0), window=frame, anchor="center")

    Table_label = Label(frame, text="Table:", font=("Arial", 14), fg=font_color, bg=bg_color)
    Table_label.pack(pady=10)

    Table_entry = Entry(frame, font=("Arial", 14), textvariable=table1)
    Table_entry.pack(pady=10)

    Attribute_label = Label(frame, text="Column:", font=("Arial", 14), fg=font_color, bg=bg_color)
    Attribute_label.pack(pady=10)

    Attribute_entry = Entry(frame, font=("Arial", 14), textvariable=column1)
    Attribute_entry.pack(pady=10)

    A_label = Label(frame, text="Data to be modified:", font=("Arial", 14), fg=font_color, bg=bg_color)
    A_label.pack(pady=10)

    A_entry = Entry(frame, font=("Arial", 14), textvariable=data1)
    A_entry.pack(pady=10)

    B_label = Label(frame, text="New Data", font=("Arial", 14), fg=font_color, bg=bg_color)
    B_label.pack(pady=10)

    B_entry = Entry(frame, font=("Arial", 14), textvariable=data2)
    B_entry.pack(pady=10)

    Update_button = Button(frame, text="Update", font=("Calibri", 14, "bold"), command=modify_data)
    Update_button.pack(pady=10)

def modify_data():
    table_name = table1.get()
    column_name = column1.get()
    team_a_name = data1.get()
    team_b_name = data2.get()
    query = "UPDATE {} SET {} = %s WHERE {} = %s;".format(table_name, column_name, column_name)
    original_data = team_a_name
    new_data = team_b_name
    z.execute(query, (new_data, original_data))
        
    query1 = "SELECT * FROM {} WHERE {} = %s;".format(table_name, column_name)
    z.execute(query1, (new_data,))
    a = z.fetchall()
    y.commit()    
    if a:  # Check if any results were fetched
        Success_label = Label(root, text="Success!! Data has been modified!", font=("Arial", 14), fg=font_color, bg=bg_color)
        Success_label.pack(pady=10)
        
        result_label = Label(root, text=a, font=("Arial", 14), fg=font_color, bg=bg_color)
        result_label.pack(pady=10)
    else:
        No_Success_label = Label(root, text="Provided credentials are incorrect. Please check the data provided", font=("Arial", 14), fg=font_color, bg=bg_color)
        No_Success_label.pack(pady=10)



root = Tk()
root.title("LIVE CRICKET SCORE")
root.geometry("1920x1080")
root.resizable(width=True, height=True)
root.configure(bg=bg_color)

bg_image = Image.open("bg.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)

title_label = Label(root, text="Cricket Score App", font=("Arial", 36), fg=primary_color, bg=bg_color)
title_label.pack(pady=20)

admin_page()

label = Label(root)
label.pack()

root.mainloop()
