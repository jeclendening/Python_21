from tkinter import *
#import tkinter as tk
from PIL import ImageTk,Image
import time

my_window = Tk()
my_window.title("My images Python script")
my_window.iconbitmap('C:/Users/Jeffrey/Documents/my_tkinter/images/Cowboys.ico')
my_window.geometry("400x400")

def clock():
	hour = time.strftime("%I")
	minute = time.strftime("%M")
	second = time.strftime("%S")
	day = time.strftime("%A")
	am_pm = time.strftime("%p")
	time_zone = time.strftime("%Z")

	my_label.config(text= hour + ":" + minute + ":" + second + " " + am_pm)
	my_label.after(1000, clock)

	my_label2.config(text=time_zone + " " + day)



def update():
	my_label.config(text="New Text")

my_label = Label(my_window, text="", font=("Helvetica", 48), fg="green", bg="black")
my_label.pack(pady=20) 

my_label.after(5000, update)

my_label2 = Label(my_window, text="", font=("Helvetica", 14))
my_label2.pack(pady=10)

clock()

my_window.mainloop()
