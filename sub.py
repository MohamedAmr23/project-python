from tkinter import *
import tkinter
from tkinter.ttk import *
from tkinter import ttk
from PIL import ImageTk,Image
import sqlite3
def fromtarek():

    root=Tk()
    root.title("subscribers")


    w=1200
    h=600
    x=100
    y=50

    root.geometry(f"{w}x{h}+{x}+{y}")

    img=Image.open("img/gym.jpg")
    img=img.resize((1200,600))
    img_tk=ImageTk.PhotoImage(img)
    imglbl=tkinter.Label(root,image=img_tk)
    imglbl.place(x=0,y=0,relwidth=1,relheight=1)


    #-----------------------------------------------------------------------
    conn=sqlite3.connect('app1.dp')
    cur=conn.cursor()

    #-----------------------------------------------------------------------
    def submit():
        conn=sqlite3.connect('app1.dp')
        cur=conn.cursor()
        choice=v2_rbtn.get()
        if choice==1:
            tex="monthly"
        else:
            tex="premium"
            
        def exit():
            root.destroy()

        cur.execute("INSERT INTO subscribers VALUES(:id, :name, :age, :joindate, :subtype, :fees, :days, :packagesub)",
                    
                    {
                        'id':int(en1.get()),
                        'name':en2.get(),
                        'age':int(en3.get()),
                        'joindate':en4.get(),
                        'subtype':tex,
                        'fees':int(en7.get()),
                        'days':float(en5.get()),
                        'packagesub':int(combo3.get())
                    })
        
        conn.commit()
        conn.close()
        
        en1.delete(0,END)
        en2.delete(0,END)
        en3.delete(0,END)
        en4.delete(0,END)
        en5.delete(0,END)
        en7.delete(0,END)
    #----------------------------------------------------------------------

    #-----------------------------------------------------------------------
    f1=tkinter.Frame(root,bg="#4E4FEB")
    f2=tkinter.Frame(root,bg="#4E4FEB")
    f3=tkinter.Frame(root)

    #-----------------------------------------------------------------------

    lb1=Label(f1,text='ID:',font=('arial',12,'bold'),background="#4E4FEB")
    lb2=Label(f1,text='Name:',font=('arial',12,'bold'),background="#4E4FEB")
    lb3=Label(f1,text='Age:',font=('arial',12,'bold'),background="#4E4FEB")
    lb4=Label(f1,text='Join date:',font=('arial',12,'bold'),background="#4E4FEB")
    lb5=Label(f2,text='Fees:',font=('arial',12,'bold'),background="#4E4FEB")
    lb6=Label(f2,text='Package num:',font=('arial',12,'bold'),background="#4E4FEB")
    lb7=Label(f2,text='Days:',font=('arial',12,'bold'),background="#4E4FEB")

    en1=Entry(f1)
    en2=Entry(f1)
    en3=Entry(f1)
    en4=Entry(f1)
    en5=Entry(f2)
    en7=Entry(f2)


    #btn1=tkinter.Button(f3,text='View',font=('arial',12,'bold'),padx=150,pady=20,command=view_subscribers)
    #btn1.grid(row=0,column=4)

    btn2=tkinter.Button(f3,text='Add',font=('arial',20,'bold'),bg="#FFC436",fg="black",padx=150,pady=20,command=submit)
    btn2.grid(row=0,column=3)

    btn3=tkinter.Button(f3,text='Exit',font=('arial',20,'bold'),bg="#FFC436",fg="black",padx=150,pady=20,command=exit)
    btn3.grid(row=0,column=5)

    lb1.grid(row=0,column=1)
    lb2.grid(row=1,column=1)
    lb3.grid(row=2,column=1)
    lb4.grid(row=3,column=1)
    #v1_rbtn=IntVar()
    #v1_rbtn.set(1)
    #rbtn1=Radiobutton(root,text='male',value=1,variable=v1_rbtn)
    #rbtn2=Radiobutton(root,text='female',value=2,variable=v1_rbtn)


    en1.grid(row=0,column=2,padx=70,pady=20)
    en2.grid(row=1,column=2,padx=70,pady=20)
    en3.grid(row=2,column=2,padx=70,pady=20)
    en4.grid(row=3,column=2,padx=70,pady=20)

    #f1.grid(row=5,column=2,pady=100)
    f1.place(anchor='e',relx=0.4,rely=0.5)


    #f3.place(anchor='s',relx=0.5,rely=0.5)

    f3.pack(side='bottom',padx=80,pady=40)

    lb5.grid(row=4,column=6,padx=40,pady=20)
    lb6.grid(row=1,column=6,padx=40,pady=20)
    lb7.grid(row=2,column=6,padx=40,pady=20)


    en5.grid(row=2,column=7,padx=40,pady=20)
    en7.grid(row=4,column=7,padx=40,pady=20)


    v2_rbtn=IntVar()
    v2_rbtn.set(1)


    #sub type
    rbtn3=Radiobutton(f2,text='monthly',value=1,variable=v2_rbtn)
    rbtn4=Radiobutton(f2,text='premium',value=2,variable=v2_rbtn)

    rbtn3.grid(row=0,column=6,padx=20,pady=20)
    rbtn4.grid(row=0,column=7)


    package_days=[0,1,2,3]

    p_var=IntVar()
    p_var.set(package_days[0])
    combo3=Combobox(f2,values=package_days,state='readonly',textvariable=p_var)
    combo3.grid(row=1,column=7,padx=5,pady=20)
    #------------------------------------------------------------------------




    #f2.grid(row=5,column=7,pady=100)
    f2.place(anchor='w',relx=0.6,rely=0.5)

    #-------------------------------------------------------------------------



    #--------------------------------------------------------------------------
    conn.commit()
    conn.close()
    root.mainloop()
if __name__ == "__main__":
    fromtarek()