import tkinter as tk
from tkinter import messagebox, simpledialog
from airport_boarding_priority_queue import PriorityQueue

# ---------------- Window ---------------- #

root = tk.Tk()
root.title("Airport Boarding Priority Queue")
root.geometry("850x600")
root.configure(bg="#E3F2FD")
root.resizable(False, False)

# ---------------- Queue ---------------- #

capacity = simpledialog.askinteger(
    "Queue Capacity",
    "Enter Maximum Boarding Queue Capacity:",
    minvalue=1
)

if capacity is None:
    root.destroy()
    exit()

pq = PriorityQueue(capacity)

# ---------------- Title ---------------- #

title = tk.Label(
    root,
    text="✈ AIRPORT BOARDING PRIORITY QUEUE ✈",
    font=("Arial", 18, "bold"),
    bg="#1565C0",
    fg="white",
    pady=10
)
title.pack(fill="x")

# ---------------- Output Box ---------------- #

output = tk.Text(
    root,
    width=90,
    height=18,
    font=("Consolas", 11),
    bg="white",
    fg="black"
)
output.pack(pady=20)

# ---------------- Helper Function ---------------- #

def display(text):
    output.insert(tk.END, text + "\n")
    output.see(tk.END)

# ---------------- Button Functions ---------------- #

def add_passenger():
    passenger = simpledialog.askstring(
        "Passenger",
        "Enter Passenger Name:"
    )

    if not passenger:
        return

    priority = simpledialog.askinteger(
        "Priority",
        "Enter Priority (1 = Highest):"
    )

    if priority is None:
        return

    if pq.is_full():
        messagebox.showerror(
            "Error",
            "Boarding Queue is Full!"
        )
        return

    pq.enqueue(passenger, priority)
    display(f"Added : {passenger}   Priority : {priority}")


def board_passenger():
    if pq.is_empty():
        messagebox.showwarning(
            "Warning",
            "Boarding Queue is Empty!"
        )
        return

    passenger = pq.dequeue()

    display(f"Boarded : {passenger}")


def show_queue():

    output.delete(1.0, tk.END)

    if pq.is_empty():
        display("Boarding Queue is Empty")
        return

    display("Current Boarding Queue")
    display("-" * 45)

    for passenger, priority in pq.queue:
        display(f"{passenger}    Priority : {priority}")


def check_empty():

    if pq.is_empty():
        messagebox.showinfo(
            "Queue Status",
            "Queue is Empty."
        )
    else:
        messagebox.showinfo(
            "Queue Status",
            "Queue is NOT Empty."
        )


def check_full():

    if pq.is_full():
        messagebox.showinfo(
            "Queue Status",
            "Queue is Full."
        )
    else:
        messagebox.showinfo(
            "Queue Status",
            "Queue is NOT Full."
        )
# ---------------- More Functions ---------------- #

def show_ascending():
    output.delete(1.0, tk.END)

    if pq.is_empty():
        display("Boarding Queue is Empty")
        return

    display("Passengers (Highest Priority First)")
    display("-" * 45)

    for passenger, priority in sorted(pq.queue, key=lambda x: x[1]):
        display(f"{passenger}    Priority : {priority}")


def show_descending():
    output.delete(1.0, tk.END)

    if pq.is_empty():
        display("Boarding Queue is Empty")
        return

    display("Passengers (Lowest Priority First)")
    display("-" * 45)

    for passenger, priority in sorted(pq.queue, key=lambda x: x[1], reverse=True):
        display(f"{passenger}    Priority : {priority}")


def clear_output():
    output.delete(1.0, tk.END)


# ---------------- Buttons ---------------- #

button_frame = tk.Frame(root, bg="#E3F2FD")
button_frame.pack(pady=10)

btn_add = tk.Button(
    button_frame,
    text="Add Passenger",
    width=18,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 10, "bold"),
    command=add_passenger
)
btn_add.grid(row=0, column=0, padx=5, pady=5)

btn_board = tk.Button(
    button_frame,
    text="Board Passenger",
    width=18,
    bg="#2196F3",
    fg="white",
    font=("Arial", 10, "bold"),
    command=board_passenger
)
btn_board.grid(row=0, column=1, padx=5, pady=5)

btn_display = tk.Button(
    button_frame,
    text="Display Queue",
    width=18,
    bg="#009688",
    fg="white",
    font=("Arial", 10, "bold"),
    command=show_queue
)
btn_display.grid(row=0, column=2, padx=5, pady=5)

btn_empty = tk.Button(
    button_frame,
    text="Check Empty",
    width=18,
    bg="#FF9800",
    fg="white",
    font=("Arial", 10, "bold"),
    command=check_empty
)
btn_empty.grid(row=1, column=0, padx=5, pady=5)

btn_full = tk.Button(
    button_frame,
    text="Check Full",
    width=18,
    bg="#9C27B0",
    fg="white",
    font=("Arial", 10, "bold"),
    command=check_full
)
btn_full.grid(row=1, column=1, padx=5, pady=5)

btn_asc = tk.Button(
    button_frame,
    text="Ascending Order",
    width=18,
    bg="#3F51B5",
    fg="white",
    font=("Arial", 10, "bold"),
    command=show_ascending
)
btn_asc.grid(row=1, column=2, padx=5, pady=5)

btn_desc = tk.Button(
    button_frame,
    text="Descending Order",
    width=18,
    bg="#795548",
    fg="white",
    font=("Arial", 10, "bold"),
    command=show_descending
)
btn_desc.grid(row=2, column=0, padx=5, pady=5)

btn_clear = tk.Button(
    button_frame,
    text="Clear Output",
    width=18,
    bg="#607D8B",
    fg="white",
    font=("Arial", 10, "bold"),
    command=clear_output
)
btn_clear.grid(row=2, column=1, padx=5, pady=5)

btn_exit = tk.Button(
    button_frame,
    text="Exit",
    width=18,
    bg="#F44336",
    fg="white",
    font=("Arial", 10, "bold"),
    command=root.destroy
)
btn_exit.grid(row=2, column=2, padx=5, pady=5)

# ---------------- Footer ---------------- #

footer = tk.Label(
    root,
    text="Data Structures Practical 6 - Airport Boarding Priority Queue",
    bg="#1565C0",
    fg="white",
    font=("Arial", 10)
)
footer.pack(side="bottom", fill="x")

# ---------------- Run Application ---------------- #

root.mainloop()
