import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk

window=Tk()
window.geometry("400x400")
list=Listbox()
list.insert(1,"Python")
list.insert(2,"Css")
list.insert(3,"Java")
list.grid(padx=20,pady=40)

window.mainloop()