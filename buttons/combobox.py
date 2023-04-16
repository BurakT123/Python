import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk

window=Tk()
window.geometry("400x400")

work =ttk.Combobox(window)
work['values']=("İşsiz","Mühendis","Öğretmen")
work.config(font=("Arial",15))
work.place(x=150,y=150)
work.current(1)

window.mainloop()