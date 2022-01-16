#function for entering details
from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
import sqlite3
import re
from tkinter import ttk
import matplotlib.pyplot as plt
root=Tk()
root.iconbitmap()
root.geometry("200x200")
def login_details():
    global name_login_box
    global passcode_login_box
    #create textboxes
    name_login_box=Entry(root,width=30)
    name_login_box.place(relx=0.4,rely=0.4)
    #passcode text code
    passcode_login_box=Entry(root,width=30)
    passcode_login_box.place(relx=0.4,rely=0.5)
    #label for userid
    name_login_label=Label(root,text="USER ID")
    name_login_label.place(relx=0.3,rely=0.4)
    #label for passcode in login
    passcode_login_label=Label(root,text="passcode")
    passcode_login_label.place(relx=0.3,rely=0.5)
    
    #create Login button
    login_btn2=Button(root,text="submit",command=login)
    login_btn2.place(relx=0.47,rely=0.55)

    #print("hel",username,password)
    #name_login_box.delete(0,END)
    #passcode_login_box.delete(0,END)
#function for login
def login():
    #create a database or connect to one
    conn=sqlite3.connect('Details.db')
    #create cursor
    c=conn.cursor()
    global username
    global password
    username=name_login_box.get()
    password=passcode_login_box.get()
    #print("hel",username,password)
    statement = f"SELECT userid from Login_details WHERE userid='{username}' AND passcode ='{password}';"
    c.execute(statement)
    record=c.fetchone()
    if not record:  # An empty result evaluates to False.
        fail=Label(text="Enter valid details...")
        fail.place(relx=0.37,rely=0.6)
        name_login_box.delete(0,END)
        passcode_login_box.delete(0,END)
        return 0
    else:
        #print("Welcome")
        passed_label=Label(text="Logged in successfully..")
        passed_label.place(relx=0.37,rely=0.6)
        login3_btn=Button(root,text="GIVE REVIEW",command=item_list_give)
        login3_btn.place(relx=0.35,rely=0.65)
        login3_1_btn=Button(root,text="GET REVIEW",command=item_list)
        login3_1_btn.place(relx=0.45,rely=0.65)
        login3_2_btn=Button(root,text="GET RESULT",command=final_ward)
        login3_2_btn.place(relx=0.55,rely=0.65)
        name_login_box.delete(0,END)
        passcode_login_box.delete(0,END)
        return 1
    #commit changes
    conn.commit()

    #close connection
    conn.close()
    #name_login_box.delete(0,END)
    #passcode_login_box.delete(0,END)    
    
    
'''
#create table
c.execute("""CREATE TABLE Login_details(
            userid text,
            passcode text,
            name text,
            phone text,
            address text,
            ward_image text,
            design_image text,
            new_image text
        )""")
'''
#frame 1

login1_btn=Button(root,text="LOGIN",command=login_details,fg="blue",activebackground = "black")
#login1_btn.grid(row=20,column=90)
login1_btn.place(relx=0.45, rely=0.25, anchor=CENTER)


