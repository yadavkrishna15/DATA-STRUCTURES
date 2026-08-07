import heapq
import time
import tkinter as tk
from tkinter import messagebox, ttk


# ---------------------------
# Part 1: AVL Tree Logic
# ---------------------------
class AVLNode:

    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:

    def __init__(self, log_callback=None):
        self.log = log_callback or (lambda msg, tag="WHITE": print(msg))

    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(
            self.get_height(root.left), self.get_height(root.right)
        )
        balance = self.get_balance(root)

        # Left Heavy
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        # Right Heavy
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        # Left-Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Right-Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.left_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(
            self.get_height(z.left), self.get_height(z.right)
        )
        y.height = 1 + max(
            self.get_height(y.left), self.get_height(y.right)
        )
        self.log(f"  ↪ Left Rotation on Node {z.key}", "YELLOW")
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(
            self.get_height(z.left), self.get_height(z.right)
        )
        y.height = 1 + max(
            self.get_height(y.left), self.get_height(y.right)
        )
        self.log(f"  ↪ Right Rotation on Node {z.key}", "YELLOW")
        return y

    def get_height(self, root):
        return root.height if root else 0

    def get_balance(self, root):
        return (
            self.get_height(root.left) - self.get_height(root.right)
            if root
            else 0
        )

    def pre_order(self, root, result=None):
        if result is None:
            result = []
        if root:
            result.append(str(root.key))
            self.pre_order(root.left, result)
            self.pre_order(root.right, result)
        return result


# ---------------------------
# Part 2: Heap Helpers
# ---------------------------
def process_min_heap(data_list):
    min_h = data_list.copy()
    heapq.heapify(min_h)
    return min_h


def process_max_heap(data_list):
    max_h = [-x for x in data_list]
    heapq.heapify(max_h)
    return [-x for x in max_h]


# ---------------------------
# Part 3: Task Manager Class
# ---------------------------
class TaskManager:

    def __init__(self):
        self.pq = []

    def add_task(self, priority, description):
        heapq.heappush(self.pq, (priority, description))

    def get_next_task(self):
        if self.pq:
            return heapq.heappop(self.pq)
        return None


