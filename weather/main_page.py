# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 00:25:21 2020

@author: Stuti
"""
import tkinter as tk

class main_page:
    def __init__(self , root):
       self.root=root
       self.root.title("MAIN MODULE")
       self.root.geometry("700x400+0+0")
       
       MAIN_Frame=tk.Frame(self.root,bg="white")
       MAIN_Frame.place(x=250,y=50)
       btn_log=tk.Button(MAIN_Frame,text="VIEW WEATHER",width=15,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=0,column=0,pady=20)
       
       btn_log1=tk.Button(MAIN_Frame,text="SEND WARNING",width=15,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=1,column=0,pady=20)
       btn_log2=tk.Button(MAIN_Frame,text="USER INFO",width=15,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=2,column=0,pady=20)
       
root=tk.Tk()
obj=main_page(root)



root.mainloop()