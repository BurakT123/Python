import tkinter
from tkinter import *

pencere = Tk()
pencere.geometry("1920x1080")
canvas = Canvas(pencere, width=1920, height=1080)
canvas.pack()

def fe():
    entry1.focus()
    
def cikis():
    pencere.destroy()

def kaydet():
    a = str(entry1.get())
    b = str(entry2.get())
    c = str(entry3.get())
    d = str(entry4.get())
    e = str(entry5.get())
    if a and b and c and d and e:
        file = open("E:\GitHub\library\Introduction-to-Algorithm-and-Programming\PhytonSchemas\metinler.txt", "a")
        file.write(a + "\n" + b + "\n" + c + "\n" + d + "\n" + e + "\n\n")
        file.close()
        temizle()

def temizle():
    if entry1:
        entry1.delete(0, 20)
    if entry2:
        entry2.delete(0, 20)
    if entry3:
        entry3.delete(0, 20)
    if entry4:
        entry4.delete(0, 20)
    if entry5:
        entry5.delete(0, 20)
    if entry5:
        entry6.delete(0, 20)
    canvas.delete("all")

def ara():
    f=open("E:\GitHub\library\Introduction-to-Algorithm-and-Programming\PhytonSchemas\metinler.txt","r")
    k=0
    s=str(entry6.get())
    x=0
    for line in f:
        k+=20
        if s in line:
            canvas.create_text(100,450+k,font="Times 14 italic bold",text=line)
    f.close

def listele():
    file = open("E:\GitHub\library\Introduction-to-Algorithm-and-Programming\PhytonSchemas\metinler.txt", "r")
    k = 0
    lineCount = 1
    lineCount1 = 1

    for line in file:
        if lineCount1 == 1:
            canvas.create_text(100, 480 + (lineCount1 * 20), font="Times 16 italic bold", text="Numarası: " + line)
        if lineCount1 == 2:
            canvas.create_text(150, 480 + (lineCount1 * 20), font="Times 16 italic bold", text="Adı Soyadı: " + line)
        if lineCount1 == 3:
            canvas.create_text(200, 480 + (lineCount1 * 20), font="Times 16 italic bold", text="Cinsiyet: " + line)
        if lineCount1 == 4:
            canvas.create_text(250, 480 + (lineCount1 * 20), font="Times 16 italic bold", text="Bölümü: " + line)
        if lineCount1 == 5:
            canvas.create_text(300, 480 + (lineCount1 * 20), font="Times 16 italic bold", text="İli: " + line)
        if lineCount1 == 6:
            lineCount1 = 1
        else:
            lineCount1 =+ 1
                  
"""
    for line in file:
        if lineCount == 1:
            lineText = "Numarası: "
        if lineCount == 2:
            lineText = "Adı Soyadı: "
        if lineCount == 3:
            lineText = "Cinsiyeti: "
        if lineCount == 4:
            lineText = "Bölümü: "
        if lineCount == 5:
            lineText = "İli: "
        if lineCount == 6:
            lineText = "------------------------------"
        canvas.create_text(100, 520+k, font="Times 16 italic bold", text=lineText+line)
        k = k + 30
        if lineCount == 6:
            lineCount = 1
        else:
            lineCount = lineCount + 1
            
""" 
def ara():
    print("test")

label0=Label(pencere)
label0.config(text="Kayıt Bilgileri", font=("Arial",20))
label0.place(x=20, y=3)

label1=Label(pencere)
label1.config(text="Numarası", font=("Arial",12))
label1.place(x=20, y=50)

label2=Label(pencere)
label2.config(text="Adı Soyadı", font=("Arial",12))
label2.place(x=20, y=100)

label3=Label(pencere)
label3.config(text="Cinsiyet", font=("Arial",12))
label3.place(x=20, y=150)

label4=Label(pencere)
label4.config(text="Bölüm", font=("Arial",12))
label4.place(x=20, y=200)

label5=Label(pencere)
label5.config(text="İli", font=("Arial",12)) 
label5.place(x=20,y=250)

label6 = Label(pencere)
label6.config(text="Ara", font=("Arial",12)) 
label6.place(x=20,y=300)

entry1=Entry(pencere)
entry1.config(font=("Arial", 12))
entry1.place(x=150,y=50)
entry1.focus()

entry2=Entry(pencere)
entry2.config(font=("Arial", 12))
entry2.place(x=150,y=100)

entry3=Entry(pencere)
entry3.config(font=("Arial", 12))
entry3.place(x=150,y=150)

entry4=Entry(pencere)
entry4.config(font=("Arial", 12))
entry4.place(x=150,y=200)

entry5=Entry(pencere)
entry5.config(font=("Arial", 12))
entry5.place(x=150,y=250)

entry6=Entry(pencere)
entry6.config(font=("Arial", 12))
entry6.place(x=150,y=420)

button1 = Button(pencere)
button1.config(text="Kayıt", bg="white", fg="black", command=kaydet)
button1.place(x=20, y=300)

button2 = Button(pencere)
button2.config(text="Temizle", bg="white", fg="black", command=temizle)
button2.place(x=20, y=330)

button3 = Button(pencere)
button3.config(text="Çıkış Yap", bg="white", fg="black", command=cikis)
button3.place(x=20, y=360)

button4 = Button(pencere)
button4.config(text="Liste", bg="white", fg="black", command=listele)
button4.place(x=20, y=390)


button4 = Button(pencere)
button4.config(text="Ara", bg="white", fg="black", command=ara)
button4.place(x=180, y=420)

mainloop()