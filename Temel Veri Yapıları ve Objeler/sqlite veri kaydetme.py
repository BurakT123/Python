import tkinter as tk
from tkinter import *
import sqlite3

connection=sqlite3.connect("veritabanı.db")
cursor=connection.cursor()

table= "CREATE TABLE students('number','name','gender','section','location')"
cursor.execute(table)

data="INSERT INTO students(number ,name,gender,section,location)VALUES(7,'burak turhan','Erkek','Bilgisayar','Kocaeli')"
cursor.execute(data)

connection.commit()