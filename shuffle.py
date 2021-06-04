from tkinter import *
#import tkinter as tk
from PIL import ImageTk,Image
from random import choice
from random import shuffle

my_window = Tk()
my_window.title("My images Python script")
my_window.iconbitmap('C:/Users/Jeffrey/Documents/my_tkinter/images/Cowboys.ico')
my_window.geometry("400x400")

my_label = Label(my_window, text="", font=("Helvetica", 48))
my_label.pack(pady=20)

def  shuffler():
	

	states = ['Washington', 'Oregon', 'California', 'Ohio', 'Nebraska', 'Colorado', 'Michigan', 'Massachusetts', 'Florida', 'Texas', 'Oklahoma', 'Hawaii', 'Alaska', 'Utah', 'New Mexico', 'North Dakota', 'South Dakota', 'West Virginia', 'Virginia', 'New Jersey', 'Minnesota', 'Illinois', 'Indiana', 'Kentucky', 'Tennessee', 'Georgia', 'Alabama', 'Mississippi', 'North Carolina', 'South Carolina', 'Maine', 'Vermont', 'New Hampshire', 'Connecticut', 'Rhode Island', 'Wyoming', 'Montana', 'Kansas', 'Iowa', 'Pennsylvania', 'Maryland', 'Missouri', 'Arizona', 'Nevada', 'New York', 'Wisconsin', 'Delaware', 'Idaho', 'Arkansas', 'Louisiana']

	# pick random state from list
	global word
	word = choice(states)
	

	# break word
	break_apart_word = list(word)
	shuffle(break_apart_word)
	
	# turn Shuffled list into word
	global shuffled_word
	shuffled_word =  ''
	for letter in break_apart_word:
		shuffled_word += letter

	my_label.config(text=shuffled_word)


def answer():
	if word  == entry_answer.get():
		answer_label.config(text="Correct")
	else:
		answer_label.config(text="Incorrect")


entry_answer = Entry(my_window, font=("Helvetica"))
entry_answer.pack(pady=20)


my_button = Button(my_window, text="Pick Another Word", command=shuffler)
my_button.pack(pady=20)


answer_button = Button(my_window, text="Answer", command=answer)
answer_button.pack(pady=20)



answer_label = Label (my_window, text= '', font=("Helvetica",  18))
answer_label.pack(pady=20)


shuffler()
my_window.mainloop()