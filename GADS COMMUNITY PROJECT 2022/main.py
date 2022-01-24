#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Jan 2022

@author: Deborah Ajah
"""

#Importing Modules
import tkinter as tk
import student_management_system as sd
from PIL import ImageTk
from PIL import Image


# Designing the General MAINWINDOW Framework
mainWindow = tk.Tk()
mainWindow.title('Student Management System | GADS 2022 Community Project')
mainWindow.configure(bg='white')


#Importing and Rezing the LOGO Used (The Google Africa Developers Logo 2022)
filename = 'GADS.PNG'
img = Image.open(filename)
resized_img = img.resize((150, 80))

mainWindow.photoimg = ImageTk.PhotoImage(resized_img)
labelimage = tk.Label(mainWindow, image=mainWindow.photoimg)
labelimage.place(relx=0.5,
                 rely=0.03,
                 anchor='center')


#Specicifying the colours and Fonts for the LABEL1

label_1 = tk.Label(mainWindow, text="\n GADS STUDENTS INFORMATION PORTAL  \n", bg='white', fg='blue1', font=("Georgia", 30))
label_1.pack(padx=100, pady=50)


#specificying the BUTTONS colours and commands colour
button_1 = tk.Button(mainWindow, text="Add Student", fg = 'green', command=lambda: sd.insert(), padx=275, pady=25,
                     activebackground='grey', activeforeground='red')
button_1.pack()

button_2 = tk.Button(mainWindow, text="Update Student Details", fg = 'gold', command=lambda: sd.update(), padx=240, pady=25,
                     activebackground='black', activeforeground='blue')
button_2.pack()

button_3 = tk.Button(mainWindow, text="View Student Details", fg = 'navy blue', command=lambda: sd.display(), padx=248, pady=25,
                     activebackground='grey', activeforeground='green')
button_3.pack()

button_4 = tk.Button(mainWindow, text="Delete Student", fg = 'red', command=lambda: sd.delete(), padx=267, pady=25,
                     activebackground='grey', activeforeground='white')
button_4.pack()

button_5 = tk.Button(mainWindow, text="Search Student", fg = 'dark violet', command=lambda: sd.search(), padx=267, pady=25,
                     activebackground='grey', activeforeground='black')
button_5.pack()


#Specicifying the colours and Fonts for the LABEL2. Label2 can contain any information

label_2 = tk.Label(mainWindow, text="Modified by Deborah Ajah for Google Africa Developer Communitiy Project 2022 (GITHUB: @DebbyCode). ", font=('arial', 12), bg = 'white', fg='black')
label_2.place(relx=0.0,
              rely=1.0,
              anchor='sw')


mainWindow.mainloop()
