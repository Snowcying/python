# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 15:14:47 2017

@author: 陈鑫一
"""

from tkinter import *
def main():
    tk=Tk()
    canvas=Canvas(tk,width=200,height=200)
    canvas.pack()
    canvas.create_text(100,40,text="welcome to Tkinter",
                       fill="blue",font=("Times",16))
    myImage=PhotoImage(file="d:\gif_test.gif")
    canvas.create_image(10,70,anchor=NW,image=myImage)
    canvas.create_rectangle(10,70,190,130)
    tk.mainloop()
    
main()    