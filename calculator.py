import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display the expressions
entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Function to update the entry widget
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Function to clear the entry widget
def button_clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Define the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Arrange buttons in a grid
row_val = 1
col_val = 0
for button in buttons:
    if button == 'C':
        tk.Button(root, text=button, padx=40, pady=20, command=button_clear).grid(row=row_val, column=col_val)
    elif button == '=':
        tk.Button(root, text=button, padx=40, pady=20, command=button_equal).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, padx=40, pady=20, command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the application
root.mainloop()
