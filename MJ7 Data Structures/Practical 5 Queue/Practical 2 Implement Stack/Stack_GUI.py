import tkinter as tk
from tkinter import messagebox

stack = []
MAX_SIZE = 5

def push():
    if len(stack) >= MAX_SIZE:
        messagebox.showerror("Error", "Stack Overflow!")
    else:
        try:
            item = int(entry.get())
            stack.append(item)
            update_display()
            entry.delete(0, tk.END)
        except:
            messagebox.showerror("Error", "Enter a valid number!")

def pop():
    if not stack:
        messagebox.showerror("Error", "Stack Underflow!")
    else:
        item = stack.pop()
        messagebox.showinfo("Pop", f"Removed: {item}")
        update_display()

def peek():
    if not stack:
        messagebox.showerror("Error", "Stack is Empty!")
    else:
        messagebox.showinfo("Peek", f"Top Element: {stack[-1]}")

def update_display():
    display.config(state="normal")
    display.delete("1.0", tk.END)

    if not stack:
        display.insert(tk.END, "Stack is Empty")
    else:
        for item in reversed(stack):
            display.insert(tk.END, f"{item}\n")

    display.config(state="disabled")

# ---------------- GUI ----------------

root = tk.Tk()
root.title("Stack - Data Structures")
root.geometry("350x400")
root.resizable(False, False)

tk.Label(root, text="Stack Operations",
         font=("Arial", 16, "bold")).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12), justify="center")
entry.pack(pady=5)

tk.Button(root, text="Push", width=15, command=push).pack(pady=5)
tk.Button(root, text="Pop", width=15, command=pop).pack(pady=5)
tk.Button(root, text="Peek", width=15, command=peek).pack(pady=5)

tk.Label(root, text="Stack Contents",
         font=("Arial", 12, "bold")).pack(pady=10)

display = tk.Text(root, height=10, width=20,
                  state="disabled", font=("Consolas", 12))
display.pack()

root.mainloop()