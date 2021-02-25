# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 01:17:13 2021

@author: fatih
"""
import tkinter as tk
from tkinter import *
import os

welcome_screen=tk.Tk()
welcome_screen.geometry("700x600") # set the configuration of GUI window 
welcome_screen.title('Welcome Page') 
# Set text variables
username = StringVar()
password = StringVar()
global username_verify 
global password_verify 
username_verify = StringVar()
password_verify = StringVar()
# Set label for user's instruction
Label(welcome_screen, text="Please login to use app", bg="blue").pack()
Label(welcome_screen, text="").pack()
# Set username label
username_label = Label(welcome_screen, text="Username : ")
username_label.pack()
# Set username entry
# The Entry widget is a standard Tkinter widget used to enter or display a single line of text.    
username_login_entry  = Entry(welcome_screen, textvariable=username_verify)
username_login_entry.pack()

# Set password label
password_lable = Label(welcome_screen, text="Password : ")
password_lable.pack()
  
# Set password entry
password_login_entry = Entry(welcome_screen, textvariable=password_verify, show='*')
password_login_entry.pack()

def register():
    global register_screen
    register_screen = Toplevel(welcome_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username : ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password : ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()



# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()

# Designing popup for login success
 
def login_success():
    global login_success_screen
    login_success_screen = Toplevel(welcome_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=main_page).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(welcome_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(welcome_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy() 


def main_page():
    global main_page_screen
    main_page_screen = Toplevel(welcome_screen)
    main_page_screen.title("Main Page")
    main_page_screen.geometry("1150x1000")
    Button(main_page_screen, text="Personnel List", height="2", width="30").pack()
    Button(main_page_screen, text="Register", height="2", width="30").pack()


button_log = tk.Button(welcome_screen, text='Login', width=25, command=login_verify) 
button = tk.Button(welcome_screen, text='Exit', width=25, command=welcome_screen.destroy) 
button_log.pack() 
# Set register button
Button(text="Register", height="2", width="30", command=register).pack()
button.pack() 

welcome_screen.mainloop() 

