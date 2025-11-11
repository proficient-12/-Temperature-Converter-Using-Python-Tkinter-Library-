import tkinter as tk
from tkinter import ttk, messagebox

# Function to perform temperature conversion
def convert_temperature():
    try:
        temp = float(entry_temp.get())         # Get user input
        unit_from = combo_from.get()           # Source unit
        unit_to = combo_to.get()               # Target unit

        # Conversion logic
        if unit_from == unit_to:
            result = temp
        elif unit_from == "Celsius":
            if unit_to == "Fahrenheit":
                result = (temp * 9/5) + 32
            elif unit_to == "Kelvin":
                result = temp + 273.15
        elif unit_from == "Fahrenheit":
            if unit_to == "Celsius":
                result = (temp - 32) * 5/9
            elif unit_to == "Kelvin":
                result = ((temp - 32) * 5/9) + 273.15
        elif unit_from == "Kelvin":
            if unit_to == "Celsius":
                result = temp - 273.15
            elif unit_to == "Fahrenheit":
                result = ((temp - 273.15) * 9/5) + 32

        # Display result
        label_result.config(text=f"Result: {result:.2f} °{unit_to[0]}")

    except ValueError:
        # Error message for invalid inputs
        messagebox.showerror("Invalid Input", "Please enter a valid number!")

# Create main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x350")
root.config(bg="#f2f2f2")

# Title label
label_title = tk.Label(root, text="Temperature Converter", font=("Arial", 18, "bold"), bg="#f2f2f2", fg="#333")
label_title.pack(pady=20)

# Input section
frame_entry = tk.Frame(root, bg="#f2f2f2")
frame_entry.pack(pady=10)
tk.Label(frame_entry, text="Enter Temperature:", font=("Arial", 12), bg="#f2f2f2").grid(row=0, column=0, padx=10)
entry_temp = tk.Entry(frame_entry, font=("Arial", 12), width=10)
entry_temp.grid(row=0, column=1)

# Unit selection
frame_units = tk.Frame(root, bg="#f2f2f2")
frame_units.pack(pady=15)
tk.Label(frame_units, text="From:", font=("Arial", 12), bg="#f2f2f2").grid(row=0, column=0, padx=10)
combo_from = ttk.Combobox(frame_units, values=["Celsius", "Fahrenheit", "Kelvin"], font=("Arial", 12), width=10)
combo_from.current(0)
combo_from.grid(row=0, column=1)
tk.Label(frame_units, text="To:", font=("Arial", 12), bg="#f2f2f2").grid(row=0, column=2, padx=10)
combo_to = ttk.Combobox(frame_units, values=["Celsius", "Fahrenheit", "Kelvin"], font=("Arial", 12), width=10)
combo_to.current(1)
combo_to.grid(row=0, column=3)

# Convert button
btn_convert = tk.Button(root, text="Convert", command=convert_temperature, font=("Arial", 12, "bold"),
                        bg="#4CAF50", fg="white", width=12)
btn_convert.pack(pady=20)

# Result label
label_result = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"), bg="#f2f2f2", fg="#222")
label_result.pack(pady=10)

# Footer
label_footer = tk.Label(root, text="Made with ❤️ using Tkinter", font=("Arial", 10, "italic"),
                        bg="#f2f2f2", fg="#555")
label_footer.pack(side="bottom", pady=10)

# Run the application
root.mainloop()
