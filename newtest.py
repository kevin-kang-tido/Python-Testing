import tkinter as tk 
from tkinter import messagebox

# Function to save the code

def button():
    try:
        number1 = float(Entry1.get())
        number2 = float(Entry2.get())
        sum = number1 + number2
        messagebox.showinfo("Save", "The Result of the submit: "+str(sum))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")
def bye():
    messagebox.showinfo("Bye", "Goodbye!")

def countLenght():
    try:
        letter = Entry3.get()
        length = len(letter)
        messagebox.showinfo("Save", "The Length of the submit: "+str(length))
    except ValueError:
        messagebox.showerror("Error Message", "Please enter a letter")

def addName(): 
    name = []
    try:
        name = Entry4.get()
        name.append(name)
    except ValueError:
        messagebox.showerror("Error Message", "Please enter a name")

def searchEntry():
    try:
        name = Entry5.get()
        messagebox.showinfo("Save", "The Name of the submit: "+name)
    except ValueError:
        messagebox.showerror("Error Message", "Not Found on the list")

wdw = tk.Tk()
wdw.title("This new window")
btn1 = tk.Button(wdw,text="ClicK Me",command=button)
btn2 = tk.Button(wdw,text="ClicK To Say Bye",command=bye)
btn1.pack(pady=25)
btn2.pack(pady=25)

## input the file 
inputfields = tk.Label(wdw,text="Please, Enter the number1:")
inputfields.pack(pady=25)

Entry1 = tk.Entry(wdw)
Entry1.pack(pady=5)
inputfields1 = tk.Label(wdw,text="Please enter the number2: ")
inputfields1.pack(pady=25)
Entry2 = tk.Entry(wdw)
Entry2.pack(pady=5)

ShowLenghtLetter = tk.Label(wdw,text="Please the Letter to count:")
ShowLenghtLetter.pack(pady=5)

Entry3 = tk.Entry(wdw)
Entry3.pack(pady=25)
btn3 = tk.Button(wdw,text="Click Me Count",command=countLenght)
btn3.pack(pady=25)

# add name to the list 
searchName = tk.Label(wdw,text="Add to the list:")
searchName.pack(pady=5)

Entry4 = tk.Entry(wdw)
Entry4.pack(pady=25)
btn4 = tk.Button(wdw,text="Add to List",command=addName)
btn4.pack(pady=25)

# for button search
EnterName = tk.Label(wdw,text="Add to the list:")
EnterName.pack(pady=5)

Entry5 = tk.Entry(wdw)
Entry5.pack(pady=25)
btn5 = tk.Button(wdw,text="Add to List",command=searchEntry)
btn5.pack(pady=25)


wdw.mainloop()
