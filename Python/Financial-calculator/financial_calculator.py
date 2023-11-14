import tkinter as tk
from tkinter import ttk

def calculate_simple_interest(principal, rate, time):
    return principal * rate * time / 100

def calculate_compound_interest(principal, rate, time):
    return principal * (1 + rate/100)**time - principal

def calculate():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())

        if interest_type.get() == "Simple Interest":
            result = calculate_simple_interest(principal, rate, time)
        elif interest_type.get() == "Compound Interest":
            result = calculate_compound_interest(principal, rate, time)
        else:
            result = 0

        result_label.config(text=f"Interest: R{result:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

# GUI Setup
root = tk.Tk()
root.title("Financial Calculator")

# Widgets
principal_label = ttk.Label(root, text="Principal:")
rate_label = ttk.Label(root, text="Interest Rate:")
time_label = ttk.Label(root, text="Time (years):")

principal_entry = ttk.Entry(root)
rate_entry = ttk.Entry(root)
time_entry = ttk.Entry(root)

interest_type_label = ttk.Label(root, text="Select Interest Type:")
interest_type = ttk.Combobox(root, values=["Simple Interest", "Compound Interest"])
interest_type.set("Simple Interest")

calculate_button = ttk.Button(root, text="Calculate", command=calculate)

result_label = ttk.Label(root, text="Interest:")

# Grid Layout
principal_label.grid(row=0, column=0, padx=10, pady=10)
rate_label.grid(row=1, column=0, padx=10, pady=10)
time_label.grid(row=2, column=0, padx=10, pady=10)

principal_entry.grid(row=0, column=1, padx=10, pady=10)
rate_entry.grid(row=1, column=1, padx=10, pady=10)
time_entry.grid(row=2, column=1, padx=10, pady=10)

interest_type_label.grid(row=3, column=0, columnspan=2, pady=10)
interest_type.grid(row=4, column=0, columnspan=2, pady=10)

calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

result_label.grid(row=6, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()