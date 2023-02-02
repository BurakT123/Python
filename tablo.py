import tkinter
from tkinter import *
import sqlite3
import tkinter as tk
import os
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog as fd

window = Tk()
window.geometry('1200x700')
window.title("Kullanıcı Kayıt Formu")

canvas = Canvas(window, width=1200, height=700)
canvas.pack()

labelFont = ("Arial", 15)


def create():
    connection = sqlite3.connect('veriler.db')
    try:
        connection.execute(
            '''CREATE TABLE users(id INT PRIMARY KEY NOT NULL, name CHAR(45), surname CHAR(45), age CHAR(45), gender CHAR(45), work CHAR(45))''')
        messagebox.showinfo('Bilgi', 'Kullanıcı veri tablosu oluşturuldu!', parent=window)
    except:
        messagebox.showerror('Uyarı', 'Kullanıcı veri tablosu daha önceden oluşturulmuş!', parent=window)
    connection.close()


def clear():
    id.delete(0, 100)
    name.delete(0, 100)
    surname.delete(0, 100)
    age.delete(0, 100)
    work.delete(0, 100)
    work.current(1)
    gender.set(3)
    canvas.delete("all")
    id.focus()


def save():
    _id = id.get()
    _name = name.get()
    _surname = surname.get()
    _age = age.get()
    _work = work.get()

    if gender.get() == 1:
        _gender = "Erkek"
    elif gender.get() == 2:
        _gender = "Kadın"

    connection = sqlite3.connect('veriler.db')
    connection.execute(
        "INSERT INTO users(id, name, surname, age, gender, work) VALUES ('" + _id + "','" + _name + "','" + _surname + "','" + _age + "','" + _gender + "','" + _work + "')")
    connection.commit()
    connection.close()

    messagebox.showinfo('Bilgi', 'Kullanıcı Kayıt Edildi!', parent=window)
    clear()


def infoText():
    canvas.create_text(50, 450, font="Times 12 italic bold", text="Kimliği")
    canvas.create_text(130, 450, font="Times 12 italic bold", text="Adı")
    canvas.create_text(210, 450, font="Times 12 italic bold", text="Soyadı")
    canvas.create_text(290, 450, font="Times 12 italic bold", text="Yaşı")
    canvas.create_text(370, 450, font="Times 12 italic bold", text="Cinsiyeti")
    canvas.create_text(450, 450, font="Times 12 italic bold", text="İşi")


def list():
    clear()
    connection = sqlite3.connect('veriler.db')
    datas = connection.execute('SELECT * FROM users')
    users = datas.fetchall()

    infoText()

    buttons = {}
    k = 0
    for user in users:
        canvas.create_text(50, 480 + k, font="Times 12", text=user[0])
        canvas.create_text(130, 480 + k, font="Times 12", text=user[1])
        canvas.create_text(210, 480 + k, font="Times 12", text=user[2])
        canvas.create_text(290, 480 + k, font="Times 12", text=user[3])
        canvas.create_text(370, 480 + k, font="Times 12 ", text=user[4])
        canvas.create_text(450, 480 + k, font="Times 12", text=user[5])

        action = lambda x=animal: text_update(x)

        buttons[user[0]] = Button(window)
        buttons[user[0]].config(text="Sil", bg="red", fg="black", command=lambda: userDelete(user[0]))
        buttons[user[0]].place(x=500, y=470 + k)

        k = k + 20

    connection.close()


def userDelete(id):
    print(id)


def searchWithId():
    _id = id.get()
    clear()
    try:
        connection = sqlite3.connect('veriler.db')
        data = connection.execute('SELECT * FROM users where id like "%' + _id + '%"')
        users = data.fetchall()
        k = 0
        for user in users:
            if user[0] == int(_id):
                infoText()
                canvas.create_text(50, 480 + k, font="Times 12", text=user[0])
                canvas.create_text(130, 480 + k, font="Times 12", text=user[1])
                canvas.create_text(210, 480 + k, font="Times 12", text=user[2])
                canvas.create_text(290, 480 + k, font="Times 12", text=user[3])
                canvas.create_text(370, 480 + k, font="Times 12 ", text=user[4])
                canvas.create_text(450, 480 + k, font="Times 12", text=user[5])
                k = k + 20
            else:
                messagebox.showerror('Hata', 'Kullanıcı bulunamadı!', parent=window)
    except:
        messagebox.showerror('Hata', 'Kullanıcı bulunamadı!', parent=window)
    connection.close()


