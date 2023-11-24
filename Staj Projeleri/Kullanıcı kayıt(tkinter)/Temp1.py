import tkinter
from tkinter import *
import sqlite3
import tkinter as tk
from tkinter import ttk

from tkinter import messagebox

from PIL import Image, ImageTk
from tkinter import filedialog as fd
import os

pencere = Tk()
pencere.geometry("1000x900")
canvas = Canvas(pencere, width=1000, height=800)
canvas.pack()


def ol():
    conn = sqlite3.connect('veri2.db')
    conn.execute(
        '''CREATE TABLE Tablo1(Nu INT PRIMARY KEY NOT NULL,ad CHAR(45),cins CHAR(6), bol CHAR(15), il CHAR(20),resim CHAR(255))''')
    messagebox.showinfo('Ana Başlık', 'Tablo Başarı ile oluşturuldu', parent=pencere)
    conn.close()


def fe():
    entry1.focus()


def cik():
    pencere.destroy()


def temiz():
    entry1.delete(0, 20)
    entry2.delete(0, 20)

    var.set(2)
    # entry3.delete(0,20)
    combo.delete(0, 20)
    entry5.delete(0, 20)
    entry6.delete(0, 20)
    entry7.delete(0, 20)
    combo.current(1)
    entry1.focus()
    canvas.delete("all")

    name = 'resim1.jpg'
    filename = name
    img = Image.open(filename)
    resized_img = img.resize((1, 1))
    pencere.photoimg = ImageTk.PhotoImage(resized_img)
    labelimage = tk.Label(pencere, image=pencere.photoimg).place(x=600, y=70)


def liste():
    canvas.delete("all")
    conn = sqlite3.connect('veri2.db')
    data = conn.execute('SELECT * FROM Tablo1 ')
    veriler = data.fetchall()
    canvas.create_text(70, 400, font="Times 16 italic bold", text="Nu")
    canvas.create_text(40 + 100, 400, font="Times 16 italic bold", text="Ad")
    canvas.create_text(30 + 200, 400, font="Times 16 italic bold", text="Cins")
    canvas.create_text(30 + 300, 400, font="Times 16 italic bold", text="Bolum")
    canvas.create_text(30 + 380, 400, font="Times 16 italic bold", text="il")
    canvas.create_text(10, 420,
                       text="       -------      --------------------------------  ---------------------------------------------------------------------------------------------------------------------")
    k = 0
    for a in veriler:
        canvas.create_text(70, 450 + k, font="Times 14 italic bold", text=a[0])
        canvas.create_text(140, 450 + k, font="Times 14 italic bold", text=a[1])
        canvas.create_text(230, 450 + k, font="Times 14 italic bold", text=a[2])
        canvas.create_text(330, 450 + k, font="Times 14 italic bold", text=a[3])
        canvas.create_text(430, 450 + k, font="Times 14 italic bold", text=a[4])
        k = k + 20

    conn.close()
    canvas.create_text(10, 450 + k,
                       text="       -------      --------------------------------  ---------------------------------------------------------------------------------------------------------------------")


def kliste():
    canvas.delete("all")
    bol = str(entry7.get())
    ili = str(entry6.get())
    temiz()
    conn = sqlite3.connect('veri2.db')
    data = conn.execute('SELECT * FROM Tablo1 where il like "%' + ili + '%" and  bol like "%' + bol + '%" ')

    # data = conn.execute('SELECT * FROM Tablo1 where il not like "%'+ili+'%" ')
    veriler = data.fetchall()
    canvas.create_text(70, 400, font="Times 16 italic bold", text="Nu.")
    canvas.create_text(40 + 100, 400, font="Times 16 italic bold", text="Adı Soyadı.")
    canvas.create_text(30 + 200, 400, font="Times 16 italic bold", text="Cins")
    canvas.create_text(30 + 300, 400, font="Times 16 italic bold", text="Bölüm.")
    canvas.create_text(30 + 380, 400, font="Times 16 italic bold", text="İli.")
    canvas.create_text(10, 420,
                       text="       -------      --------------------------------  ---------------------------------------------------------------------------------------------------------------------")
    k = 0
    for a in veriler:
        canvas.create_text(70, 450 + k, font="Times 14 italic bold", text=a[0])
        canvas.create_text(140, 450 + k, font="Times 14 italic bold", text=a[1])
        canvas.create_text(230, 450 + k, font="Times 14 italic bold", text=a[2])
        canvas.create_text(330, 450 + k, font="Times 14 italic bold", text=a[3])
        canvas.create_text(430, 450 + k, font="Times 14 italic bold", text=a[4])
        k = k + 20

    conn.close()
    canvas.create_text(10, 450 + k,
                       text="       -------      --------------------------------  ---------------------------------------------------------------------------------------------------------------------")


