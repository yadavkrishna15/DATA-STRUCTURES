import tkinter as tk
from tkinter import messagebox
from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def run_dfs():
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

        visited = set()
        tree = defaultdict(list)

        def dfs(v):
            visited.add(v)
            for neighbor in graph[v]:
                if neighbor not in visited:
                    tree[v].append(neighbor)
                    dfs(neighbor)

        dfs(start)

        # Text result
        result.delete(0, tk.END)
        result.insert(tk.END, f"DFS Tree from {start}:")
        for v in tree:
            result.insert(tk.END, f"{v}: {tree[v]}")

        # Clear old plot
        for widget in plot_frame.winfo_children():
            widget.destroy()

        # Draw graph + DFS tree
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))

        G = nx.Graph(graph)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue',
                 edge_color='gray', node_size=800, font_size=12,
                 font_weight='bold', ax=ax1)
        ax1.set_title("Graph")

        T = nx.DiGraph(tree)
        pos_tree = nx.spring_layout(T)
        nx.draw(T, pos_tree, with_labels=True, node_color='lightgreen',
                 edge_color='blue', node_size=800, font_size=12,
                 font_weight='bold', arrows=True, ax=ax2)
        ax2.set_title("DFS Tree")

        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    except Exception as e:
        messagebox.showerror("Error", f"Invalid input.\n{e}")


root = tk.Tk()
root.title("DFS Tree")

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

tk.Button(root, text="Run DFS", command=run_dfs).grid(row=3, column=0, columnspan=2, pady=10)

result = tk.Listbox(root, width=40, height=8)
result.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

plot_frame = tk.Frame(root)
plot_frame.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
