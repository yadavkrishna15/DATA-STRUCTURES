import tkinter as tk


class Number:
    def __init__(self, value):
        self.value = value
        self.next_number = None


class NumberList:
    def __init__(self):
        self.first_number = None

    def add_number(self, value):
        num = Number(value)
        if not self.first_number:
            self.first_number = num
            return
        cur = self.first_number
        while cur.next_number:
            cur = cur.next_number
        cur.next_number = num

    def remove_number(self, value):
        cur, prev = self.first_number, None
        while cur:
            if cur.value == value:
                if prev:
                    prev.next_number = cur.next_number
                else:
                    self.first_number = cur.next_number
                return
            prev, cur = cur, cur.next_number

    def as_list(self):
        values = []
        cur = self.first_number
        while cur:
            values.append(cur.value)
            cur = cur.next_number
        return values


# --- Colors (just 3) ---
BG = "#ffffff"
PRIMARY = "#4a90e2"
PRIMARY_DARK = "#357abd"

number_list = NumberList()

root = tk.Tk()
root.title("Number Chain")
root.geometry("280x420")
root.configure(bg=BG)

tk.Label(root, text="Number Chain", font=("Arial", 16, "bold"), bg=PRIMARY, fg="white", pady=10).pack(fill="x")

entry = tk.Entry(root, font=("Arial", 13), justify="center")
entry.pack(pady=10, padx=20, fill="x")

listbox = tk.Listbox(root, font=("Arial", 12), bg=BG, fg=PRIMARY_DARK, justify="center")
listbox.pack(pady=5, padx=20, fill="both", expand=True)


def refresh():
    listbox.delete(0, tk.END)
    for value in number_list.as_list():
        listbox.insert(tk.END, value)


def add_number():
    text = entry.get().strip()
    if text.lstrip("-").isdigit():
        number_list.add_number(int(text))
        entry.delete(0, tk.END)
        refresh()


def remove_number():
    selection = listbox.curselection()
    if selection:
        value = int(listbox.get(selection[0]))
        number_list.remove_number(value)
        refresh()


entry.bind("<Return>", lambda e: add_number())

tk.Button(root, text="Add", font=("Arial", 11, "bold"), bg=PRIMARY, fg="white", relief="flat", command=add_number).pack(pady=5, padx=20, fill="x")
tk.Button(root, text="Remove Selected", font=("Arial", 11, "bold"), bg=PRIMARY_DARK, fg="white", relief="flat", command=remove_number).pack(pady=5, padx=20, fill="x")

root.mainloop()
