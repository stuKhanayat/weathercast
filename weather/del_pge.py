# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 10:55:10 2020

@author: Stuti
"""

import tkinter as tk
import pymongo


    
class del_user:
    def __init__(self,root):
        self.root=root
        self.root.title(" USER MODULE")
        self.root.geometry("700x400+0+0")
        
        
        self.n=tk.StringVar()
        
        
        title=tk.Label(self.root,text="Delete USER\n ENTER THE DETAILS",font=("times new roman",20,"bold"),bg="blue",fg="red",bd=10,relief='groove')
        title.place(x=0,y=0,relwidth=1)
        D_Frame=tk.Frame(self.root,bg="white")
        D_Frame.place(x=0,y=150)
        del_name=tk.Label(D_Frame,text="Enter the name you want to delete",compound='left',font=("times new roman",20,"bold")).grid(row=1,column=0,padx=20,pady=10)
        txtname=tk.Entry(D_Frame,textvariable=self.n,bd=5,relief='groove',font=("",15)).grid(row=1,column=1,padx=20)
        
        btn_log=tk.Button(D_Frame,text="Delete",width=15,font=("times new roman",14,"bold"),bg="yellow",fg="red",command=self.connect).grid(row=4,column=1,pady=10)
        
        
        
    def connect(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["farmers"]
        mycol = mydb["farmers"]

        mydict={"name":self.n.get()}

        x = mycol.delete_many(mydict)
        print(x)
        tk.messagebox.showinfo("MESSAGE","Deleted Successfully")


root=tk.Tk()
obj=del_user(root)











root.mainloop()