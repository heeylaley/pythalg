# 2. Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter, namedtuple
import heapq  # для работы с кучами


class Node(namedtuple("Node", ["left", "right"])):
    def get_code(self, n_code, n_bin_code):
        self.left.get_code(n_code, n_bin_code + "0")
        self.right.get_code(n_code, n_bin_code + "1")


class Leaf(namedtuple("Leaf", ["symbol"])):
    def get_code(self, l_code, l_bin_code):
        l_code[self.symbol] = l_bin_code or "0"


def huffman(a):
    sybl_list = Counter(a).items()
    sybl_heap = [(freq, len(a.replace(sym, '')), Leaf(sym)) for sym, freq in sybl_list]
    heapq.heapify(sybl_heap)

    while len(sybl_heap) > 1:
        freq1, cnt1, left = heapq.heappop(sybl_heap)
        freq2, cnt2, right = heapq.heappop(sybl_heap)
        heapq.heappush(sybl_heap, (freq1 + freq2, cnt1 + cnt2, Node(left, right)))

    return sybl_heap


res = {}
code_in = input('Введите строку: ')
symbl_heap = huffman(code_in)

if symbl_heap:
    [(_freq, _count, root)] = symbl_heap
    root.get_code(res, "")

print("Таблица кодирования по алгоритму Хаффмана:")
for symbl, bin_code in res.items():
    print(f'{symbl} - {bin_code}')

print(f'Закодировання строка: {" ".join([res[el] for el in code_in])}')
