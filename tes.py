import heapq
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq

    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.freq = left.freq + right.freq

    def __lt__(self, other):
        return self.freq < other.freq

# Build Huffman tree
def build_huffman_tree(text):
    frequency = Counter(text)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        heapq.heappush(heap, HuffmanNode(left, right))

    return heap[0]

# Generate Huffman codes
def generate_codes(node, prefix="", code_map=None):
    if code_map is None:
        code_map = {}
        
    if isinstance(node, Node):
        code_map[node.char] = prefix
    else:
        generate_codes(node.left, prefix + "0", code_map)
        generate_codes(node.right, prefix + "1", code_map)
    
    return code_map

# Encode the text
def encode(text, code_map):
    return "".join(code_map[char] for char in text)

# Calculate bit size
def calculate_sizes(text, code_map):
    original_size = len(text) * 8
    compressed_size = sum(len(code_map[char]) for char in text)
    compression_ratio = (original_size - compressed_size) / original_size * 100
    return original_size, compressed_size, compression_ratio

# Main function
if __name__ == "__main__":
    while True:
        text = input("Masukkan teks yang ingin dikompresi (atau ketik 'exit' untuk keluar): ")
        if text.lower() == 'exit':
            print("Program selesai.")
            break
        if not text:
            print("Teks tidak boleh kosong. Silakan masukkan teks yang valid.")
            continue
        try:
            tree = build_huffman_tree(text)
            code_map = generate_codes(tree)
            encoded_text = encode(text, code_map)
            original_size, compressed_size, compression_ratio = calculate_sizes(text, code_map)

            print("\nHasil Kompresi")
            print(f"Kode Huffman: {encoded_text}")
            print(f"Ukuran asli: {original_size} bit")
            print(f"Ukuran setelah kompresi: {compressed_size} bit")
            print(f"Rasio kompresi: {compression_ratio:.2f}%")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
