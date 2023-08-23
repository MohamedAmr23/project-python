from tkinter import *
import sqlite3
import re
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image,ImageTk
import os
from tkinter.ttk import Combobox
import passlib #encript password
def display_signup():
    root=Tk()
    root.geometry('1366x786')
    root.title("Gym")
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'#format email
    #create database
    db=sqlite3.connect('app.db')
    #setting up cursor
    cr=db.cursor()
    def insert_data():
        firstname = fname.get()
        lastname=lname.get()
        try:
            g1=Gender
        except:
            messagebox.showerror("error",'select gender')  
        c=countryc.get() 
        a=age.get()
        e=email.get()
        p=password.get()
        ####validation of email
        if(re.fullmatch(regex, e)):
            pass 
        elif len(e)>0:
            e="not"
            messagebox.showerror('Error',"Invalid Email")
            
        #################validation of password
        if len(p)<=7 and len(p)>0:
            p="no"
            messagebox.showerror('Error',"minimum password length should greater than 7")
        elif not re.search("[a-z]", p) and len(p)>0:
            p="no"
            messagebox.showerror('Error'," password  should contain [a-z],[A-Z],[0-9],[_@$]")
        
        elif not re.search("[A-Z]", p) and len(p)>0:
            p="no"
            messagebox.showerror('Error'," password  should contain [a-z],[A-Z],[0-9],[_@$]")
            
        elif not re.search("[0-9]", p) and len(p)>0:
            p="no"
            messagebox.showerror('Error'," password  should contain [a-z],[A-Z],[0-9],[_@$]")
        
        elif not re.search("[_@$]" , p) and len(p)>0:
            p="no"
            messagebox.showerror('Error'," password  should contain [a-z],[A-Z],[0-9],[_@$]")


        if firstname=="" or lastname=="" or c=="Select Country" or a=="" or e=="" or p=="":
            messagebox.showerror('error','few data is missing')
        elif e=="not": #email
            pass
        elif p=="no": #password
            pass
        else:
            #cr.execute("INSERT INTO signup (first,last,age,email,password,country) VALUES (?,?,?,?,?,?)", (firstname,lastname,a,e,p,c))
            messagebox.showinfo('done','save successful') 
        db.commit()

    #function to delete data  
    #function to select gender
    def select():
        global Gender
        value=radio.get()
        if value==1:
            Gender='Male'
        
        else:
            Gender='Female' 
    #function to clear data
    def clear(): 
        fname.set('')
        lname.set('')
        radio.set('')    
        age.set('')    
        email.set('')
        password.set('')
        countryc.set('Select Option')      
    #function to exit window
    def exit():
        root.destroy() #Exit Window          
    #insert img of sign up
    sign_img=Image.open('imgs/sign2.jpg')
    sign_img_tk=ImageTk.PhotoImage(sign_img)
    btnsign=Button(root,image=sign_img_tk)
    btnsign.pack()
    #make sign up
    navsigb=LabelFrame(root,text='sign up',font=('',18,'bold'),fg='white',bd=2,bg='#131112',width=300,height=680,relief='groove')
    navsigb.place(x=220,y=20)
    #labels and enters
    lblsign1=Label(root,text='First Name',font=('',16,'bold'),bg='#131112',bd=0,fg='white').place(x=240,y=100)
    fname=StringVar()
    entrysign1=Entry(root,textvariable=fname,width=23).place(x=360,y=105)

    lblsign2=Label(root,text='Last Name',font=('',16,'bold'),bg='#131112',bd=0,fg='white').place(x=240,y=150)
    lname=StringVar()
    entrysign2=Entry(root,textvariable=lname,width=23).place(x=360,y=155)

    lblage=Label(root,text='age',font=('',16,'bold'),bg='#131112',bd=0,fg='white').place(x=240,y=200)
    age=StringVar()
    entryage=Entry(root,textvariable=age,width=23).place(x=360,y=205)

    lblgender=Label(root,text='Gender',font=('',16,'bold'),bg='#131112',bd=0,fg='white').place(x=240,y=250)
    radio=IntVar()
    rad1=Radiobutton(root,text='Male',variable=radio,value=1,bg='#131112',fg='#60656F',font=('',13,'bold'),command=select).place(x=340,y=252)
    rad1=Radiobutton(root,text='Female',variable=radio,value=2,bg='#131112',fg='#60656F',font=('',13,'bold'),command=select).place(x=405,y=252)

    lblemail=Label(root,text='Email',font=('',16,'bold'),bg='#131112',bd=0,fg='white').place(x=240,y=300)
    email=StringVar()
    entryemail=Entry(root,textvariable=email,width=23).place(x=360,y=300)

    lblpass=Label(root,text='Password',font=('',16,'bold'),bg='#131112',bd=0,fg='white').place(x=240,y=350)
    password=StringVar()
    entrypass=Entry(root,textvariable=password,width=23,show='*').place(x=360,y=350)

    country=Label(root,text='Country',font=('',16,'bold'),bg='#131112',bd=0,fg='white').place(x=240,y=400)
    countryc=Combobox(root,values=['Egypt','England','Germany','Morocco','Algeria','Palestine','Switzerland','America','Argentina','Brazil'],font='Roboto 10',state='r')
    countryc.place(x=350,y=400)
    countryc.set("Select Country")
    ######################database#######
    savebtn=Button(root,text='Save',width=19,height=2,font='arial 12 bold',bg='lightgreen',command=insert_data)
    savebtn.place(x=265,y=450)
    resetbtn=Button(root,text='Reset',width=19,height=2,font='arial 12 bold',bg='lightpink',command=clear).place(x=265,y=530)
    exitbtn=Button(root,text='Exit',width=19,height=2,font='arial 12 bold',bg='grey',command=exit).place(x=265,y=610)
######

    root.mainloop()


if __name__ == "__main__":
    display_signup()