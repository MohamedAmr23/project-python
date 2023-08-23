# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 13:53:17 2023

@author: hp
"""
# =============================================================================
# --------------------------- "About Frame" -----------------------------------
# =============================================================================

from tkinter import * 
from PIL import Image , ImageTk
import home_page
def fromabout():
    window = Tk() 
    window.title("About Us" ) 
    window.config(bg='#FFB100' )

    about = Frame(window) 

    # =============================================================================
    # # Centering the window
    # =============================================================================
    def center_screen (w , h) :
        
        height = window.winfo_screenheight() 
        width = window.winfo_screenwidth() 
        print(height , width)
        
        x = int ((width - w)/2)
        y = int ((height - h)/2)
        
        window.geometry(f'{w}x{h}+{x}+{y}')

    center_screen(1366, 700)


    #----------------------------- Add an icon ------------------------------------

    icon = Image.open('images/5eb3cb4bc8c459000443515c.png') 
    icon = icon.resize((163 , 100))
    icon_tk = ImageTk.PhotoImage(icon)

    #----------------------------- Label 1 ----------------------------------------

    lbl = Label(window , text="About Gold's Gym",compound='bottom' , image=icon_tk ,bg= '#FFB100', font=("Times", 24 , "bold" ))
    lbl.pack(pady = 10 )

    #----------------------------- Label 2 ----------------------------------------

    lbl2 = Label(window , text='''What’s the history of Gold’s Gym? Why is it so popular?
        Gold's Gym is one of the most well-known and respected fitness chains in the world. 
    It was founded in Venice Beach, California in 1965 by Joe Gold, a bodybuilder and weightlifting enthusiast. 
    Gold's Gym quickly became popular among bodybuilders, powerlifters, and other fitness enthusiasts, 
    thanks to its focus on strength training and its excellent equipment.
    One of the reasons for its popularity is that it was one of the first gyms to focus on weightlifting and bodybuilding. 
    It has also been the home gym of some of the most famous bodybuilders of all time, such as Arnold Schwarzenegger, 
    Lou Ferrigno, and Frank Zane.
    In addition to its reputation as a "Mecca of Bodybuilding," Gold's Gym is also known for its diverse range of training options, 
    including cardio, group fitness, and personal training. It has also been featured in numerous movies, TV shows and music videos, 
    which helped to increase its exposure and popularity.
    Gold's Gym has always been a leader in the fitness industry and continues to be a major player today with gyms all over the world.''' , fg="black", font=("Arial" , 14 ), bg= '#FFB100')

    lbl2.pack( pady= 5, after= lbl)

    #----------------------------- Label 3 ----------------------------------------

    lbl3 = Label(window , text='''Who is the Golds gym model?
    (April 26, 2022) Gold's Gym, the most iconic name in fitness, 
    has named bodybuilder and fitness mega-influencer Simeon Panda as the new face of the brand. 
    The partnership bridges the famed, Venice-born gym's storied past to the future of the evolving brand ''' , bg="#FFB100" , fg="black", font=("Arial" , 15 ))

    lbl3.pack(pady= 10, after= lbl2)
    #----------------------------- Label 4 ----------------------------------------

    lbl4 = Label(window , text='''What is special about gold gym?
    ABOUT GOLD'S GYM
    It was the place for serious fitness. Opened long before the modern-day health club existed, 
    the original Gold's Gym featured homemade equipment and a dedication to getting results. 
    It was an instant hit. Gold's Gym quickly became known as “The Mecca of Bodybuilding''' , bg="#FFB100" , fg="black", font=("Arial" , 15 ))

    lbl4.pack(pady= 10, after= lbl3) 

    # =============================================================================
    # ----------------------- backHome function -----------------------------------
    # =============================================================================
    def backHome () :
        import home_page
        import signup
        about.destroy()
        home_page.display_home()
       ##############################
        

        
    def exit_func():
        about.destroy()
        home_page.display_home()        
        
    #btn_home = Button(window , text= 'Home Page' ,bg='black' , fg = 'yellow', font=("Arial" , 16 , "bold") , borderwidth= 5 , command=exit_func )
    #btn_home.place(x=50,y=50)#pack(anchor ="s" , after= lbl4 ,padx= 10 , pady= 10)



    about.place(anchor='center' , relx= 0.5 , rely= 0.5)

    window.mainloop() 
if __name__ == "__main__":
        fromabout()