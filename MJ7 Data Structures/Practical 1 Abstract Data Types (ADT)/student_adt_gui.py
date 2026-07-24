import tkinter as tk
from tkinter import messagebox

students = []

def create():
    roll = roll_entry.get()
    name = name_entry.get()
    age = age_entry.get()

    students.append([roll, name, age])
    messagebox.showinfo("Success", "Student Added")
    display()

def update():
    roll = roll_entry.get()

    for s in students:
        if s[0] == roll:
            s[1] = name_entry.get()
            s[2] = age_entry.get()
            messagebox.showinfo("Success", "Student Updated")
            display()
            return

    messagebox.showerror("Error", "Student Not Found")

def delete():
    roll = roll_entry.get()

    for s in students:
        if s[0] == roll:
            students.remove(s)
            messagebox.showinfo("Success", "Student Deleted")
            display()
            return

    messagebox.showerror("Error", "Student Not Found")

def display():
    listbox.delete(0, tk.END)

    for s in students:
        listbox.insert(tk.END, f"Roll: {s[0]}  Name: {s[1]}  Age: {s[2]}")

root = tk.Tk()
root.title("Student ADT")
root.geometry("400x450")

tk.Label(root, text="Roll No").pack()
roll_entry = tk.Entry(root)
roll_entry.pack()

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Button(root, text="Create", command=create).pack(pady=5)
tk.Button(root, text="Update", command=update).pack(pady=5)
tk.Button(root, text="Delete", command=delete).pack(pady=5)
tk.Button(root, text="Display", command=display).pack(pady=5)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

root.mainloop()