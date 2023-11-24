import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk

window=Tk()
window.geometry("400x400")
def bilgiver():
    print("Butona tıklandı")

button=Button()
button.config(text="birinci button",bg="white",fg="black",command=bilgiver)
button.place(x=100,y=100)

window.mainloop()