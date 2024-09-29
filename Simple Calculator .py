import tkinter as tk
from tkinter import messagebox

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_operation(operator):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + operator)

def button_equals():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for button_text, row, col in buttons:
    if button_text == 'C':
        button = tk.Button(root, text=button_text, padx=20, pady=10, command=button_clear)
    elif button_text == '=':
        button = tk.Button(root, text=button_text, padx=20, pady=10, command=button_equals)
    elif button_text in {'+', '-', '*', '/'}:
        button = tk.Button(root, text=button_text, padx=20, pady=10, command=lambda op=button_text: button_operation(op))
    else:
        button = tk.Button(root, text=button_text, padx=20, pady=10, command=lambda num=button_text: button_click(num))
    
    button.grid(row=row, column=col)

root.mainloop()




