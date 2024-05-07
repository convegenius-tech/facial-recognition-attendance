
from _typeshed import Self
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()

image = Image.open(r"C:\Users\Reks\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\img\6.jpg")
image = image.resize((20,20), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)
my_img = Label(root,image = my_img)
my_img.pack()
root.mainloop()