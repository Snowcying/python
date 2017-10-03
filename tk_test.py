# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 11:52:27 2017

@author: 陈鑫一
"""

from tkinter import*
def processOK():
    print("OK button is clicked")
    
def processCancel():
    print("Cancel button is clicked")
    
def main():
    tk= Tk()
    btnOK=Button(tk,text="OK",fg="red",
       command=processOK          )
    btnCancel=Button(tk,text="Cancel",bg="yellow",
                     command=processCancel)
    btnOK.pack()
    btnCancel.pack()
    
    tk.mainloop()
    

main() 