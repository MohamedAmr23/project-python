from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image,ImageTk
import os
import re
from tkinter.ttk import Combobox
import passlib #encript password
def display_forget():
    root=Tk()
    root.geometry('1366x786')
    root.title("Gym")
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'#format email
    #function to email validation
    def valid_email():
        forget=emailforget.get()
        if len(forget)==0:
            messagebox.showerror('Error',"Enter your Email")
        if(re.fullmatch(regex, forget)):
            messagebox.showinfo('done',"You will recieve a massege now")
        elif len(forget)>0:
            forget="not"
            messagebox.showerror('Error',"Invalid Email")
            

    #backgroundimg
    lblbg=Label(root,width=1366,height=786,bg='#CAA928').place(x=0,y=0)
    #import labels

    logemail=Label(root,text='Enter your email',font=('',16,'bold'),bg='#CAA928',bd=0,fg='white').place(x=500,y=120)
    emailforget=StringVar()
    entryemaillog=Entry(root,textvariable=emailforget,width=23).place(x=700,y=123)


    send=Button(root,text='Send',width=19,height=2,font='arial 12 bold',bg='grey',command=valid_email).place(x=600,y=200)







    root.mainloop()
if __name__ == "__main__":
    display_forget()    