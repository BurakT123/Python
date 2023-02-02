import tkinter
from tkinter import Tk,Canvas

wn=Tk()
wn.geometry("1000x800")

canvas=Canvas(wn,width=1000,height=800)
canvas.pack()

canvas.create_oval(5,195,65,265,outline="black",fill="white",width=2)
canvas.create_rectangle(10,200,70,270,outline="black",fill="blue",width=1)


wn.mainloop()