def searchWithName():
    _name = name.get()
    clear()
    try:
        connection = sqlite3.connect('veriler.db')
        data = connection.execute('SELECT * FROM users where name like "%' + _name + '%"')
        users = data.fetchall()
        clear()
        k = 0
        for user in users:
            if user[1] == str(_name):
                infoText()
                canvas.create_text(50, 480 + k, font="Times 12", text=user[0])
                canvas.create_text(130, 480 + k, font="Times 12", text=user[1])
                canvas.create_text(210, 480 + k, font="Times 12", text=user[2])
                canvas.create_text(290, 480 + k, font="Times 12", text=user[3])
                canvas.create_text(370, 480 + k, font="Times 12 ", text=user[4])
                canvas.create_text(450, 480 + k, font="Times 12", text=user[5])
                k = k + 20
            else:
                messagebox.showerror('Hata', 'Kullanıcı bulunamadı!', parent=window)
    except:
        messagebox.showerror('Hata', 'Kullanıcı bulunamadı!', parent=window)
    connection.close()


def searchWithSurname():
    _surname = surname.get()
    clear()
    try:
        connection = sqlite3.connect('veriler.db')
        data = connection.execute('SELECT * FROM users where surname like "%' + _surname + '%"')
        users = data.fetchall()
        k = 0
        for user in users:
            if user[2] == str(_surname):
                infoText()
                canvas.create_text(50, 480 + k, font="Times 12", text=user[0])
                canvas.create_text(130, 480 + k, font="Times 12", text=user[1])
                canvas.create_text(210, 480 + k, font="Times 12", text=user[2])
                canvas.create_text(290, 480 + k, font="Times 12", text=user[3])
                canvas.create_text(370, 480 + k, font="Times 12 ", text=user[4])
                canvas.create_text(450, 480 + k, font="Times 12", text=user[5])
                k = k + 20
            else:
                messagebox.showerror('Hata', 'Kullanıcı bulunamadı!', parent=window)
    except:
        messagebox.showerror('Hata', 'Kullanıcı bulunamadı!', parent=window)
    connection.close()


def searchWithAge():
    _age = age.get()
    clear()
    try:
        connection = sqlite3.connect('veriler.db')
        data = connection.execute('SELECT * FROM users where age like "%' + _age + '%"')
        users = data.fetchall()
        k = 0
        for user in users:
            if int(user[3]) == int(_age):
                infoText()
                canvas.create_text(50, 480 + k, font="Times 12", text=user[0])
                canvas.create_text(130, 480 + k, font="Times 12", text=user[1])
                canvas.create_text(210, 480 + k, font="Times 12", text=user[2])
                canvas.create_text(290, 480 + k, font="Times 12", text=user[3])
                canvas.create_text(370, 480 + k, font="Times 12 ", text=user[4])
                canvas.create_text(450, 480 + k, font="Times 12", text=user[5])
                k = k + 20
            else:
                messagebox.showerror('Hata', 'Kullanıcı bulunamadı!', parent=window)
    except:
        messagebox.showerror('Hata', 'Kullanıcı bulunamadı!', parent=window)
    connection.close()


def searchWithGender():
    if gender.get() == 1:
        _gender = "Erkek"
    elif gender.get() == 2:
        _gender = "Kadın"
    clear()
    try:
        connection = sqlite3.connect('veriler.db')
        data = connection.execute('SELECT * FROM users where gender like "%' + _gender + '%"')
        users = data.fetchall()
        k = 0
        for user in users:
            if user[4] == _gender:
                infoText()
                canvas.create_text(50, 480 + k, font="Times 12", text=user[0])
                canvas.create_text(130, 480 + k, font="Times 12", text=user[1])
                canvas.create_text(210, 480 + k, font="Times 12", text=user[2])
                canvas.create_text(290, 480 + k, font="Times 12", text=user[3])
                canvas.create_text(370, 480 + k, font="Times 12 ", text=user[4])
                canvas.create_text(450, 480 + k, font="Times 12", text=user[5])
                k = k + 20
            else:
                messagebox.showerror('Hata', 'Kullanıcı bulunamadı!', parent=window)
    except:
        messagebox.showerror('Hata', 'Kullanıcı bulunamadı!', parent=window)
    connection.close()


