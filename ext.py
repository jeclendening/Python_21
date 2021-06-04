from tkinter import *
from tkinter import filedialog
#import tkinter as tk
from PIL import ImageTk,Image
import os

my_window = Tk()
my_window.title("My images Python script")
my_window.iconbitmap('C:/Users/Jeffrey/Documents/my_tkinter/images/Cowboys.ico')
my_window.geometry("400x400")

def open_program():
	my_program = filedialog.askopenfilename()
	my_label.config(text=my_program)
	os.system('"%s"' % my_program)
	

def open_notepad():
	notepad = 'c:/Windows/System32/notepad.exe'
	os.system('"%s"' % notepad)

def open_textpad():
	textpad = ('c:/Program Files/TextPad 7/TextPad.exe')
	os.system('"%s"' % textpad)


def open_edge():
	edge = ('c:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe')
	os.system('"%s"' % edge)

def open_excel():
	excel = ('c:/Program Files (x86)/Microsoft Office/root/Office16/EXCEL.EXE')
	os.system('"%s"' % excel)

my_button = Button(my_window, text="Open Program", command=open_program)
my_button.pack(pady=20)

my_button2 = Button(my_window, text="NotePad", command=open_notepad)
my_button2.pack(pady=20)

my_button3 = Button(my_window, text="TextPad", command=open_textpad)
my_button3.pack(pady=20)

my_button4 = Button(my_window, text="Microsoft Edge", command=open_edge)
my_button4.pack(pady=20)

my_button5 = Button(my_window, text="Microsoft Excel", command=open_excel)
my_button5.pack(pady=20)

#c:/Program Files (x86)/Notepad++/notepad++.exe


my_label = Label(my_window, text="")
my_label.pack(pady=20)

my_window.mainloop()