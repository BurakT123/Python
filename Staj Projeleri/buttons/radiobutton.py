import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk

window=Tk()
window.geometry("400x400")

gender=tk.IntVar()
man=tk.Radiobutton(window,text="erkek",value=1,variable=gender)
man.config(font=("Arial",15))
man.place(x=50,y=50)
woman=tk.Radiobutton(window,text="kadın",value=2,variable=gender)
woman.config(font=("Arial",15))
woman.place(x=150,y=50)
gender.set(1)

window.mainloop()