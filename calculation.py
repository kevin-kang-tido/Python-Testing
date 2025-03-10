import tkinter as tk

# Functions to perform calculations and display results
def calculate_sum():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        showresult.config(text=f"Result: {result}")
    except ValueError:
        showresult.config(text="Invalid input! Please enter numbers.")

def calculate_difference():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 - num2
        showresult.config(text=f"Result: {result}")
    except ValueError:
        showresult.config(text="Invalid input! Please enter numbers.")

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        showresult.config(text=f"Result: {result}")
    except ValueError:
        showresult.config(text="Invalid input! Please enter numbers.")

# Main window
root = tk.Tk()
root.title("Simple Calculator")

# Result label
showresult = tk.Label(root, text="Result: ", width=30, height=2, bg="lightgray")
showresult.pack(pady=10)

# First number input
label1 = tk.Label(root, text="Enter the first number:")
label1.pack(pady=5)

entry1 = tk.Entry(root)
entry1.pack(pady=5)

# Second number input
label2 = tk.Label(root, text="Enter the second number:")
label2.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Buttons for operations
calc_button = tk.Button(root, text="Plus", command=calculate_sum)
calc_button.pack(pady=5)

minus_button = tk.Button(root, text="Minus", command=calculate_difference)
minus_button.pack(pady=5)

multiplication_button = tk.Button(root, text="Multiplication", command=calculate_product)
multiplication_button.pack(pady=5)

# Run the program
root.mainloop()