def kay():
    name = fd.askopenfilename()
    filename = name
    img = Image.open(filename)
    resized_img = img.resize((150, 150))
    pencere.photoimg = ImageTk.PhotoImage(resized_img)
    labelimage = tk.Label(pencere, image=pencere.photoimg).place(x=600, y=70)
    resim1 = name
    if var.get() == 2:
        cins = "Erkek"
    else:
        cins = "Kadın"

    numa = entry1.get()
    adsoy = entry2.get()
    # cins=entry3.get()
    bolum = combo.get()
    ili = entry5.get()

    conn = sqlite3.connect('veri2.db')
    conn.execute(
        "INSERT INTO Tablo1(Nu,ad,cins,bol,il,resim) VALUES ('" + numa + "','" + adsoy + "','" + cins + "','" + bolum + "','" + ili + "','" + resim1 + "' )")
    conn.commit()
    messagebox.showinfo('Ana Başlık', 'Kayıt Yapıldı', parent=pencere)
    conn.close()
    temiz()


def ara1():
    ad = str(entry2.get())
    il = str(entry5.get())
    num = str(entry2.get())
    conn = sqlite3.connect('veri1.db')
    # temiz()
    combo.delete(0, 20)
    # data = conn.execute('SELECT * FROM Tablo1 where ad like "%'+ad+'%" and il like "%'+il+'%" ')
    data = conn.execute('SELECT * FROM Tablo1 where nu like "%' + num + '%" ')
    veriler = data.fetchall()
    entry1.delete(0, 20)
    for a in veriler:
        entry1.insert(END, a[0])
        entry2.insert(END, a[1])
        if a[2] == "Kadın":
            var.set(1)
        else:
            var.set(2)

        combo.insert(END, a[3])
        entry5.insert(END, a[4])

    conn.close()


def ara():
    num = str(entry1.get())
    conn = sqlite3.connect('veri2.db')
    temiz()
    data = conn.execute('SELECT * FROM Tablo1 where nu  like "%' + num + '%" ')
    veriler = data.fetchall()
    entry1.delete(0, 20)
    combo.delete(0, 20)
    for a in veriler:
        entry1.insert(END, a[0])
        entry2.insert(END, a[1])
        if a[2] == "Kadın":
            var.set(1)
        else:
            var.set(2)
        combo.insert(END, a[3])
        entry5.insert(END, a[4])

        name = a[5]
        filename = name
        img = Image.open(filename)
        resized_img = img.resize((150, 150))
        pencere.photoimg = ImageTk.PhotoImage(resized_img)
        labelimage = tk.Label(pencere, image=pencere.photoimg).place(x=600, y=70)
    conn.close()


def sil():
    num = str(entry1.get())
    conn = sqlite3.connect('veri2.db')

    data = conn.execute('SELECT * FROM Tablo1 where nu like "%' + num + '%" ')
    veriler = data.fetchall()
    entry1.delete(0, 20)
    for a in veriler:
        for a in veriler:
            entry1.insert(END, a[0])
            entry2.insert(END, a[1])
            if a[2] == "Kadın":
                var.set(1)
            else:
                var.set(2)

            combo.insert(END, a[3])
            entry5.insert(END, a[4])
            name = a[5]
            filename = name
            img = Image.open(filename)
            resized_img = img.resize((150, 150))
            pencere.photoimg = ImageTk.PhotoImage(resized_img)
            labelimage = tk.Label(pencere, image=pencere.photoimg).place(x=600, y=70)

    conn.close()
    mem = messagebox.askyesno('Ana Başlık', 'Kayıt Silinsin mi', parent=pencere)
    if mem == True:
        num = str(entry1.get())
        conn = sqlite3.connect('veri2.db')
        data = conn.execute('DELETE FROM Tablo1 Where nu  like "%' + num + '%" ')
        conn.commit()
        messagebox.showinfo('Ana Başlık', 'Kayıt Başarı ile SİLİNDİ', parent=pencere)
        conn.close();
        entry1.delete(0, 20)
        entry2.delete(0, 20)

        entry5.delete(0, 20)
        entry1.focus()
        name = 'resim1.jpg'
        filename = name
        img = Image.open(filename)
        resized_img = img.resize((1, 1))
        pencere.photoimg = ImageTk.PhotoImage(resized_img)
        labelimage = tk.Label(pencere, image=pencere.photoimg).place(x=600, y=70)


def duz():
    mem = messagebox.askyesno('Ana Başlık', 'Kayıt Düzeltilsin mi', parent=pencere)
    if mem == True:
        if var.get() == 2:
            cins = "Erkek"
        else:
            cins = "Kadın"
        num = entry1.get()
        ad = entry2.get()
        # cins=entry3.get()
        bol = combo.get()
        il = entry5.get()
        conn = sqlite3.connect('veri2.db')
        mem = messagebox.askyesno('Ana Başlık', 'Resim düzeltilsin mi', parent=pencere)
        conn = sqlite3.connect('veri2.db')
        data = conn.execute('SELECT * FROM Tablo1 where nu like "%' + num + '%" ')
        veriler = data.fetchall()
        for a in veriler:
            name = a[5]
            resim1 = name

        if mem == True:
            name = fd.askopenfilename()
            filename = name
            img = Image.open(filename)
            resized_img = img.resize((150, 150))
            pencere.photoimg = ImageTk.PhotoImage(resized_img)
            labelimage = tk.Label(pencere, image=pencere.photoimg).place(x=600, y=70)
            resim1 = name

        data = conn.execute('''UPDATE Tablo1 SET ad = ?, cins = ?, bol = ?, il = ?, resim = ?  WHERE Nu = ?''',
                            (ad, cins, bol, il, resim1, num))
        conn.commit()
        messagebox.showinfo('Ana Başlık', 'Tablo Kayıt Başarı ile Düzeltildi ', parent=pencere)
        conn.close();
        entry1.delete(0, 20)
        entry2.delete(0, 20)

        var.set(2)
        # entry3.delete(0,20)
        combo.delete(0, 20)
        entry5.delete(0, 20)
        entry6.delete(0, 20)
        combo.current(0)
        entry1.focus()
        canvas.delete("all")
        name = 'resim1.jpg'
        filename = name
        img = Image.open(filename)
        resized_img = img.resize((1, 1))
        pencere.photoimg = ImageTk.PhotoImage(resized_img)
        labelimage = tk.Label(pencere, image=pencere.photoimg).place(x=600, y=70)


