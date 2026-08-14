import tkinter as tk
from tkinter import messagebox
from collections import deque, defaultdict


def run_bfs():
    try:
        vertices = [v.strip() for v in vertex_entry.get().split(",") if v.strip()]
        edge_pairs = [e.strip() for e in edge_entry.get().split(",") if e.strip()]
        start = start_entry.get().strip()

        graph = defaultdict(list)
        for v in vertices:
            graph[v] = []

        for pair in edge_pairs:
            a, b = pair.split("-")
            a, b = a.strip(), b.strip()
            graph[a].append(b)
            graph[b].append(a)

        if start not in graph:
            raise ValueError("Start vertex not in graph.")

        visited = {start}
        tree = defaultdict(list)
        queue = deque([start])
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    tree[current].append(neighbor)
                    queue.append(neighbor)

        result.delete(0, tk.END)
        result.insert(tk.END, f"BFS Tree from {start}:")
        for v in tree:
            result.insert(tk.END, f"{v}: {tree[v]}")

    except Exception as e:
        messagebox.showerror("Error", f"Invalid input.\n{e}")


root = tk.Tk()
root.title("BFS Tree")

tk.Label(root, text="Vertices (A,B,C):").grid(row=0, column=0, padx=5, pady=5)
vertex_entry = tk.Entry(root, width=30)
vertex_entry.insert(0, "A,B,C,D,E,F")
vertex_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Edges (A-B,A-C):").grid(row=1, column=0, padx=5, pady=5)
edge_entry = tk.Entry(root, width=30)
edge_entry.insert(0, "A-B,A-C,B-D,B-E,C-F")
edge_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Start vertex:").grid(row=2, column=0, padx=5, pady=5)
start_entry = tk.Entry(root, width=10)
start_entry.insert(0, "A")
start_entry.grid(row=2, column=1, sticky="w", padx=5, pady=5)

tk.Button(root, text="Run BFS", command=run_bfs).grid(row=3, column=0, columnspan=2, pady=10)

result = tk.Listbox(root, width=40, height=12)
result.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
