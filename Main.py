# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 01:17:13 2021

@author: fatih
"""
import tkinter as tk
import pandas as pd # data processing, CSV file I/O 
import numpy as np # linear algebra
from tkinter import *
import os
file=pd.read_csv("PersonnelList.csv",delimiter=";",error_bad_lines=False)
personnel=file.values
personnel_column_names=file.columns.values
total_rows = len(personnel) 
total_columns = len(personnel[0]) 
last_row=" "
file1=pd.read_csv("ProjectList.csv",delimiter=";",error_bad_lines=False)
project=file1.values
total_project_rows = len(project) 
total_project_columns = len(project[0]) 
project_column_names=file1.columns.values
welcome_screen=tk.Tk()
welcome_screen.geometry("700x600") # set the configuration of GUI window 
welcome_screen.title('Hoşgeldiniz') 
# Set text variables
username = StringVar()
password = StringVar()
global username_verify 
global password_verify 
username_verify = StringVar()
password_verify = StringVar()
# Set label for user's instruction
Label(welcome_screen, text="Uygulamayı kullanmak için lütfen giriş yapın", bg="blue").pack()
Label(welcome_screen, text="").pack()
# Set username label
username_label = Label(welcome_screen, text="Kullanıcı Adı : ")
username_label.pack()
# Set username entry
# The Entry widget is a standard Tkinter widget used to enter or display a single line of text.    
username_login_entry  = Entry(welcome_screen, textvariable=username_verify)
username_login_entry.pack()

# Set password label
password_lable = Label(welcome_screen, text="Şifre : ")
password_lable.pack()
  
# Set password entry
password_login_entry = Entry(welcome_screen, textvariable=password_verify, show='*')
password_login_entry.pack()

def register():
    global register_screen
    register_screen = Toplevel(welcome_screen)
    register_screen.title("Kayıt Ol")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Kayıt olmak için lütfen aşağıdaki bilgileri doldurun", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Kullanıcı Adı : ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Şifre : ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Kayıt Ol", width=10, height=1, bg="blue", command = register_user).pack()



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
 
    Label(register_screen, text="Kayıt başarılı, Lütfen hesabın onaylanmasını bekleyiniz. ", fg="green", font=("calibri", 11)).pack()

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
# Designing main page after login success
def main_page():
    global main_page_screen
    main_page_screen = Toplevel(welcome_screen)
    delete_login_success()
    main_page_screen.title("Ana Sayfa")
    main_page_screen.geometry("1150x1000")
    Button(main_page_screen, text="Personel Listesi", height="2", width="30", command=personnel_list).pack()
    Button(main_page_screen, text="Proje Listesi", height="2", width="30", command=project_list).pack()
    Button(main_page_screen, text="Atama Modeli", height="2", width="30").pack()
    Button(main_page_screen, text="Yeni Kullanıcı Onaylama", height="2", width="30").pack()
    Button(main_page_screen, text="Çıkış Yap", height="2", width="30", command=delete_main_page_screen).pack()

# Designing popup for personnel list

def personnel_list():
    
    global personnel_list_screen
    personnel_list_screen = Toplevel(welcome_screen)
    back_button=Button(personnel_list_screen, text="Geri", command=delete_personnel_list_screen)
    add_button=Button(personnel_list_screen, text="Personel Ekle", command=delete_personnel_list_screen)
    delete_button=Button(personnel_list_screen, text="Personel Sil", command=delete_personnel_list_screen)
    edit_button=Button(personnel_list_screen, text="Verileri Düzenle", command=delete_personnel_list_screen)
    refresh_button=Button(personnel_list_screen, text="Yenile", command=delete_personnel_list_screen)
    for i in range(total_columns):
          e=Entry(personnel_list_screen, width=10, fg='blue', font=('Arial',16,'bold')) 
          e.grid(row=0, column=i) 
          e.insert(END, personnel_column_names[i])  
    for i in range(total_rows): 
        for j in range(total_columns): 
              
            e=Entry(personnel_list_screen, width=10, fg='blue', font=('Arial',16,'bold'))    
            e.grid(row=i+1, column=j) 
            e.insert(END, personnel[i][j]) 
    
    add_button.grid(row=total_rows+1, column=0, sticky="ew")
    edit_button.grid(row=total_rows+1, column=1, sticky="ew")
    delete_button.grid(row=total_rows+1, column=2, sticky="ew")
    refresh_button.grid(row=total_rows+1, column=3, sticky="ew")
    back_button.grid(row=total_rows+1, column=4, sticky="ew")   
     
    personnel_list_screen.title("Personel Listesi")
    personnel_list_screen.geometry("2150x1680")  
    
# Designing popup for project list
def project_list():
    
    global project_list_screen
    project_list_screen = Toplevel(welcome_screen)
    back_button=Button(project_list_screen, text="Geri", command=delete_project_list_screen)
    add_button=Button(project_list_screen, text="Proje Ekle", command=add_project_screen)
    project_is_completed_button=Button(project_list_screen, text="Proje Tamamlandı",command=delete_project_list_screen)
    for i in range(total_project_columns):
          e=Entry(project_list_screen, width=10, fg='blue', font=('Arial',16,'bold')) 
          e.grid(row=0, column=i) 
          e.insert(END, project_column_names[i])    
    for i in range(total_project_rows): 
        for j in range(total_project_columns): 
            e=Entry(project_list_screen, width=10, fg='blue', font=('Arial',16,'bold')) 
            e.grid(row=i+1, column=j) 
            e.insert(END, project[i][j]) 
    
    add_button.grid(row=total_project_rows+1, column=0, sticky="ew")
    project_is_completed_button.grid(row=total_project_rows+1, column=2, sticky="ew")
    back_button.grid(row=total_project_rows+1, column=4, sticky="ew")   
    project_list_screen.title("Proje Listesi")
    project_list_screen.geometry("2150x1680")  
# Designing popup for new project 
def add_project_screen():
    global new_project_screen
    new_project_screen = Toplevel(welcome_screen)
    login_success_screen.title("Giriş Başarılı")
    login_success_screen.geometry("150x100")

# Designing popup for login success
 
def login_success():
    global login_success_screen
    login_success_screen = Toplevel(welcome_screen)
    login_success_screen.title("Giriş Başarılı")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Giriş Başarılı").pack()
    Button(login_success_screen, text="OK", command=main_page).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(welcome_screen)
    password_not_recog_screen.title("Geçersiz Şifre")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Geçersiz Şifre").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(welcome_screen)
    user_not_found_screen.title("Kullanıcı Bulunamadı")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="Kullanıcı Bulunamadı").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy() 

def delete_main_page_screen():
    main_page_screen.destroy()
    
def delete_personnel_list_screen():
    personnel_list_screen.destroy()

def delete_project_list_screen():
    project_list_screen.destroy()
button_log = tk.Button(welcome_screen, text='Giriş', width=25, command=login_verify) 
button = tk.Button(welcome_screen, text='Çıkış Yap', width=25, command=welcome_screen.destroy) 
button_log.pack() 
# Set register button
Button(text="Kayıt Ol", height="2", width="30", command=register).pack()
button.pack() 

welcome_screen.mainloop() 