def resim():
    name = fd.askopenfilename()
    filename = name
    img = Image.open(filename)
    resized_img = img.resize((150, 150))
    pencere.photoimg = ImageTk.PhotoImage(resized_img)
    labelimage = tk.Label(pencere, image=pencere.photoimg).place(x=600, y=70)


label0 = Label(pencere)
label0.config(text="Kayıt Bilgileri", font=("Arial", 20))
label0.place(x=150, y=3)

label = Label(pencere)
label.config(text="Numarası  =", font=("Arial", 15))
label.place(x=20, y=35)

label1 = Label(pencere)
label1.config(text="Adı Soyadı=", font=("Arial", 15))
label1.place(x=20, y=80)

label2 = Label(pencere)
label2.config(text="Cinsiyet    =", font=("Arial", 15))
label2.place(x=20, y=140)

var = tk.IntVar()

R2 = tk.Radiobutton(pencere, text='Kadın', value=1, variable=var)
R1 = tk.Radiobutton(pencere, text='Erkek', value=2, variable=var)
R2.config(font=("Arial", 12))
R1.config(font=("Arial", 12))

R1.place(x=170, y=145)
R2.place(x=250, y=145)

var.set(2)
label3 = Label(pencere)
label3.config(text="Bölüm      =", font=("Arial", 15))
label3.place(x=20, y=200)

label4 = Label(pencere)
label4.config(text="İli             =", font=("Arial", 20))
label4.place(x=20, y=260)

label5 = Label(pencere)
label5.config(text="İl Ara=", font=("Arial", 10))
label5.place(x=650, y=320)

label6 = Label(pencere)
label6.config(text="Bölüm Ara=", font=("Arial", 10))
label6.place(x=650, y=370)

labelimage = tk.Label(pencere).place(x=600, y=70)

entry1 = Entry(pencere)
entry1.config(font=("Arial", 12))
entry1.place(x=170, y=40)
entry1.focus()

entry2 = Entry(pencere)
entry2.config(font=("Arial", 12))
entry2.place(x=170, y=85)

combo = ttk.Combobox(pencere)

combo['values'] = ("Bilgisayar", "Muhasebe", "Mat", "İşletme", "Makine", "Elektrik",)

combo.current(1)  # set the selected item
combo.place(x=170, y=205)
combo.config(font=("Arial", 12))

entry5 = Entry(pencere)
entry5.config(font=("Arial", 12,))
entry5.place(x=170, y=270)

entry6 = Entry(pencere)
entry6.config(font=("Arial", 12,))
entry6.place(x=690, y=320)

entry7 = Entry(pencere)
entry7.config(font=("Arial", 12,))
entry7.place(x=720, y=370)

buton0 = Button(pencere)
buton0.config(text="Oluştur", bg="white", fg="blue", command=ol)
buton0.place(x=30, y=320)

buton = Button(pencere)
buton.config(text="Kayıt", bg="white", fg="black", command=kay)
buton.place(x=98, y=320)

buton1 = Button(pencere)
buton1.config(text="Temizle", bg="white", fg="black", command=temiz)
buton1.place(x=160, y=320)

buton2 = Button(pencere)
buton2.config(text="Çıkış", bg="white", fg="black", command=cik)
buton2.place(x=240, y=320)

buton3 = Button(pencere)
buton3.config(text="Liste", bg="white", fg="black", command=liste)
buton3.place(x=320, y=320)

buton4 = Button(pencere)
buton4.config(text="Kliste", bg="white", fg="black", command=kliste)
buton4.place(x=380, y=320)

buton5 = Button(pencere)
buton5.config(text="Arama", bg="white", fg="black", command=ara)
buton5.place(x=440, y=320)

buton6 = Button(pencere)
buton6.config(text="Sil", bg="white", fg="black", command=sil)
buton6.place(x=500, y=320)

buton7 = Button(pencere)
buton7.config(text="Düzelt", bg="white", fg="black", command=duz)
buton7.place(x=550, y=320)

# buton8=Button(pencere)
# buton8.config(text="Resim Ekle",bg="white",fg="black",command=resim)
# buton8.place(x=630,y=220)

mainloop()


