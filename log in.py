from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image,ImageTk
import os
from tkinter.ttk import Combobox
import passlib #encript password
import re
import sqlite3
import home_page
import signup
import forgetpassword
root=Tk()
root.geometry('1366x786')
root.title("Gym")
################create database login##################
#create database
dblogin=sqlite3.connect('log.db')
#setting up cursor
cr=dblogin.cursor()
cr.execute("CREATE TABLE  if not exists login(email text,password TEXT ,id integer auto increment)")
#insert into database login
#cr.execute("insert into login(email,password,id) values('mohamed@gmail.com,'1234566Mm@','1')")
def login():
    em=emaillog.get()
    #password=passwordlog.get()
    if em=="":
        messagebox.showerror("error","Enter Your Email")
    if(re.fullmatch(regex, em)):
        pass
        #messagebox.showinfo('valid',' Valid Email')  
 
    elif len(em)>0:
         messagebox.showerror('Error',"Invalid Email")
#check for password
    respass=passwordlog.get()
    if respass=="":
        p="m"
        messagebox.showerror("error","Enter Your Password")
    if len(respass)<=7 and len(respass)>0:
         p="m"
         messagebox.showerror('Error',"minimum password length should greater than 7")
    elif not re.search("[a-z]", respass) and len(respass)>0:
       p="m"
       messagebox.showerror('Error'," password  should contain [a-z],[A-Z],[0-9],[_@$]")
    elif not re.search("[A-Z]", respass) and len(respass)>0:
        p="m"
        messagebox.showerror('Error'," password  should contain [a-z],[A-Z],[0-9],[_@$]")
        
    elif not re.search("[0-9]", respass) and len(respass)>0:
       p="m"
       messagebox.showerror('Error'," password  should contain [a-z],[A-Z],[0-9],[_@$]")
      
    elif not re.search("[_@$]" , respass) and len(respass)>0:
        p="m"
        messagebox.showerror('Error'," password  should contain [a-z],[A-Z],[0-9],[_@$]")
        
    cursor=dblogin.cursor()
    cursor.execute("select email , password from login")
    data = cursor.fetchall()
    for rows in data :
        if respass == rows[1] and em == rows[0]:
            root.destroy()
            home_page.display_home()
        if respass!= rows[1] and len(respass)>=8 and re.search("[_@$]" , respass) and re.search("[0-9]", respass) and  re.search("[A-Z]", respass):
            messagebox.showerror('Error',"don't have account sign up")    
    ################forgetpassword############



#function to move to sign up    
def move():
    root.destroy()
    signup.display_signup()
#function to forget password
def to_forget():
    root.destroy()
    forgetpassword.display_forget()

#insert log in img
login_img=Image.open('imgs/log in.jpg')
login_img_tk=ImageTk.PhotoImage(login_img)
btnimg=Button(root,image=login_img_tk).place(x=0,y=0)
#############################################################
#make log in
navlog=LabelFrame(root,text='log in',font=('',18,'bold'),fg='white',bd=2,bg='#F86F03',width=340,height=768,relief='groove')
navlog.place(x=1010,y=5)
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
#function to validation email
def email():
    resemail=emaillog.get()
    if resemail=="":
        messagebox.showerror("error","Enter Your Email")
    if(re.fullmatch(regex, resemail)):
        pass
        #messagebox.showinfo('valid',' Valid Email')  
 
    elif len(resemail)>0:
         messagebox.showerror('Error',"Invalid Email")
#check for password
    respass=passwordlog.get()
    if respass=="":
        messagebox.showerror("error","Enter Your Password")
    if len(respass)<=7 and len(respass)>0:
         messagebox.showerror('Error',"minimum password length should greater than 7")
    elif not re.search("[a-z]", respass) and len(respass)>0:
       messagebox.showerror('Error'," password  should contain [a-z],[A-Z],[0-9],[_@$]")
       
    elif not re.search("[A-Z]", respass) and len(respass)>0:
        messagebox.showerror('Error'," password  should contain [a-z],[A-Z],[0-9],[_@$]")
        
    elif not re.search("[0-9]", respass) and len(respass)>0:
       messagebox.showerror('Error'," password  should contain [a-z],[A-Z],[0-9],[_@$]")
      
    elif not re.search("[_@$]" , respass) and len(respass)>0:
        messagebox.showerror('Error'," password  should contain [a-z],[A-Z],[0-9],[_@$]")
        
   
           
    
#labels and enters
logwelcome=Label(root,text='Welcome Back',font=('',16,'bold'),bg='#F86F03',bd=0,fg='white').place(x=1100,y=50)


logemail=Label(root,text='Email',font=('',16,'bold'),bg='#F86F03',bd=0,fg='white').place(x=1070,y=120)
emaillog=StringVar()
entryemaillog=Entry(root,textvariable=emaillog,width=23).place(x=1160,y=123)



logpass=Label(root,text='Password',font=('',16,'bold'),bg='#F86F03',bd=0,fg='white').place(x=1050,y=190)
passwordlog=StringVar()
entrypasslog=Entry(root,textvariable=passwordlog,width=23,show='*').place(x=1160,y=190)

forgetpass=Button(root,text="Forget Password?",bg='#F86F03',fg='white',font=('',12,'bold'),command=to_forget).place(x=1120,y=250)

#button login
login_img=PhotoImage(file='imgs/login.png')
login_nav=Button(root,text='Login',compound='left',image=login_img,fg='white',bg='#C7B590',font=('',"13", "bold"),bd=0,padx=8,pady=8,command=login)
login_nav.place(x=1140,y=300)

notacc=Label(root,text='Don\'t have account ',font=('',12,'bold'),bg='#F86F03',bd=0,fg='white').place(x=1115,y=360)


#button sign up
sign_img=PhotoImage(file='imgs/sign up.png')
sign_nav=Button(root,text='Sign Up',compound='left',image=sign_img,fg='white',bg='#C7B590',font=('',"13", "bold"),bd=0,padx=8,pady=8,command=move)
sign_nav.place(x=1135,y=400)
# def back():
#     import home_page
#     a=home_page.root.mainloop()
#     print(a)
# btn=Button(root,text='home',command=back).place(x=10,y=10)
root.mainloop()