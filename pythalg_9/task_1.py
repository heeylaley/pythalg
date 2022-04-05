# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.

from hashlib import sha1
from itertools import combinations


def substring(a):
    if a == '':
        return 0

    hash_set = set([a[x:y] for x, y in combinations(range(len(a) + 1), r=2)])
    hash_list = list(hash_set)
    hash_list.pop(hash_list.index(a))

    res = [sha1(element.encode('utf-8')).hexdigest() for element in hash_list]

    return len(res)


hash_str = input('Введите строку: ')
print(f'Количество подстрок в вашей строке = {substring(hash_str)}')
