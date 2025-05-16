import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
import os 
import random

#  create the login page that contain
#  username, password, login button and signin button 


## try to encrypt 
chars = "this is kevin tido "

print("Before the Encryption",chars)

encryption(chars)

print("After the encryption",chars)

def encryption(encrypt):
    encrypt.encode
    


class login_page:
        
    def __init__(self,root):
        self.root=root
        self.root.title("Login Page")
        self.root.geometry("300x250")

        self.label=tk.Label(self.root, text="UserName: ")
        self.label.grid(row=0,column=0,pady=4,sticky="nsew")
        self.username=tk.Entry(self.root)
        self.username.grid(row=1,column=0,sticky="nsew")

        self.label=tk.Label(self.root, text="Password: ")
        self.label.grid(row=2,column=0,pady=4,sticky="nsew")
        self.password=tk.Entry(self.root)
        self.password.grid(row=3,column=0,sticky="nsew")

       
        # Login Button
        tk.Button(root, text="Login", command=self.login).grid(row=4, column=0, columnspan=2, pady=(10, 5))

        # Signup Button
        tk.Button(root, text="Signup", command=self.signup).grid(row=5, column=0, columnspan=2)

    
    def login(self):
        username = self.username.get()
        password = self.password.get()

        ## username and password can not be back before the login and signup 
        if not username or not password:
            messagebox.showerror("Error","Username and Password must not be bank")
            return

        if not os.path.exists("users.json"):
            messagebox.showerror("Error","User have been not found in the system, Please signup first!!")
            return
        
        with open("users.json","r") as file:
            users = json.load(file)

        if username in users and users[username] == password:
            with open("current_user.json", "w") as file:
                json.dump({"username": username}, file)
            messagebox.showinfo("Success", f"Welcome, {username}, Login successfully!")
        else:
            messagebox.showerror("Error", "Invalid username or password.")



    def signup(self):
        username  = self.username.get()
        password = self.password.get()

        ## user must file the filed 
        if not username or not password:
            messagebox.showerror("Error","Username and password must not be bank")
            return
        
        users = {}
        if os.path.exists("users.json"):
            with open("users.json","r") as file:
                users = json.load(file)
        
        
        if username in users:
            messagebox.showerror("Error","User name already exit in the system")
        else:
            users[username] = password
            with open("users.json","w") as file:
                json.dump(users,file)
            messagebox.showinfo("User Successfully Signup to the system")


# create the window
root = tk.Tk()
create_window=login_page(root)
root.mainloop()
   