# ---------------------------
# Main GUI Interface Application
# ---------------------------
class InteractiveApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Data Structures Interactive Visualizer")
        self.geometry("800x700")
        self.configure(bg="#1e1e1e")

        self.avl_root = None
        self.avl_tree = AVLTree(log_callback=self.print_text)
        self.task_manager = TaskManager()

        self.setup_ui()

    def setup_ui(self):
        # Header
        header = tk.Label(
            self,
            text="Data Structures Simulator (User Input)",
            font=("Consolas", 15, "bold"),
            fg="#007acc",
            bg="#1e1e1e",
        )
        header.pack(pady=5)

        # Tab Window
        notebook = ttk.Notebook(self)
        notebook.pack(fill="x", padx=15, pady=5)

        # TAB 1: AVL Tree Inputs
        tab_avl = tk.Frame(notebook, bg="#252526")
        notebook.add(tab_avl, text=" 1. AVL Tree ")

        lbl_avl = tk.Label(
            tab_avl,
            text="Enter numbers (comma separated):",
            fg="#dcdcdc",
            bg="#252526",
            font=("Consolas", 10),
        )
        lbl_avl.pack(anchor="w", padx=10, pady=(5, 0))

        self.entry_avl = tk.Entry(
            tab_avl, font=("Consolas", 11), bg="#1e1e1e", fg="white"
        )
        self.entry_avl.insert(0, "20, 4, 15, 70, 50, 100, 80")
        self.entry_avl.pack(fill="x", padx=10, pady=5)

        btn_avl = tk.Button(
            tab_avl,
            text="Build AVL Tree",
            bg="#0e639c",
            fg="white",
            font=("Consolas", 10, "bold"),
            command=self.run_avl_input,
        )
        btn_avl.pack(fill="x", padx=10, pady=5)

        # TAB 2: Heap Inputs
        tab_heap = tk.Frame(notebook, bg="#252526")
        notebook.add(tab_heap, text=" 2. Min/Max Heap ")

        lbl_heap = tk.Label(
            tab_heap,
            text="Enter numbers (comma separated):",
            fg="#dcdcdc",
            bg="#252526",
            font=("Consolas", 10),
        )
        lbl_heap.pack(anchor="w", padx=10, pady=(5, 0))

        self.entry_heap = tk.Entry(
            tab_heap, font=("Consolas", 11), bg="#1e1e1e", fg="white"
        )
        self.entry_heap.insert(0, "9, 5, 6, 2, 3")
        self.entry_heap.pack(fill="x", padx=10, pady=5)

        btn_heap = tk.Button(
            tab_heap,
            text="Build Min & Max Heap",
            bg="#0e639c",
            fg="white",
            font=("Consolas", 10, "bold"),
            command=self.run_heap_input,
        )
        btn_heap.pack(fill="x", padx=10, pady=5)

        # TAB 3: Priority Queue Inputs
        tab_task = tk.Frame(notebook, bg="#252526")
        notebook.add(tab_task, text=" 3. Task Manager ")

        frame_task_input = tk.Frame(tab_task, bg="#252526")
        frame_task_input.pack(fill="x", padx=10, pady=5)

        tk.Label(
            frame_task_input,
            text="Priority (1=High):",
            fg="#dcdcdc",
            bg="#252526",
            font=("Consolas", 9),
        ).grid(row=0, column=0, sticky="w")
        self.entry_prio = tk.Entry(
            frame_task_input,
            width=8,
            font=("Consolas", 10),
            bg="#1e1e1e",
            fg="white",
        )
        self.entry_prio.grid(row=0, column=1, padx=5)

        tk.Label(
            frame_task_input,
            text="Task Description:",
            fg="#dcdcdc",
            bg="#252526",
            font=("Consolas", 9),
        ).grid(row=0, column=2, sticky="w")
        self.entry_desc = tk.Entry(
            frame_task_input, font=("Consolas", 10), bg="#1e1e1e", fg="white"
        )
        self.entry_desc.grid(row=0, column=3, padx=5, sticky="ew")
        frame_task_input.grid_columnconfigure(3, weight=1)

        btn_add_task = tk.Button(
            tab_task,
            text="Add Task to Priority Queue",
            bg="#0e639c",
            fg="white",
            font=("Consolas", 10, "bold"),
            command=self.add_task_input,
        )
        btn_add_task.pack(fill="x", padx=10, pady=2)

        btn_run_tasks = tk.Button(
            tab_task,
            text="Process All Tasks",
            bg="#388a34",
            fg="white",
            font=("Consolas", 10, "bold"),
            command=self.process_tasks,
        )
        btn_run_tasks.pack(fill="x", padx=10, pady=2)

        # Console Output Screen
        console_frame = tk.Frame(self, bg="#1e1e1e")
        console_frame.pack(fill="both", expand=True, padx=15, pady=10)

        self.console = tk.Text(
            console_frame,
            font=("Consolas", 11),
            bg="#252526",
            fg="#dcdcdc",
            wrap="word",
        )
        scrollbar = ttk.Scrollbar(
            console_frame, orient="vertical", command=self.console.yview
        )
        self.console.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.console.pack(side="left", fill="both", expand=True)

        # Color Tags
        self.console.tag_config("BLUE", foreground="#569cd6")
        self.console.tag_config("YELLOW", foreground="#dcdcaa")
        self.console.tag_config("GREEN", foreground="#6a9955")
        self.console.tag_config("CYAN", foreground="#4ec9b0")
        self.console.tag_config("WHITE", foreground="#ffffff")

        self.print_text("Select a tab above and enter custom inputs!\n", "CYAN")

    def print_text(self, text, tag="WHITE"):
        self.console.insert("end", text + "\n", tag)
        self.console.see("end")
        self.update()

    def run_avl_input(self):
        try:
            raw = self.entry_avl.get()
            nums = [int(x.strip()) for x in raw.split(",") if x.strip()]
        except ValueError:
            messagebox.showerror(
                "Error", "Please enter valid comma-separated integers."
            )
            return

        self.print_text("\n=== AVL Tree Insertion & Balancing ===", "BLUE")
        self.avl_root = None
        for val in nums:
            self.print_text(f"Inserting {val}...", "CYAN")
            self.avl_root = self.avl_tree.insert(self.avl_root, val)
            time.sleep(0.2)

        traversal = " ".join(self.avl_tree.pre_order(self.avl_root))
        self.print_text("AVL Pre-Order Traversal:", "GREEN")
        self.print_text(f"➜ {traversal}\n", "WHITE")

    def run_heap_input(self):
        try:
            raw = self.entry_heap.get()
            nums = [int(x.strip()) for x in raw.split(",") if x.strip()]
        except ValueError:
            messagebox.showerror(
                "Error", "Please enter valid comma-separated integers."
            )
            return

        self.print_text("\n=== Min & Max Heap Construction ===", "BLUE")
        self.print_text(f"User Inputs: {nums}", "WHITE")

        min_res = process_min_heap(nums)
        self.print_text(f"Min-Heap Result: {min_res}", "GREEN")

        max_res = process_max_heap(nums)
        self.print_text(f"Max-Heap Result: {max_res}\n", "GREEN")

    def add_task_input(self):
        prio = self.entry_prio.get().strip()
        desc = self.entry_desc.get().strip()

        if not prio.isdigit() or not desc:
            messagebox.showwarning(
                "Warning", "Enter a valid integer priority and description!"
            )
            return

        self.task_manager.add_task(int(prio), desc)
        self.print_text(
            f"Added Task: [Priority {prio}] -> {desc}", "YELLOW"
        )
        self.entry_prio.delete(0, "end")
        self.entry_desc.delete(0, "end")

    def process_tasks(self):
        if not self.task_manager.pq:
            messagebox.showinfo("Info", "No tasks in priority queue!")
            return

        self.print_text("\n=== Processing Tasks by Priority ===", "BLUE")
        while self.task_manager.pq:
            prio, desc = self.task_manager.get_next_task()
            self.print_text(f"  Priority {prio} ➔ Task: {desc}", "GREEN")
            time.sleep(0.3)


if __name__ == "__main__":
    app = InteractiveApp()
    app.mainloop()
