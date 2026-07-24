import tkinter as tk
from tkinter import messagebox


class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def enqueue(self, item):
        if self.is_full():
            return "Queue is Full!"
        self.queue.append(item)
        return f"Enqueued: {item}"

    def dequeue(self):
        if self.is_empty():
            return "Queue is Empty!"
        return f"Dequeued: {self.queue.pop(0)}"

    def peek(self):
        if self.is_empty():
            return "Queue is Empty!"
        return f"Front Item: {self.queue[0]}"

    def traverse(self):
        if self.is_empty():
            return "Queue is Empty!"
        return " -> ".join(self.queue)

    def display_list(self):
        if self.is_empty():
            return "Queue is Empty!"
        return "\n".join(f"{i+1}. {item}" for i, item in enumerate(self.queue))


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Queue Operations")
root.geometry("500x600")
root.configure(bg="white")
root.resizable(False, False)

queue = None


def create_queue():
    global queue
    try:
        size = int(max_entry.get())
        queue = Queue(size)
        output.delete("1.0", tk.END)
        output.insert(tk.END, f"Queue Created (Max Size = {size})")
    except:
        messagebox.showerror("Error", "Enter a valid queue size")


def enqueue_item():
    if queue is None:
        messagebox.showwarning("Warning", "Create Queue First")
        return

    item = item_entry.get().strip()

    if item == "":
        messagebox.showwarning("Warning", "Enter an Item")
        return

    result = queue.enqueue(item)
    output.delete("1.0", tk.END)
    output.insert(tk.END, result)
    item_entry.delete(0, tk.END)


def dequeue_item():
    if queue is None:
        messagebox.showwarning("Warning", "Create Queue First")
        return

    output.delete("1.0", tk.END)
    output.insert(tk.END, queue.dequeue())


def peek_item():
    if queue is None:
        messagebox.showwarning("Warning", "Create Queue First")
        return

    output.delete("1.0", tk.END)
    output.insert(tk.END, queue.peek())


def traverse_queue():
    if queue is None:
        messagebox.showwarning("Warning", "Create Queue First")
        return

    output.delete("1.0", tk.END)
    output.insert(tk.END, queue.traverse())


def display_queue():
    if queue is None:
        messagebox.showwarning("Warning", "Create Queue First")
        return

    output.delete("1.0", tk.END)
    output.insert(tk.END, queue.display_list())


def check_empty():
    if queue is None:
        messagebox.showwarning("Warning", "Create Queue First")
        return

    if queue.is_empty():
        messagebox.showinfo("Queue", "Queue is Empty")
    else:
        messagebox.showinfo("Queue", "Queue is NOT Empty")


def check_full():
    if queue is None:
        messagebox.showwarning("Warning", "Create Queue First")
        return

    if queue.is_full():
        messagebox.showinfo("Queue", "Queue is Full")
    else:
        messagebox.showinfo("Queue", "Queue is NOT Full")


# ---------------- Widgets ---------------- #

title = tk.Label(
    root,
    text="Queue Operations",
    font=("Segoe UI", 18, "bold"),
    bg="white"
)
title.pack(pady=15)

frame1 = tk.Frame(root, bg="white")
frame1.pack()

tk.Label(frame1, text="Max Size:", bg="white",
         font=("Segoe UI", 10)).grid(row=0, column=0, padx=5)

max_entry = tk.Entry(frame1, width=8)
max_entry.grid(row=0, column=1)

tk.Button(frame1, text="Create Queue",
          command=create_queue,
          bg="#4CAF50",
          fg="white").grid(row=0, column=2, padx=10)

frame2 = tk.Frame(root, bg="white")
frame2.pack(pady=20)

tk.Label(frame2, text="Item:", bg="white",
         font=("Segoe UI", 10)).grid(row=0, column=0)

item_entry = tk.Entry(frame2, width=25)
item_entry.grid(row=0, column=1)

button_frame = tk.Frame(root, bg="white")
button_frame.pack()

buttons = [
    ("Enqueue", enqueue_item),
    ("Dequeue", dequeue_item),
    ("Peek", peek_item),
    ("Traverse", traverse_queue),
    ("Display", display_queue),
    ("Check Empty", check_empty),
    ("Check Full", check_full),
    ("Clear", lambda: output.delete("1.0", tk.END)),
]

row = 0
col = 0

for text, cmd in buttons:
    tk.Button(
        button_frame,
        text=text,
        width=15,
        height=2,
        command=cmd,
        bg="#2196F3",
        fg="white"
    ).grid(row=row, column=col, padx=5, pady=5)

    col += 1

    if col == 2:
        col = 0
        row += 1

tk.Button(
    root,
    text="Exit",
    command=root.destroy,
    width=15,
    height=2,
    bg="#F44336",
    fg="white"
).pack(pady=10)

output = tk.Text(
    root,
    width=50,
    height=12,
    font=("Consolas", 10)
)
output.pack(pady=10)

root.mainloop()