# Student form using tkinter widgets
import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    if not name or not age or not gender:
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return
    messagebox.showinfo("Form Submitted", f"Name: {name}\nAge: {age}\nGender: {gender}")

root = tk.Tk()
root.title("Student Form")
root.geometry("400x400")

# Name
tk.Label(root, text="Name:").pack(pady=(10,0))
entry_name = tk.Entry(root)
entry_name.pack()

# Age
tk.Label(root, text="Age:").pack(pady=(10,0))
entry_age = tk.Entry(root)
entry_age.pack()

# Gender
tk.Label(root, text="Gender:").pack(pady=(10,0))
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other").pack()

#colleges name using dropdown
# Listbox for college selection
tk.Label(root, text="Select College:").pack(pady=(10,0))
listbox = tk.Listbox(root, height=5)
listbox.insert(1, "SKNCOE")
listbox.insert(2, "PVG")
listbox.insert(3, "D.Y. Patil")
listbox.insert(4, "JSPM")
listbox.pack(pady=(0,10))
# Listbox for college selection
# Colleges name
#colleges name
listbox.insert(5, "TSSM")
listbox.insert(6, "MIT")
listbox.insert(7, "Vishwakarma")


# Submit Button
tk.Button(root, text="Submit", command=submit_form).pack(pady=15)

root.mainloop()
