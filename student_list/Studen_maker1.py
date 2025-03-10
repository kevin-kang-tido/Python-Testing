import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


#create the window
root = tk.Tk()
root.title("Student Form")


def button_pressed():


    pass

#create a label

label=tk.Label(root, text="Student name")
label.grid(row=0,column=0,pady=4,sticky="nsew")

# # this is input filde 
# entry1 = tk.Entry(root)
# entry1.grid(row=1,column=0,sticky="nsew")



#create an input
inp=tk.Entry(root)
inp.grid(row=2,column=0,sticky="nsew")


# create a button
B=tk.Button(root,text="Click Me!",command=lambda:button_pressed())
B.grid(row=8,column=0,pady=4,sticky="nsew")


#Creating a drop list
label=tk.Label(root, text="Student name")
label.grid(row=0,column=0,pady=4,sticky="nsew")


label=tk.Label(root, text="Student Gender")
label.grid(row=4,column=0,pady=24,sticky="nsew")

options=["Male","Female"]
dl=ttk.Combobox(root,values=options)
dl.grid(row=5,column=0)
#get the current option
selected_option=dl.get()

label=tk.Label(root, text="Student Score")
label.grid(row=6,column=0,pady=24,sticky="nsew")

#create an input
inp=tk.Entry(root)
inp.grid(row=7,column=0,sticky="nsew")


  
#get the label text
txt=label.cget("text")
       
          
#set the label text        
label.config(text=txt)
        
        
   

root.mainloop()
