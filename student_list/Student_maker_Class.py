import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


## create a class that store all student information

class Student:
    def __init__(self, name, gender, score, grade):
        self.name=name
        self.gender=gender
        self.score=score
        self.grade=grade
    
    def get_student_data(self):
        print(self.name, self.gender, self.score, self.grade)
        return self.name, self.gender, self.score, self.grade
    

class student_window:

    def __init__(self,root):
        self.root=root
        self.label=tk.Label(self.root, text="Student name")
        self.label.grid(row=0,column=0,pady=4,sticky="nsew")
        self.inp=tk.Entry(self.root)
        self.inp.grid(row=1,column=0,sticky="nsew")

        self.label_2=tk.Label(self.root, text="Gender")
        self.label_2.grid(row=2,column=0,pady=4,sticky="nsew")
        self.options=["Male","Female"]
        self.dl=ttk.Combobox(self.root,values=self.options)
        self.dl.grid(row=3,column=0)

        self.label_3=tk.Label(self.root, text="Score")
        self.label_3.grid(row=4,column=0,pady=4,sticky="nsew")
        self.label_4=tk.Label(self.root, text="Grade")
        self.label_4.grid(row=5,column=1,pady=4,sticky="nsew")

        self.str_var=tk.StringVar()
        self.str_var.trace_add("write",self.on_change)
        self.inp2=tk.Entry(self.root,textvariable=self.str_var)
    

        self.inp2.grid(row=5,column=0,pady=4,sticky="nsew")
        self.button=self.create_btn()

        
        

    def create_btn(self):
        B=tk.Button(self.root,text="input",command=lambda:self.button_pressed())
        B.grid(row=6,column=2,pady=4,sticky="nsew")
        return B

    def button_pressed(self):
        self.inp.delete(0,tk.END)
        self.inp2.delete(0,tk.END)

    def on_change(self,*args):
        try:
            value=int(self.inp2.get())
        
            if value<=50:
                self.label_4.config(text="F")
            elif value>50 and value<=60:
                self.label_4.config(text="E")
            elif value>60 and value<=70:
                self.label_4.config(text="D")
            elif value>70 and value<=80:
                self.label_4.config(text="C")
            elif value>80 and value<=90:
                self.label_4.config(text="B")
            else:
                self.label_4.config(text="A")
        except:
            pass
        
    # def save_student_data(self):
        
    



#create the window
root = tk.Tk()
create_window=student_window(root)
root.mainloop()



        
        
   






    





root.mainloop()
