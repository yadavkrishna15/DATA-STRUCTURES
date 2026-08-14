import tkinter as tk
from tkinter import messagebox


def insert_all():
    try:
        size = int(size_entry.get())
        data = list(map(int, data_entry.get().split()))
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers.")
        return

    table = [None] * size

    for value in data:
        idx = original = value % size
        while table[idx] is not None:
            idx = (idx + 1) % size
            if idx == original:
                idx = None
                break
        if idx is not None:
            table[idx] = value

    # Show result
    result.delete(0, tk.END)
    for i, v in enumerate(table):
        result.insert(tk.END, f"Index {i}: {v}")


root = tk.Tk()
root.title("Linear Probing Hash Table")

tk.Label(root, text="Table size:").grid(row=0, column=0, padx=5, pady=5)
size_entry = tk.Entry(root, width=10)
size_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Data (space-separated):").grid(row=1, column=0, padx=5, pady=5)
data_entry = tk.Entry(root, width=30)
data_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Button(root, text="Insert", command=insert_all).grid(row=2, column=0, columnspan=2, pady=10)

result = tk.Listbox(root, width=40, height=15)
result.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
