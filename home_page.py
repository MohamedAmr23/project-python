from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image,ImageTk
import os
from tkinter.ttk import Combobox
import passlib #encript password


def display_home():
    import about_frame
    import moibrahim
    import sub
    def toabout():
        root.destroy()
        about_frame.fromabout()
    def toibrahim():
        root.destroy()
        moibrahim.frommoibrahim()
    def totarek():
        root.destroy()
        sub.fromtarek()


    root=Tk()
    root.geometry('1366x786')
    root.title("Gym")
    #insert main picture
    mainimg=Image.open('imgs/mainimg.jpg')
    mainimg_tk=ImageTk.PhotoImage(mainimg)
    btn=Button(root,compound='left',image=mainimg_tk)
    btn.place(x=0,y=0)

    #right side
    lblri=Label(root,bg='#CAA928',height=776,width=146)
    lblri.place(x=1200,y=0)
    lblri1=Label(root,text='Golds Gym',font=("Times", "24", "bold italic"),fg='white',bd=0,bg='#CAA928')
    lblri1.place(x=1210,y=150)

    #insert logo img
    logoimg=Image.open('imgs/logoresize.png')
    logoimg_tk=ImageTk.PhotoImage(logoimg)
    btnlogo=Button(root,compound='right',image=logoimg_tk,bd=0,bg='#CAA928')#,width=150,height=150
    btnlogo.place(x=1220,y=250)

    #features of gold gym
    lblfea=Label(root,text='Group Exercise',bg='#CAA928',fg='white',font=('',"13", "bold"))
    lblfea.place(x=1220,y=400)

    lblfea1=Label(root,text='Personal Training',bg='#CAA928',fg='white',font=('',"13", "bold"))
    lblfea1.place(x=1220,y=440)

    lblfea2=Label(root,text='Pools',bg='#CAA928',fg='white',font=('',"13", "bold"))
    lblfea2.place(x=1225,y=480)

    lblfea3=Label(root,text='Cardio Equipment',bg='#CAA928',fg='white',font=('',"13", "bold"))
    lblfea3.place(x=1218,y=520)

    lblfea3=Label(root,text='Cardio Cinema',bg='#CAA928',fg='white',font=('',"13", "bold"))
    lblfea3.place(x=1220,y=560)

    lblfea3=Label(root,text='Free Weights.',bg='#CAA928',fg='white',font=('',"13", "bold"))
    lblfea3.place(x=1224,y=600)

    lblfea3=Label(root,text='Group Cycle.',bg='#CAA928',fg='white',font=('',"13", "bold"))
    lblfea3.place(x=1224,y=640)

    #create navigator
    nav=LabelFrame(root,text='Navigator',font=20,bg='#CAA928',fg='white',bd=2,width=1366,height=100,relief='groove')
    nav.place(x=0,y=0)
    #create buttons
    home_img=PhotoImage(file='imgs/home.png')
    home_nav=Button(root,text='Home',compound='left',highlightcolor='black',image=home_img,fg='#43380D',bg='#CAA928',font=('',"13", "bold"),bd=0,padx=8,pady=8)
    home_nav.place(x=50,y=33)

    gym1_img=PhotoImage(file='imgs/buy.png')
    btn1_nav=Button(root,text='buy products',compound='left',highlightcolor='black',image=gym1_img,fg='white',bg='#CAA928',font=('',"13", "bold"),bd=0,padx=8,pady=8)
    btn1_nav.place(x=1050,y=33)

    gym2_img=PhotoImage(file='imgs/add.png')
    btn2_nav=Button(root,text='Add a new package',compound='left',image=gym2_img,fg='white',bg='#CAA928',font=('',"13", "bold"),bd=0,padx=3,pady=8,command=totarek)
    btn2_nav.place(x=595,y=33)

    gym3_img=PhotoImage(file='imgs/services.png')
    btn3_nav=Button(root,text='Subscribers services',compound='left',image=gym3_img,fg='white',bg='#CAA928',font=('',"13", "bold"),bd=0,padx=8,pady=8,command=toibrahim)
    btn3_nav.place(x=350,y=33)

    gym4_img=PhotoImage(file='imgs/about.png')
    btn4_nav=Button(root,text='About',compound='left',image=gym4_img,fg='white',bg='#CAA928',font=('',"13", "bold"),bd=0,padx=8,pady=8,command=toabout)
    btn4_nav.place(x=850,y=33)

    # gym5_img=PhotoImage(file='imgs/gym5.png')
    # btn5_nav=Button(root,text='Sports Sets',compound='left',image=gym5_img,fg='white',bg='#CAA928',font=('',"13", "bold"),bd=0,padx=8,pady=8)
    # btn5_nav.place(x=1150,y=33)

    # #button login
    # login_img=PhotoImage(file='imgs/login.png')
    # login_nav=Button(root,text='Login',compound='left',image=login_img,fg='white',bg='#C7B590',font=('',"13", "bold"),bd=0,padx=8,pady=8)
    # login_nav.place(x=1140,y=33)

    # #button sign up
    # sign_img=PhotoImage(file='imgs/sign up.png')
    # sign_nav=Button(root,text='Sign Up',compound='left',image=sign_img,fg='white',bg='#C7B590',font=('',"13", "bold"),bd=0,padx=8,pady=8)
    # sign_nav.place(x=1240,y=33)

    #button profile
    # profile_img=PhotoImage(file='imgs/profile.png')
    # btn6_nav=Button(root,text='My Profile',compound='left',image=profile_img,fg='white',bg='#C7B590',font=18,bd=0,padx=8,pady=8)
    # btn6_nav.place(x=10,y=400)
    root.mainloop()

if __name__ == "__main__":
    display_home()