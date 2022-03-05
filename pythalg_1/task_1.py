# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.

import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']

a = input('Введите левую границу: ')
b = input('Введите правую границу: ')

try:
    left = ord(a)  # ord -- chr определяют индекс символа/символ юникода
    right = ord(b)
    print(chr(random.randint(left, right)))
except TypeError:
    if '.' in list(a):
        print(round(random.uniform(float(a), float(b)), 3))
    else:
        print(random.randint(int(a), int(b)))
