import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk

window=Tk()
window.geometry("400x400")

var = IntVar
box=Checkbutton(window,text="Onaylıyor musunuz?",variable=var,onvalue=1,offvalue=2)
box.pack()

window.mainloop()