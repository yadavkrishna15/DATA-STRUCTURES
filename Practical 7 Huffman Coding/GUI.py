import heapq
import time
import tkinter as tk
from collections import Counter
from tkinter import messagebox, ttk


class Node:
    """Represents a node in the Huffman Tree."""

    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Huffman Coding Visualizer")
        self.geometry("720x680")
        self.configure(bg="#1e1e1e")

        self.setup_ui()

    def setup_ui(self):
        # Header Label
        header = tk.Label(
            self,
            text="Huffman Coding Visualizer",
            font=("Consolas", 16, "bold"),
            fg="#007acc",
            bg="#1e1e1e",
        )
        header.pack(pady=10)

        # Input Frame
        input_frame = tk.Frame(self, bg="#1e1e1e")
        input_frame.pack(fill="x", padx=20, pady=5)

        lbl_input = tk.Label(
            input_frame,
            text="Enter text to encode:",
            font=("Consolas", 11),
            fg="#dcdcdc",
            bg="#1e1e1e",
        )
        lbl_input.pack(anchor="w")

        self.entry_text = tk.Entry(
            input_frame,
            font=("Consolas", 12),
            bg="#252526",
            fg="#dcdcdc",
            insertbackground="white",
        )
        self.entry_text.pack(fill="x", pady=5)

        # Action Button
        self.btn_run = tk.Button(
            input_frame,
            text="Start Huffman Encoding & Decoding",
            font=("Consolas", 11, "bold"),
            bg="#0e639c",
            fg="white",
            activebackground="#1177bb",
            activeforeground="white",
            command=self.process_huffman,
        )
        self.btn_run.pack(fill="x", pady=5)

        # Output Terminal Screen
        console_frame = tk.Frame(self, bg="#1e1e1e")
        console_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.console = tk.Text(
            console_frame,
            font=("Consolas", 11),
            bg="#1e1e1e",
            fg="#dcdcdc",
            wrap="word",
        )
        scrollbar = ttk.Scrollbar(
            console_frame, orient="vertical", command=self.console.yview
        )
        self.console.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.console.pack(side="left", fill="both", expand=True)

        # Tag Styles for Terminal Color Simulation
        self.console.tag_config("BLUE", foreground="#569cd6")
        self.console.tag_config("YELLOW", foreground="#dcdcaa")
        self.console.tag_config("GREEN", foreground="#6a9955")
        self.console.tag_config("CYAN", foreground="#4ec9b0")
        self.console.tag_config("RED", foreground="#f44747")
        self.console.tag_config("MAGENTA", foreground="#c586c0")
        self.console.tag_config("WHITE", foreground="#ffffff")

        # Welcome Screen
        self.animate_text("Welcome to Huffman Coding GUI Application!\n", "BLUE")

    def animate_text(self, text, tag="WHITE", speed=0.03):
        """Simulates character typing effect in GUI."""
        for char in text:
            self.console.insert("end", char, tag)
            self.console.see("end")
            self.update()
            time.sleep(speed)

    def print_text(self, text, tag="WHITE"):
        """Prints a line of text instantly."""
        self.console.insert("end", text + "\n", tag)
        self.console.see("end")
        self.update()

    def build_huffman_tree(self, frequencies):
        heap = [Node(char, freq) for char, freq in frequencies.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)

            merged = Node(freq=left.freq + right.freq)
            merged.left = left
            merged.right = right

            heapq.heappush(heap, merged)

            self.print_text(
                f"Merging nodes: {left.char} ({left.freq}) and {right.char} ({right.freq})",
                "YELLOW",
            )
            time.sleep(0.4)

        return heap[0] if heap else None

    def generate_codes(self, node, prefix="", codebook=None):
        if codebook is None:
            codebook = {}

        if node:
            if node.char is not None:
                codebook[node.char] = prefix
                self.print_text(
                    f"Assigning code to character {node.char}: {prefix}",
                    "GREEN",
                )
                time.sleep(0.2)

            self.generate_codes(node.left, prefix + "0", codebook)
            self.generate_codes(node.right, prefix + "1", codebook)

        return codebook

    def huffman_encoding(self, data):
        if not data:
            return "", {}

        frequencies = Counter(data)
        self.print_text(f"Character Frequencies: {dict(frequencies)}", "CYAN")

        root = self.build_huffman_tree(frequencies)
        codebook = self.generate_codes(root)
        encoded_data = "".join(codebook[char] for char in data)

        self.print_text(f"Encoded Data: {encoded_data}", "CYAN")
        return encoded_data, codebook

    def huffman_decoding(self, encoded_data, codebook):
        reverse_codebook = {v: k for k, v in codebook.items()}
        decoded_data = ""
        current_code = ""

        for bit in encoded_data:
            current_code += bit
            if current_code in reverse_codebook:
                decoded_data += reverse_codebook[current_code]
                self.print_text(
                    f"Decoding: {current_code} -> {reverse_codebook[current_code]}",
                    "MAGENTA",
                )
                current_code = ""
                time.sleep(0.15)

        return decoded_data

    def process_huffman(self):
        data = self.entry_text.get()

        if not data:
            messagebox.showwarning("Warning", "Please enter some text first!")
            return

        self.console.delete("1.0", "end")
        self.btn_run.config(state="disabled")

        # Step 1: Encoding Process
        self.animate_text("Starting Huffman Encoding...\n", "GREEN")
        encoded_data, codebook = self.huffman_encoding(data)
        self.animate_text("Encoding completed!\n", "GREEN")

        self.print_text(f"Codebook: {codebook}\n", "CYAN")

        # Step 2: Decoding Process
        self.animate_text("Starting Huffman Decoding...\n", "RED")
        decoded_data = self.huffman_decoding(encoded_data, codebook)
        self.animate_text("Decoding completed!\n", "RED")

        # Step 3: Verification
        self.print_text(f"Original data: {data}", "BLUE")
        self.print_text(f"Decoded data:  {decoded_data}", "WHITE")

        if data == decoded_data:
            self.print_text(
                "Success: The original and decoded data match!", "GREEN"
            )
        else:
            self.print_text(
                "Error: The original and decoded data do not match!", "RED"
            )

        self.btn_run.config(state="normal")


if __name__ == "__main__":
    app = HuffmanApp()
    app.mainloop()
