# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 13:44:22 2020

@author: Stuti
"""
import tkinter as tk
import pymongo


    
class add_user:
    def __init__(self,root):
        self.root=root
        self.root.title(" USER MODULE")
        self.root.geometry("700x400+0+0")
        
        
        self.n=tk.StringVar()
        self.a=tk.StringVar()
        self.phone=tk.StringVar()
        
        title=tk.Label(self.root,text="ADD USER\n ENTER THE DETAILS",font=("times new roman",20,"bold"),bg="blue",fg="red",bd=10,relief='groove')
        title.place(x=0,y=0,relwidth=1)
        Add_Frame=tk.Frame(self.root,bg="white")
        Add_Frame.place(x=0,y=150)
        addname=tk.Label(Add_Frame,text="NAME",compound='left',font=("times new roman",20,"bold")).grid(row=1,column=0,padx=20,pady=10)
        txtname=tk.Entry(Add_Frame,textvariable=self.n,bd=5,relief='groove',font=("",15)).grid(row=1,column=1,padx=20)
        lbladrs=tk.Label(Add_Frame,text="ADDRESS",compound='left',font=("times new roman",20,"bold")).grid(row=2,column=0,padx=20,pady=10)
        txtadrs=tk.Entry(Add_Frame,textvariable=self.a,bd=5,relief='groove',font=("",15)).grid(row=2,column=1,padx=20)
        lblphn=tk.Label(Add_Frame,text="PHONE NO(with country code)",compound='left',font=("times new roman",20,"bold")).grid(row=3,column=0,padx=20,pady=10)
        txtphn=tk.Entry(Add_Frame,textvariable=self.phone,bd=5,relief='groove',font=("",15)).grid(row=3,column=1,padx=20)
        btn_log=tk.Button(Add_Frame,text="Add",width=15,font=("times new roman",14,"bold"),bg="yellow",fg="red",command=self.connect).grid(row=4,column=1,pady=10)
        
        
        
    def connect(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["farmers"]
        mycol = mydb["farmers"]

        mydict={"name":self.n.get(),"address":self.a.get(),"phoneNo":self.phone.get()}

        x = mycol.insert_one(mydict)
        tk.messagebox.showinfo("MESSAGE","Added Successfully")


root=tk.Tk()
obj=add_user(root)











root.mainloop()