def searchWithWork():
    _work = work.get()
    clear()
    try:
        connection = sqlite3.connect('veriler.db')
        data = connection.execute('SELECT * FROM users where work like "%' + _work + '%"')
        users = data.fetchall()
        k = 0
        for user in users:
            if user[5] == str(_work):
                infoText()
                canvas.create_text(50, 480 + k, font="Times 12", text=user[0])
                canvas.create_text(130, 480 + k, font="Times 12", text=user[1])
                canvas.create_text(210, 480 + k, font="Times 12", text=user[2])
                canvas.create_text(290, 480 + k, font="Times 12", text=user[3])
                canvas.create_text(370, 480 + k, font="Times 12 ", text=user[4])
                canvas.create_text(450, 480 + k, font="Times 12", text=user[5])
                k = k + 20
            else:
                messagebox.showerror('Hata', 'Kullanıcı bulunamadı!', parent=window)
    except:
        messagebox.showerror('Hata', 'Kullanıcı bulunamadı!', parent=window)
    connection.close()


def delete():
    num = str(entry1.get())
    connection = sqlite3.connect('veriler.db')

    data = connection.execute('SELECT * FROM users where nu like "%' + num + '%" ')
    veriler = data.fetchall()
    entry1.delete(0, 20)
    for a in veriler:
        for a in veriler:
            entry1.insert(END, a[0])
            entry2.insert(END, a[1])
            if a[2] == "Kadın":
                gender.set(1)
            else:
                gender.set(2)

            combo.insert(END, a[3])
            entry5.insert(END, a[4])
            name = a[5]
            filename = name
            img = Image.open(filename)
            resized_img = img.resize((150, 150))
            window.photoimg = ImageTk.PhotoImage(resized_img)
            labelimage = tk.Label(
                window, image=window.photoimg).place(x=600, y=70)

    connection.close()
    mem = messagebox.askyesno('Ana Başlık', 'Kayıt Silinsin mi', parent=window)
    if mem == True:
        num = str(entry1.get())
        connection = sqlite3.connect('veriler.db')
        data = connection.execute('DELETE FROM users Where nu  like "%' + num + '%" ')
        connection.commit()
        messagebox.showinfo(
            'Ana Başlık', 'Kayıt Başarı ile SİLİNDİ', parent=window)
        connection.close()
        entry1.delete(0, 20)
        entry2.delete(0, 20)

        entry5.delete(0, 20)
        entry1.focus()
        name = 'resim1.jpg'
        filename = name
        img = Image.open(filename)
        resized_img = img.resize((1, 1))
        window.photoimg = ImageTk.PhotoImage(resized_img)
        labelimage = tk.Label(window, image=window.photoimg).place(x=600, y=70)


def fix():
    mem = messagebox.askyesno(
        'Ana Başlık', 'Kayıt Düzeltilsin mi', parent=window)
    if mem == True:
        if gender.get() == 2:
            cins = "Erkek"
        else:
            cins = "Kadın"
        num = entry1.get()
        ad = entry2.get()
        # cins=entry3.get()
        bol = combo.get()
        il = entry5.get()
        connection = sqlite3.connect('veriler.db')
        mem = messagebox.askyesno(
            'Ana Başlık', 'Resim düzeltilsin mi', parent=window)
        connection = sqlite3.connect('veriler.db')
        data = connection.execute('SELECT * FROM users where nu like "%' + num + '%" ')
        veriler = data.fetchall()
        for a in veriler:
            name = a[5]
            resim1 = name

        if mem == True:
            name = fd.askopenfilename()
            filename = name
            img = Image.open(filename)
            resized_img = img.resize((150, 150))
            window.photoimg = ImageTk.PhotoImage(resized_img)
            labelimage = tk.Label(
                window, image=window.photoimg).place(x=600, y=70)
            resim1 = name

        data = connection.execute(
            '''UPDATE users SET ad = ?, cins = ?, bol = ?, il = ?, resim = ?  WHERE Nu = ?''',
            (ad, cins, bol, il, resim1, num))
        connection.commit()
        messagebox.showinfo(
            'Ana Başlık', 'Tablo Kayıt Başarı ile Düzeltildi ', parent=window)
        connection.close()
        entry1.delete(0, 20)
        entry2.delete(0, 20)

        gender.set(2)
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
        window.photoimg = ImageTk.PhotoImage(resized_img)
        labelimage = tk.Label(window, image=window.photoimg).place(x=600, y=70)


