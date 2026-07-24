import tkinter as tk


class Book:
    def __init__(self, title):
        self.title = title
        self.next_book = None


class Bookshelf:
    def __init__(self):
        self.first_book = None

    def add_book(self, title):
        book = Book(title)
        if not self.first_book:
            self.first_book = book
            return
        cur = self.first_book
        while cur.next_book:
            cur = cur.next_book
        cur.next_book = book

    def remove_book(self, title):
        cur, prev = self.first_book, None
        while cur:
            if cur.title == title:
                if prev:
                    prev.next_book = cur.next_book
                else:
                    self.first_book = cur.next_book
                return
            prev, cur = cur, cur.next_book

    def as_list(self):
        titles = []
        cur = self.first_book
        while cur:
            titles.append(cur.title)
            cur = cur.next_book
        return titles


# --- Colors (just 3) ---
BG = "#fdf6ec"
PRIMARY = "#6d4c41"
PRIMARY_LIGHT = "#a1887f"

shelf = Bookshelf()

root = tk.Tk()
root.title("My Bookshelf")
root.geometry("300x430")
root.configure(bg=BG)

tk.Label(root, text="📚 My Bookshelf", font=("Arial", 16, "bold"), bg=PRIMARY, fg="white", pady=10).pack(fill="x")

entry = tk.Entry(root, font=("Arial", 12), justify="center")
entry.pack(pady=10, padx=20, fill="x")

listbox = tk.Listbox(root, font=("Arial", 12), bg=BG, fg=PRIMARY)
listbox.pack(pady=5, padx=20, fill="both", expand=True)


def refresh():
    listbox.delete(0, tk.END)
    for title in shelf.as_list():
        listbox.insert(tk.END, title)


def add_book():
    title = entry.get().strip()
    if title:
        shelf.add_book(title)
        entry.delete(0, tk.END)
        refresh()


def remove_book():
    selection = listbox.curselection()
    if selection:
        title = listbox.get(selection[0])
        shelf.remove_book(title)
        refresh()


entry.bind("<Return>", lambda e: add_book())

tk.Button(root, text="Add Book", font=("Arial", 11, "bold"), bg=PRIMARY, fg="white", relief="flat", command=add_book).pack(pady=5, padx=20, fill="x")
tk.Button(root, text="Remove Selected", font=("Arial", 11, "bold"), bg=PRIMARY_LIGHT, fg="white", relief="flat", command=remove_book).pack(pady=5, padx=20, fill="x")

root.mainloop()
