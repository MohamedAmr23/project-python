from tkinter import *
from PIL import Image , ImageTk
from tkinter.ttk import *
import mysql.connector
from mysql.connector import *

from tkinter import simpledialog
from tkinter import simpledialog
sale = Tk()
sale.title("Buy")
sale.geometry('1366x786')
sale.resizable(False, False)
#r1=sale.winfo_screenheight()
#r2=sale.winfo_screenwidth()
#print(r1)
#print(r2)
v1_rbtn=IntVar()
v1_rbtn.set(1)

v1_co=IntVar()
v1_co.set(1)
#Create DataBase

# def Create_database():
#     db = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="*#@Mohamed*#@12"
#     )
#     cursor = db.cursor()
#     cursor.execute("CREATE DATABASE Sales")

#######################################################################
def CreateTables():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="*#@Mohamed*#@12",
        database="Sales"
    )
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE products(id INT Primary key ,prod VARCHAR(200),amount INT ) """)
####################################################################
def insert_data(IDD,pro,am):
  db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="*#@Mohamed*#@12",
        database="Sales"
  )

  cursor = db.cursor()
  cursor.execute(f"""INSERT INTO products (id ,prod,amount)VALUES ( {ID},{pro},{am} )""")
  
  db.commit()
################################################################################
def show_data():
  db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="*#@Mohamed*#@12",
            database="Sales"
  )
  cursor = db.cursor()
  cursor.execute("SELECT * FROM products")
  results = cursor.fetchall()
  for data in results:
      print(data)    
###############################################################################################  
def decrease_value(n):
    db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="*#@Mohamed*#@12",
                database="Sales"
      )

    cursor = db.cursor()
    cursor.execute(f" UPDATE  products SET amount= amount - 1 WHERE id = {n}")
    db.commit()  # Commit the changes to the database
    show_data()  
    print("#"*20)
###########################################################################################


bll=Label(sale , text='Classic Joe Classic \n\nBlender Bottle 20oz \n\n $10.00',font=('Arial',15,'bold'))


bu_buy=Button(sale ,text="Buy",command= lambda :decrease_value(1) )

#creat image 
img = Image.open("images/IMG_421.png")
img = img.resize ((150 , 200))
img_tk = ImageTk.PhotoImage(img)
# imglbl = Label( sale , image=img_tk)
bt10=Button(sale ,image=img_tk).place(x=250,y=10)


bll.place(x=40,y=10)
bu_buy.place(x=50,y=170)
##########################################################################row=1  column=2  good
bll3=Label(sale , text='Classic Joe Tee \n\n    $24.00',font=('Arial',15,'bold'))

btn1=Radiobutton(sale,text='L',value=1,variable=v1_rbtn)
rbtn2=Radiobutton(sale,text='XL',value=2,variable=v1_rbtn)
rbtn3=Radiobutton(sale,text='2XL',value=3,variable=v1_rbtn)

bu3_buy=Button(sale ,text="Buy",command= lambda :decrease_value(2) )

# #creat image
img2 = Image.open("images/IMG_422.png")
img2 = img2.resize ((200 , 250))
img_tk = ImageTk.PhotoImage(img2) 
#imglbl = Label( sale , image=img_tk)
bt20=Button(sale ,image=img_tk).place(x=690,y=10)



bll3.place(x=500,y=30)

bu3_buy.place(x=530,y=170)
btn1.place(x=530,y=115)
rbtn2.place(x=560,y=115)
rbtn3.place(x=595,y=115)
########################################################################### row=1  column=3
bll4=Label(sale , text=" Hand Grip Strengthener",font=('Arial' ,15 , 'bold') )
bll4_sale=Label(sale ,text='$90.00',font=('Arial' ,15 , 'bold'))
btn1=Radiobutton(sale,text='Green',value=1,variable=v1_co)
rbtn2=Radiobutton(sale,text='Black',value=2,variable=v1_co)
txt_buy=Button(sale , text='Buy',command= lambda :decrease_value(3))


#creat image 
img = Image.open("images/IMG_4133.png")
img = img.resize ((140 , 240))
img_tk = ImageTk.PhotoImage(img)
imglbl = Label( sale , image=img_tk)
bt10=Button(sale ,image=img_tk).place(x=1200,y=10)



bll4.place(x=930,y=10)
bll4_sale.place(x=965,y=60)
txt_buy.place(x=950,y=170)
btn1.place(x=950,y=100)
rbtn2.place(x=1010,y=100)
########################################################################### row=2  column=1
bll1=Label(sale , text='Drawstring Bag\n\n  $25.00',font=('Arial',15,'bold'))
bu_buy1=Button(sale ,text="Buy" ,command= lambda :decrease_value(4))

#creat image 
img = Image.open("images/IMG_4244.png")
img = img.resize ((180 , 210))
img_tk = ImageTk.PhotoImage(img)
imglbl = Label( sale , image=img_tk)
bt10=Button(sale ,image=img_tk).place(x=250,y=350)

bll1.place(x=25,y=357)
bu_buy1.place(x=45,y=470)
###########################################################################  row=2  column=2
bll5=Label(sale , text='Gloves\n\n$265.00',font=('Arial',15,'bold'))
bu_buy5=Button(sale , text="Buy",command= lambda :decrease_value(5) )

#creat image 
img90 = Image.open("images/IMG_4255.png")
img90 = img90.resize ((180 , 210))
img_tk = ImageTk.PhotoImage(img90)
imglbl90 = Label( sale , image=img_tk)
bt90=Button(sale ,image=img_tk).place(x=680,y=350)

bll5.place(x=530,y=350)
bu_buy5.place(x=540,y=460)

###########################################################################  row=2  column=3

bll5=Label(sale , text='Commandos\n\n Re-Load weight\n\n Gainer 3KG \n\n       $1500 ',font=('Arial',13,'bold'))
bu_buy5=Button(sale ,text="Buy" ,command= lambda :decrease_value(6))

#creat image 
img = Image.open("images/IMG_4266.png")
img = img.resize ((150 , 180))
img_tk = ImageTk.PhotoImage(img)
imglbl = Label( sale , image=img_tk)
bt10=Button(sale ,image=img_tk).place(x=680,y=590)

bll5.place(x=530,y=585)
bu_buy5.place(x=560,y=750)


################################################### ######################## row=3  column=1
bll2=Label(sale , text='Creatine Monohydrate \n\n Powder  \n\n   $1000',font=('Arial',15,'bold'))
bu_buy2=Button(sale ,text="Buy" ,command= lambda :decrease_value(7))

#creat image 
img = Image.open("images/IMG-20277.png")
img = img.resize ((180 , 200))
img_tk = ImageTk.PhotoImage(img)
imglbl = Label( sale , image=img_tk)
bt10=Button(sale ,image=img_tk).place(x=250,y=590)

bll2.place(x=25,y=585)
bu_buy2.place(x=45,y=755)

############################################################################ row=3 column=2

bll5=Label(sale , text='SportQ Cement Barbell Set  \n\n   $1.350',font=('Arial',15,'bold'))
bu_buy5=Button(sale ,text="Buy" , command= lambda :decrease_value(8) )

img = Image.open("images/IMG-2026666.png")
img = img.resize ((150 , 210))
img_tk = ImageTk.PhotoImage(img)
imglbl = Label( sale , image=img_tk)
bt10=Button(sale ,image=img_tk).place(x=1200,y=350)

bll5.place(x=920,y=350)
bu_buy5.place(x=1020,y=445)
 
###########################################################################  row=3  column=3
bll2=Label(sale , text= 'Optimum Nutrition (ON) \n\n Serious Mass High \n\n Protein      $3.500',font=('Arial',14,'bold'))
bu_buy2=Button(sale ,text="Buy",command= lambda :decrease_value(9) )

img = Image.open("images/IMG-2099.png")
img = img.resize ((160 , 200))
img_tk = ImageTk.PhotoImage(img)
imglbl = Label( sale , image=img_tk)
bt10=Button(sale ,image=img_tk).place(x=1150,y=590)

bll2.place(x=910,y=585)
bu_buy2.place(x=1010,y=755)


sale.mainloop()

















 