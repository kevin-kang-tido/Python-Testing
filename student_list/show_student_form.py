import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
import os


class Student:
    def __init__(self, name, gender, score, grade):
        self.name = name
        self.gender = gender
        self.score = score
        self.grade = grade

    def get_student_data(self):
        return self.name, self.gender, self.score, self.grade

class StudentWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Information")
        self.students = []  # List to store student objects
        self.file_path = r"C:\Users\kang\Desktop\Python-PPUA\student_list\Studen.json"
        
        self.label = tk.Label(self.root, text="Student Name")
        self.label.grid(row=0, column=0, pady=4, sticky="w")
        self.inp_name = tk.Entry(self.root)
        self.inp_name.grid(row=0, column=1, sticky="ew")
        
        self.label_2 = tk.Label(self.root, text="Gender")
        self.label_2.grid(row=1, column=0, pady=4, sticky="w")
        self.options = ["Male", "Female"]
        self.gender_combo = ttk.Combobox(self.root, values=self.options)
        self.gender_combo.grid(row=1, column=1)
        
        self.label_3 = tk.Label(self.root, text="Score")
        self.label_3.grid(row=2, column=0, pady=4, sticky="w")
        self.score_var = tk.StringVar()
        self.score_var.trace_add("write", self.on_change)
        self.inp_score = tk.Entry(self.root, textvariable=self.score_var)
        self.inp_score.grid(row=2, column=1, pady=4, sticky="ew")
        
        self.label_4 = tk.Label(self.root, text="Grade: N/A")
        self.label_4.grid(row=3, column=1, pady=4, sticky="w")
        
        self.submit_btn = tk.Button(self.root, text="Submit", command=self.save_student)
        self.submit_btn.grid(row=4, column=1, pady=4, sticky="ew")
        
        self.display_btn = tk.Button(self.root, text="Display Students", command=self.display_students)
        self.display_btn.grid(row=5, column=1, pady=4, sticky="ew")
        
        # change text area to tree 
        self.tree = ttk.Treeview(self.root, columns=("Name", "Gender", "Score", "Grade"), show="headings")
        self.tree.grid(row=6, column=0, columnspan=2, pady=4)
        self.tree.heading("Name", text="Name")
        self.tree.heading("Gender", text="Gender")
        self.tree.heading("Score", text="Score")
        self.tree.heading("Grade", text="Grade")

        ## TODO: load student information from the json file 
        self.load_students()


    def on_change(self, *args):
        try:
            value = int(self.inp_score.get())
            if value <= 50:
                grade = "F"
            elif value <= 60:
                grade = "E"
            elif value <= 70:
                grade = "D"
            elif value <= 80:
                grade = "C"
            elif value <= 90:
                grade = "B"
            else:
                grade = "A"
            self.label_4.config(text=f"Grade: {grade}")
        except ValueError:
            self.label_4.config(text="Grade: N/A")

    def save_student(self):
        name = self.inp_name.get().strip()
        gender = self.gender_combo.get().strip()
        try:
            score = int(self.inp_score.get().strip())
        except ValueError:
            messagebox.showerror("Input Error", "Score must be a number")

            return
        grade = self.label_4.cget("text").split(": ")[1]

        if name and gender and grade != "N/A":
            student = Student(name, gender, score, grade)
            # print(student)
            self.students.append(student)

            self.save_student_json()  # Save to JSON file

            messagebox.showinfo("Success", "Student added successfully!")
            self.clear_fields()
        else:
            messagebox.showerror("Input Error", "Please fill all fields correctly")
        
    def display_students(self):
        # Clear existing rows in the Treeview
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        if not self.students:
            messagebox.showinfo("Info", "No students available!")
        else:
            for student in self.students:
                self.tree.insert("", tk.END, values=(student.name, student.gender, student.score, student.grade))
     ## TODO: save student to the json file 
    def save_student_json(self):
        # Save data to a file or database
        student_data = [student.get_student_data() for student in self.students]
      # Ensure directory exists
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        with open(self.file_path, "w") as f:
            json.dump(student_data, f, indent=4)
   
    def load_students(self):
        ## TODO: """Loads student data from the JSON file if it exists."""
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                try:
                    data = json.load(f)
                    self.students = [Student(**student) for student in data]
                except json.JSONDecodeError:
                    self.students = []

    def clear_fields(self):
        self.inp_name.delete(0, tk.END)
        self.inp_score.delete(0, tk.END)
        self.gender_combo.set("")
        self.label_4.config(text="Grade: N/A")
    # Loading the data

# Create the window
root = tk.Tk()
app = StudentWindow(root)
root.mainloop()
