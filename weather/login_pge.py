# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 23:57:07 2020

@author: Stuti
"""
import tkinter as tk
from PIL import ImageTk




class Login_System:   
    def __init__(self , root):
       self.root=root
       self.root.title("LOGIN SYSTEM")
       self.root.geometry("1350x700+0+0")
       
       ####All Images####
       self.bg_icon=ImageTk.PhotoImage(file="images/bg2.jpg")
       #self.user_icon=tk.PhotoImage(file="images/tiny.png")
       #self.pass_icon=tk.PhotoImage(file="images/password.png")
       self.logo_icon=tk.PhotoImage(file="images/man-user1.png")
       
       #=====variable===#
       self.uname=tk.StringVar()
       self. pass_=tk.StringVar()
       bg_lbl=tk.Label(self.root,image=self.bg_icon).pack()
       title=tk.Label(self.root,text="LOGIN SYSTEM",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief='groove')
       title.place(x=0,y=0,relwidth=1)
       
       Login_Frame=tk.Frame(self.root,bg="white")
       Login_Frame.place(x=500,y=150)
       logolbl=tk.Label(Login_Frame,image=self.logo_icon).grid(row=0,columnspan=2,pady=20)
       
       lbluser=tk.Label(Login_Frame,text="Username",compound='left',font=("times new roman",20,"bold")).grid(row=1,column=0,padx=20,pady=10)
       txtuser=tk.Entry(Login_Frame,textvariable=self.uname,bd=5,relief='groove',font=("",15)).grid(row=1,column=1,padx=20)
       lblpass=tk.Label(Login_Frame,text="Password",compound='left',font=("times new roman",20,"bold")).grid(row=2,column=0,padx=20,pady=10)
       txtpass=tk.Entry(Login_Frame,textvariable=self.pass_,bd=5,relief='groove',font=("",15)).grid(row=2,column=1,padx=20)
       btn_log=tk.Button(Login_Frame,text="Login",width=15,font=("times new roman",14,"bold"),bg="yellow",fg="red",command=self.login_id).grid(row=3,column=1,pady=10)
       
    def login_id(self):
        if self.uname.get()==" "  or  self.pass_.get()==" ":
               tk.messagebox.showerror('Error',"All fields are required !!")
        elif self.uname.get()=="shivam"  and  self.pass_.get()=="shivam@24":
               tk.messagebox.showinfo("Successfull",f"welcome {self.uname.get()}")
                           
        else:
               tk.messagebox.showerror("Error","Invalid username or password")
   
    #========

                                   

root=tk.Tk()
obj=Login_System(root)











root.mainloop()