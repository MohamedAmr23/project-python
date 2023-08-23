from tkinter import *
from datetime import date
import sqlite3
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image,ImageTk
import os
from tkinter.ttk import Combobox
import passlib #encript password
root=Tk()
root.geometry('1366x786')
root.title("Gym")
#create database
db=sqlite3.connect('app.db')
#setting up cursor
cr=db.cursor()
#create database
#cr.execute("create TABLE if not exists manager1 (user_id integer auto increment,name text,age integer,email text,password integer,id integer)")
cr.execute("create TABLE if not exists manager2 (user_id integer auto increment,name text,age integer,email text,password integer,id integer auto increment)")
#insert into table
# cr.execute('insert into manager2(name,age,email,password,id) values("mohamed","35","amrm96754@gmail","123456789Mm@@","1")')
# cr.execute('insert into manager2(name,age,email,password,id) values("Ahmed","37","ahmed96754@gmail","472003Mm@@","2")')
#cr.execute('insert into manager2(name,age,email,password,id) values("mahmoud","40","mahmoud912354@gmail","85200389Mm@@","3")')
#cr.execute('insert into manager2(name,age,email,password,id) values("Amr","40","mahmoud912354@gmail","85200389Mm@@","5")')

#cr.execute('delete from manager2  where user_id=3')
db.commit()
######database of sign up######################
cr.execute("create TABLE if not exists signup (user_id integer auto increment,first name text,last name text,age integer,email text,password integer,country text)")

#root.mainloop()
