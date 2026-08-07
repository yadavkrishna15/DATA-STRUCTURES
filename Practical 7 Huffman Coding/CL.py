import heapq
import sys
import time
from collections import Counter


class Node:

    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

        print(
            "Merging nodes:",
            f"{left.char} ({left.freq})",
            "and",
            f"{right.char} ({right.freq})",
        )
        time.sleep(0.5)

    return heap[0] if heap else None


def generate_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}

    if node:
        if node.char is not None:
            codebook[node.char] = prefix
            print(f"Assigning code to character {node.char}: {prefix}")
            time.sleep(0.3)

        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)

    return codebook


def huffman_encoding(data):
    if not data:
        return "", {}

    frequencies = Counter(data)
    print("Character Frequencies: ", dict(frequencies))

    root = build_huffman_tree(frequencies)
    codebook = generate_codes(root)
    encoded_data = "".join(codebook[char] for char in data)

    print("Encoded Data: ", encoded_data)
    return encoded_data, codebook


def huffman_decoding(encoded_data, codebook):
    reverse_codebook = {v: k for k, v in codebook.items()}
    decoded_data = ""
    current_code = ""

    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codebook:
            decoded_data += reverse_codebook[current_code]
            print(f"Decoding: {current_code} -> {reverse_codebook[current_code]}")
            current_code = ""
            time.sleep(0.2)

    return decoded_data


def animate_text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()


if __name__ == "__main__":
    animate_text("Welcome to Huffman Coding CLI Application!")
    data = input("Enter the text to encode: ")

    animate_text("Starting Huffman Encoding...")
    encoded_data, codebook = huffman_encoding(data)
    animate_text("Encoding completed!")

    print("Codebook: ", codebook)

    animate_text("Starting Huffman Decoding...")
    decoded_data = huffman_decoding(encoded_data, codebook)
    animate_text("Decoding completed!")

    print("Original data:", data)
    print("Decoded data:", decoded_data)

    if data == decoded_data:
        print("Success: The original and decoded data match!")
    else:
        print("Error: The original and decoded data do not match!")
