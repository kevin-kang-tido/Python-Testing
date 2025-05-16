import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
import os 

  

class students_info:

    def __init__(self,name,gender,score,grade):
        self.name=name
        self.gender=gender
        self.score=score
        self.grade=grade


class student_window:

    def __init__(self,root):
        self.root=root
        self.root.title("Login Page")
        self.root.geometry("300*250")


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
        self.current_grade=""
        self.inp2.grid(row=5,column=0,pady=4,sticky="nsew")
        self.button=self.create_btn()
        self.tree=ttk.Treeview(self.root,column=("N","G","S","Gr"),show="headings")
        self.tree.heading("N",text="Name")
        self.tree.heading("G",text="Gender")
        self.tree.heading("S",text="Score")
        self.tree.heading("Gr",text="Grade")
        self.tree.grid(row=7,column=0,pady=4)
        self.data=""
        self.N_data=""
        self.names=[]
        self.students=[]
        self.load_data()

    def load_data(self):
        try:
            fileme="Names.json"
            with open(fileme, 'r') as json_file:
                self.N_data=json.load(json_file)
            self.names=json.loads(self.N_data)
            print(self.names)
        except:
            print("Error")
            fil_name_2="Names.json"
            js_string=json.dumps(self.names)
            with open(fil_name_2, 'w') as json_file:
                json.dump(js_string, json_file, indent=4)
    


        for i in range(len(self.names)):
            filename=self.names[i]+".json"
            with open(filename, 'r') as json_file:
                self.data=json.load(json_file)
            new_data=json.loads(self.data)
            stdnt=students_info(**new_data)
            self.students.append(stdnt)
            self.tree.insert("",tk.END,values=(stdnt.name,stdnt.gender,stdnt.score,stdnt.grade))
        pass
        
    def create_btn(self):
        B=tk.Button(self.root,text="input",command=lambda:self.button_pressed())
        B.grid(row=6,column=2,pady=4,sticky="nsew")
        
        C=tk.Button(self.root,text="Delete",command=lambda:self.delete_selected())
        C.grid(row=7,column=2,pady=4,sticky="nsew")

        return B ,C

    def button_pressed(self):
        name=self.inp.get()
        gender=self.dl.get()
        score=self.inp2.get()
        student=students_info(name,gender,score,self.current_grade)
        self.names.append(student.name)
        js_string=json.dumps(self.names)
        fil_name="Names.json"
        with open(fil_name, 'w') as json_file:
            json.dump(js_string, json_file, indent=4)
       
         
    
    
        js_st=json.dumps(student.__dict__,indent=4)

        print(js_st)

        fl_name=student.name+".json"
        with open(fl_name, 'w') as json_file:
            json.dump(js_st, json_file, indent=4)
        self.tree.insert("",tk.END,values=(student.name,student.gender,student.score,student.grade))
        self.inp.delete(0,tk.END)
        self.inp2.delete(0,tk.END)

    def delete_selected(self):
        # Get the selected item
        selected_item = self.tree.selection()
        
        if not selected_item:
            messagebox.showwarning("Warning", "Please select an item to delete.")
            return

        # Get the name of the selected student
        name = self.tree.item(selected_item, "values")[0]
        
        # Remove the item from the Treeview
        self.tree.delete(selected_item)
        
        # Remove the student name from the names list
        if name in self.names:
            self.names.remove(name)

        # Update Names.json
        with open("Names.json", 'w') as json_file:
            json.dump(json.dumps(self.names), json_file, indent=4)

        # Remove the corresponding JSON file for that student
        filename = name + ".json"

        if os.path.exists(filename):
            os.remove(filename)

        messagebox.showinfo("Success", f"Data for {name} has been deleted successfully.")
            
    
    def on_change(self,*args):
        try:
            value=int(self.inp2.get())
        
            if value<=50:
                self.label_4.config(text="F")
                self.current_grade="F"
            elif value>50 and value<=60:
                self.label_4.config(text="E")
                self.current_grade="E"
            elif value>60 and value<=70:
                self.label_4.config(text="D")
                self.current_grade="D"
            elif value>70 and value<=80:
                self.label_4.config(text="C")
                self.current_grade="C"
            elif value>80 and value<=90:
                self.label_4.config(text="B")
                self.current_grade="B"
            else:
                self.label_4.config(text="A")
                self.current_grade="A"
        except:
            pass


# create the windo

root = tk.Tk()
create_window=student_window(root)
root.mainloop()
   






    

