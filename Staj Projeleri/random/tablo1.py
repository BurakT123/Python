import tkinter as tk
from tkinter import *
import sqlite3
conn = sqlite3.connect("../veritabanı.db")
imlec = conn.cursor()
yarat = "CREATE TABLE  Tablo1('Nu', 'Ad', 'Cins', 'Bolum', 'il')"
imlec.execute(yarat)
kaydet = "INSERT INTO Tablo1(Nu, Ad, Cins, Bolum, il) VALUES(7, 'Nuray Gül', 'Kadın', 'Elektrik', 'Van')"
imlec.execute(kaydet)
conn.commit()
