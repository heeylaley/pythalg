# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Задача:
# 2.3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

# Python 3.9.6 (v3.9.6) [MSC v.1929 64 bit (AMD64)] on win32
from sys import getsizeof as gs
from collections import deque


def vars_mem(lst):
    bite_sum = 0

    for i in lst:
        bite_sum += gs(i)

    return bite_sum


# 1й вариант (мой изначальный) -- 4 переменных
num_1 = input('Введите число: ')

new_num = []
a = -1

while abs(a) <= len(num_1):
    new_num.append(num_1[a])
    a -= 1

res_1 = ''.join(new_num)

variables = list(locals().values())[-4:]  # исключая variables у нас использовано 4 переменных, поэтому [-4:]
print('Использование памяти в 1 варианте:')
print(vars_mem(variables))


# 2й вариант -- 2 переменных
num_2 = deque(input('Введите число: '))
num_2.reverse()

res_2 = ''.join(num_2)

variables = list(locals().values())[-2:]
print('Использование памяти во 2 варианте:')
print(vars_mem(variables))


# 3й вариант -- 2 переменных
num_3 = input('Введите число: ')
res_3 = int(str(num_3)[::-1])

variables = list(locals().values())[-2:]
print('Использование памяти во 2 варианте:')
print(vars_mem(variables))


# Результат (перевернутое число не выводила для удобства):
#
# Введите число: 1978
# Использование памяти в 1 варианте:
# 222
#
# Введите число: 1978
# Использование памяти во 2 варианте:
# 677
#
# Введите число: 1978
# Использование памяти во 2 варианте:
# 81
#
# Вывод:
# 1й вариант проигрывает и по лаконичности, и по месту, занимаемыми переменными
# 2й вариант короткий, но deque много весит
# 3й вариант самый лучший: он самый короткий и занимает меньше места