import tkinter as tk

# The part for functions
def button_pressed(char):
    text = label1.cget("text")  
    global txt 
    if char == "C":
        label1.config(text="") 
        txt = ""  
    elif char == "=":
        try:
            label1.config(text=str(eval(txt)))  # Evaluate the expression and show result
            txt = label1.cget("text")  # Store result in txt
        except:
            label1.config(text="Error")  # In case of invalid expression
    else:
        txt += char  # Append the pressed button's character
        label1.config(text=txt)

# Main window setup
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("500x500")

txt = ""  # Initialize txt as an empty string

label1 = tk.Label(root, text="", font=("Arial", 24), anchor="e", bg="white", height=2)
label1.grid(row=0, column=0, columnspan=4, pady=2, sticky="nsew")

# Button values (same as before but now corrected)
charts = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "+", "*", "/", "C", "="]

# Button creation and placement
B1 = tk.Button(root, text="1", command=lambda: button_pressed(charts[1]))
B1.grid(row=1, column=0, pady=2, sticky="nsew")

B2 = tk.Button(root, text="2", command=lambda: button_pressed(charts[2]))
B2.grid(row=1, column=1, pady=2, sticky="nsew")

B3 = tk.Button(root, text="3", command=lambda: button_pressed(charts[3]))
B3.grid(row=1, column=2, pady=2, sticky="nsew")

B4 = tk.Button(root, text="-", command=lambda: button_pressed(charts[10]))
B4.grid(row=1, column=3, pady=2, sticky="nsew")

B5 = tk.Button(root, text="4", command=lambda: button_pressed(charts[4]))
B5.grid(row=2, column=0, pady=2, sticky="nsew")

B6 = tk.Button(root, text="5", command=lambda: button_pressed(charts[5]))
B6.grid(row=2, column=1, pady=2, sticky="nsew")

B7 = tk.Button(root, text="6", command=lambda: button_pressed(charts[6]))
B7.grid(row=2, column=2, pady=2, sticky="nsew")

B8 = tk.Button(root, text="+", command=lambda: button_pressed(charts[11]))
B8.grid(row=2, column=3, pady=2, sticky="nsew")

B9 = tk.Button(root, text="7", command=lambda: button_pressed(charts[7]))
B9.grid(row=3, column=0, pady=2, sticky="nsew")

B10 = tk.Button(root, text="8", command=lambda: button_pressed(charts[8]))
B10.grid(row=3, column=1, pady=2, sticky="nsew")

B11 = tk.Button(root, text="9", command=lambda: button_pressed(charts[9]))
B11.grid(row=3, column=2, pady=2, sticky="nsew")

B12 = tk.Button(root, text="*", command=lambda: button_pressed(charts[12]))
B12.grid(row=3, column=3, pady=2, sticky="nsew")

B13 = tk.Button(root, text="0", command=lambda: button_pressed(charts[0]))
B13.grid(row=4, column=1, pady=2, sticky="nsew")

B14 = tk.Button(root, text="C", command=lambda: button_pressed(charts[14]))
B14.grid(row=4, column=0, pady=2, sticky="nsew")

B15 = tk.Button(root, text="=", command=lambda: button_pressed(charts[15]))
B15.grid(row=4, column=2, pady=2, sticky="nsew")

# Ensure grid resizing
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Run the program
root.mainloop()
