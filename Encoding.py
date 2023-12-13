import heapq
from collections import defaultdict
import os

def build_huffman_tree(symbols_freq):
    heap = [[weight, [symbol, ""]] for symbol, weight in symbols_freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return heap[0]

def generate_huffman_codes(tree):
    huff_codes = {}
    for pair in tree[1:]:
        symbol, code = pair
        if symbol == '\n':
            symbol = '\\n'
        huff_codes[symbol] = code
    return huff_codes

def save_codes(file_name, huff_codes):
    os.mkdir(file_name[:-4] + '_encode')
    os.chdir(file_name[:-4] + '_encode')
    name = file_name[:-4] + '_codes' + '.txt'
    my_file = open(name, "w+")
    for word, code in huff_codes.items():
        my_file.write(word + ' ' + code + '\n')


def compress_data(text, huff_codes, file_name):
    compressed_data = ""
    for char in text:
        if char == '\n':
            compressed_data += huff_codes['\\n']
        else:
            compressed_data += huff_codes[char]
    name = file_name[:-4] + '_encode' + '.txt'
    my_file = open(name, "w+")
    my_file.write(compressed_data)
    os.chdir("..")
    return compressed_data

def start(file_name):
    if '.txt' in file_name:
        with open(file_name, 'r', encoding="utf-8") as file:
            text = file.read()
    else:
        text = file_name
    
    # Подсчет частоты символов в тексте
    symbols_freq = defaultdict(int)
    for symbol in text:
        symbols_freq[symbol] += 1
    
    # Построение дерева Хаффмана и генерация кодов
    huffman_tree = build_huffman_tree(symbols_freq)
    huffman_codes = generate_huffman_codes(huffman_tree)
    save_codes(file_name, huffman_codes)

    compressed_data = compress_data(text, huffman_codes, file_name)
    return compressed_data