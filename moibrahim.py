from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
import sqlite3
from tkinter import simpledialog
from PIL import ImageTk,Image
import home_page

def frommoibrahim():

    # import mysql.connector
    # import PIL
    # from PIL import Image, ImageTk


    # setting up the connection
    Mydb = sqlite3.connect("app1.dp")
    cursor = Mydb.cursor()


    # Creating a Database For Testing


    cursor.execute("create table if not exists subscribers (id integer, name text, age integer, joindate date, subtype text, fees float, days integer, packagesub integer)")
    cursor.execute("insert into subscribers (id , name, age, joindate, subtype , fees, days, packagesub) values(2,'ahmed', 40, 2008-11-11, 'premium', 2000, 200, 2)")
    Mydb.commit()


    # this Fuction made to present data on the treeview


    def update_func(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert('', 'end', values=i)


    # this function made to search the Data base based on the name


    def search_func():
        q2 = q.get()
        query = "SELECT id , name, age, joindate, subtype , fees, days, packagesub FROM subscribers WHERE name like '%"+q2+"%'"
        cursor.execute(query)
        rows = cursor.fetchall()
        update_func(rows)


    # this function made to refresh the tabel afte every update, search or delete


    def clear_func():
        query = "SELECT id , name, age, joindate, subtype, fees, days, packagesub FROM subscribers"
        cursor.execute(query)
        rows = cursor.fetchall()
        update_func(rows)


    # this function is event driven <double click> to present data in the entry box for modification


    def getrow(event):
        rowid = trv.identify_row(event.y)
        item = trv.item(trv.focus())
        t1.set(item['values'][0])
        t2.set(item['values'][1])
        t3.set(item['values'][7])
        t4.set(item['values'][6])


    # this function is made for updating the remaining days of the subscribers


    def update_customer():
        days = t4.get()
        id = t1.get()
        Mydb = sqlite3.connect("app1.dp")
        cursor = Mydb.cursor()
        if messagebox.askyesno(" Confirm update", "Are you sure you want to update the days?"):
            query = "update subscribers SET days = ? where id = ?"
            cursor.execute(query, (days, id))
            Mydb.commit()
            clear_func()
        else:
            return True

    # this function is made to cancel the subscribtion


    def delete_customer():
        id = t1.get()
        package_number = t3.get()
        days = t4.get()
        Mydb = sqlite3.connect("app1.dp")
        cursor = Mydb.cursor()
        if messagebox.askyesno(" Confirm Deleteion", "Are you sure you want to delete this user?"):
            query = "delete from subscribers where id = ?"
            cursor.execute(query, (id))
            Mydb.commit()
            clear_func()

            if package_number == "1" or package_number == "2" or package_number == "3":
                if package_number == "1":
                    remaining = ((200 - int(days)) / 200) * 250
                    messagebox.showinfo(
                        "Change", f"The customer should recive: {remaining} as a change for canceling")
                    print(package_number+"11")
                elif package_number == "2":
                    remaining = ((500 - int(days)) / 500) * 625
                    messagebox.showinfo(
                        "Change", f"The customer should recive: {remaining} as a change for canceling")
                    print(package_number+"22")
                elif package_number == "3":
                    remaining = ((700 - int(days)) / 700) * 930
                    messagebox.showinfo(
                        "Change", f"The customer should recive: {remaining} as a change for canceling")
                    print(package_number+"33")
        else:
            return True

    # this function is made to reward a certain package subscribers with additonal days


    def reward():
        increase_days = simpledialog.askinteger(
            "reward days", "enter the number of days to reward")
        package_num = simpledialog.askinteger(
            "rewarde package", "enter the number of the package rewarded")
        if messagebox.askyesno(" Confirm update", "Are you sure you want to increase the days?"):
            query = "update subscribers SET days = days + ? where packagesub = ?"
            cursor.execute(query, (increase_days, package_num))
            Mydb.commit()
            clear_func()
        else:
            return True

    # exit to home page function


    def exit_func():
        subscribers.destroy()
        home_page.display_home()



    # # img = Image.open('C:\coding\Screenshot (171).png')
    # # img_tk = ImageTk.PhotoImage(img)
    # # img.show()
    # bg = ImageTk.PhotoImage(file="C:\coding\Screenshot (171).png")
    # label1 = Label(subscribers, image=bg)
    # label1.place(x=0, y=0)


    subscribers = Tk()  # the form
    q = StringVar()  # made for use in search function
    t1, t2, t3, t4 = StringVar(), StringVar(), StringVar(), StringVar()












    subscribers.title('Subscribers Modifications')
    screenwidth = subscribers.winfo_screenwidth()
    screenheight = subscribers.winfo_screenheight()
    subscribers.geometry(f'{screenwidth}x{screenheight}+0+0')


    #-----------------------------------------------------------------------------

    img=Image.open("img/iiiiii.png")
    img=img.resize((screenwidth,screenheight))
    img_tk=ImageTk.PhotoImage(img)
    imglbl=Label(subscribers,image=img_tk)
    imglbl.place(x=0,y=0,relwidth=1,relheight=1)



    #-----------------------------------------------------------------------------
    # frame = Frame(subscribers)
    # frame.place(x=0, y=0)


    # bgimg = tk.PhotoImage(file="Screenshot (171).png")
    # # label = ttk.Label(subscribers, image=bgimg).pack()
    # # limg = Label(subscribers, i=bgimg)
    # # limg.pack()


    # (subscribers)#the main form

    #-----------------------------------------------------------------------------
    #img=Image.open("img/gg.jpeg")
    #img=img.resize((1200,600))
    #img_tk=ImageTk.PhotoImage(img)
    #imglbl=tkinter.Label(subscribers,image=img_tk)
    #imglbl.place(x=0,y=0,relwidth=1,relheight=1)
    #-----------------------------------------------------------------------------
    #2frames
    f1=tk.Frame(subscribers,bg="#D3D04F")
    f2=tk.Frame(subscribers,bg="#D3D04F")


    # 3 label frames
    #wrapper1 = LabelFrame(subscribers, text="subscribers list",width=50, height= 25)
    #wrapper2 = LabelFrame(subscribers, text="Search")
    #wrapper3 = LabelFrame(subscribers, text="subscriber Data -- (double click to select data)")





    #wrapper1.grid_propagate(0)
    #wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
    #wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
    #wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)


    # tree view for traversing the database
    trv = Treeview(subscribers, columns=(1, 2, 3, 4, 5, 6, 7,8), show="headings", height="10", selectmode='browse')
    trv.pack(side=LEFT)
    trv.place(x=0, y=0)


    # verticall scrollbar
    #yscrollbar = ttk.Scrollbar(subscribers, orient="vertical", command=trv.yview)
    #yscrollbar.pack(side=RIGHT, fill="y")
    #trv.configure(yscrollcommand=yscrollbar.set)


    trv.heading(1, text="ID")
    trv.heading(2, text="Name")
    trv.heading(3, text="Age")
    trv.heading(4, text="Join Date")
    trv.heading(5, text="Subscribtion Type")
    trv.heading(6, text="Subscribtion Fees")
    trv.heading(7, text="Days")
    trv.heading(8, text="Backge number")


    trv.column(1, width=100, anchor='center')
    trv.column(2, width=400)
    trv.column(3, width=100, anchor='center')
    trv.column(4, width=250)
    trv.column(5, width=150, anchor='center')
    trv.column(6, width=150, anchor='center')
    trv.column(7, width=100, anchor='center')
    trv.column(8, width=150, anchor='center')

    style = Style()
    style.configure('Treeview', font=('arial', 11),
                    foreground='#100720', background='#FFC23C')
    style.configure('Treeview.Heading', font=('tahoma', 12))

    # traverse data on the tree view section
    cursor.execute(
        "select id , name, age, joindate, subtype , fees, days, packagesub from subscribers")
    rows = cursor.fetchall()
    update_func(rows)

    # search section
    lbl = Label(f1, text="Search",background="#D3D04F")
    lbl.pack(side=tk.LEFT, padx=10)
    ent = Entry(f1, textvariable=q)
    ent.pack(side=tk.LEFT, padx=6)
    btn = tk.Button(f1, text="Search",background="#FFC436", command=search_func)
    btn.pack(side=tk.LEFT, padx=10)
    Cbtn = tk.Button(f1, text='clear',background="#FFC436", command=clear_func)
    Cbtn.pack(side=tk.LEFT, padx=10)


    # User Data Section
    trv.bind('<Double 1>', getrow)

    # 4 data entry
    lbl1 = Label(f2, text="Customer ID",background="#D3D04F")
    lbl1.grid(row=0, column=0, padx=5, pady=3)
    ent1 = Entry(f2, textvariable=t1)
    ent1.grid(row=0, column=1, padx=5, pady=3)
    ent1.configure(state=DISABLED)

    lbl2 = Label(f2, text="Name",background="#D3D04F")
    lbl2.grid(row=1, column=0, padx=5, pady=3)
    ent2 = Entry(f2, textvariable=t2)
    ent2.grid(row=1, column=1, padx=5, pady=3)
    ent2.configure(state=DISABLED)

    lbl3 = Label(f2, text="subscription type",background="#D3D04F")
    lbl3.grid(row=2, column=0, padx=5, pady=3)
    ent3 = Entry(f2, textvariable=t3)
    ent3.grid(row=2, column=1, padx=5, pady=3)
    ent3.configure(state=DISABLED)

    lbl4 = Label(f2, text="days",background="#D3D04F")
    lbl4.grid(row=3, column=0, padx=5, pady=3)
    ent4 = Entry(f2, textvariable=t4)
    ent4.grid(row=3, column=1, padx=5, pady=3)

    # 3 Buttons for modifications
    up_btn = tk.Button(f2, text="Update days",background="#FFC436", command=update_customer)
    add_btn = tk.Button(f2, text="Reward days",background="#FFC436", command=reward)
    delete_btn = tk.Button(f2, text="Cancel subscribtion",background="#FFC436",command=delete_customer)
    # add fuction here to return to main page
    Exit = tk.Button(f2, text="EXIT to main menu",background="#FFC436", command=exit_func)

    add_btn.grid(row=4, column=0, padx=5, pady=3)
    up_btn.grid(row=4, column=1, padx=5, pady=3)
    delete_btn.grid(row=4, column=2, padx=5, pady=3)
    Exit.grid(row=4, column=3, padx=10, pady=3)


    f1.pack(side="left",padx=150,pady=300)
    f2.pack(side="right",padx=90,pady=80)

    subscribers.mainloop()

if __name__ == "__main__":
        frommoibrahim()