title = Label(window)
title.config(text="Kullanıcı Bilgileri", font=("Arial", 20))
title.place(x=150, y=50)

idLabel = Label(window)
idLabel.config(text="Kimlik:", font=labelFont)
idLabel.place(x=30, y=100)

id = Entry(window)
id.config(font=("Arial", 12))
id.place(x=150, y=100)
id.focus()

searchIdButton = Button(window)
searchIdButton.config(text="Bul", bg="orange", fg="black", command=searchWithId)
searchIdButton.place(x=350, y=100)

nameLabel = Label(window)
nameLabel.config(text="Adı:", font=labelFont)
nameLabel.place(x=30, y=150)

name = Entry(window)
name.config(font=("Arial", 12))
name.place(x=150, y=150)

searchNameButton = Button(window)
searchNameButton.config(text="Bul", bg="orange", fg="black", command=searchWithName)
searchNameButton.place(x=350, y=150)

surnameLabel = Label(window)
surnameLabel.config(text="Soyadı:", font=labelFont)
surnameLabel.place(x=30, y=200)

surname = Entry(window)
surname.config(font=("Arial", 12))
surname.place(x=150, y=200)

searchSurnameButton = Button(window)
searchSurnameButton.config(text="Bul", bg="orange", fg="black", command=searchWithSurname)
searchSurnameButton.place(x=350, y=200)

ageLabel = Label(window)
ageLabel.config(text="Yaşı:", font=labelFont)
ageLabel.place(x=30, y=250)

age = Entry(window)
age.config(font=("Arial", 12))
age.place(x=150, y=250)

searchAgeButton = Button(window)
searchAgeButton.config(text="Bul", bg="orange", fg="black", command=searchWithAge)
searchAgeButton.place(x=350, y=250)

genderLabel = Label(window)
genderLabel.config(text="Cinsiyeti:", font=labelFont)
genderLabel.place(x=30, y=300)

gender = tk.IntVar()

genderM = tk.Radiobutton(window, text='Erkek', value=1, variable=gender)
genderM.config(font=("Arial", 12))
genderM.place(x=150, y=300)

genderW = tk.Radiobutton(window, text='Kadın', value=2, variable=gender)
genderW.config(font=("Arial", 12))
genderW.place(x=250, y=300)

gender.set(1)

searchGenderButton = Button(window)
searchGenderButton.config(text="Bul", bg="orange", fg="black", command=searchWithGender)
searchGenderButton.place(x=350, y=300)

workLabel = Label(window)
workLabel.config(text="İşi:", font=labelFont)
workLabel.place(x=30, y=350)

work = ttk.Combobox(window)
work.config(font=("Arial", 12), width=15)
work.place(x=150, y=350)
work['values'] = ("İşsiz", "Mühendis", "Mimar", "Öğretmen", "Memur", "Çiftçi", "İşci", "Emekli")
work.current(1)

searchWorkButton = Button(window)
searchWorkButton.config(text="Bul", bg="orange", fg="black", command=searchWithWork)
searchWorkButton.place(x=350, y=350)

createButton = Button(window)
createButton.config(text="Veri Tablosunu Oluştur", bg="blue", fg="black", command=create)
createButton.place(x=30, y=400)

saveButon = Button(window)
saveButon.config(text="Kullanıcıyı Kayıt Et", bg="green", fg="black", command=save)
saveButon.place(x=200, y=400)

clearButton = Button(window)
clearButton.config(text="Temizle", bg="pink", fg="black", command=clear)
clearButton.place(x=350, y=400)

listButton = Button(window)
listButton.config(text="Listele", bg="red", fg="black", command=list)
listButton.place(x=420, y=400)

fixButton = Button(window)
fixButton.config(text="Düzelt", bg="white", fg="black", command=fix)
fixButton.place(x=650, y=400)

mainloop()