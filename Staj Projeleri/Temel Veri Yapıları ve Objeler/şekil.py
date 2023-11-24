import tkinter
from tkinter import Tk,Canvas

wn=Tk()
wn.geometry("1000x800")

canvas=Canvas(wn, width=1000,height=800)
canvas.pack()

canvas.create_rectangle(10,200,80,270,outline="black",fill="darkblue",width=2)
canvas.create_oval(11,201,81,271,outline="black",fill="yellow",width=2)

canvas.create_polygon(44,201,11,234,79,274)

wn.mainloop()