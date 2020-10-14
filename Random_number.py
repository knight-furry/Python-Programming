import tkinter as tk
from tkinter import ttk
from tkinter.massagebox import showinfo
import random
win = tk.Tk()
win.title("Random number Generator : ")
def play():
	random_num = random.randint(1,6)
	number.config(text = "Number is : {random_num}")
	if random_num == 6:
		showinfo("Congratulations ","You Win !!")
number = ttk.Lable(win , text = "")
number.pack(pady = 10)
play = ttk.Button(win , text = "Play",command = platy )
play.pack(padx = 50)
win.mainloop()
