# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import Counter

num_1 = Counter(input('Введите первое число: '))
num_2 = Counter(input('Введите второе число: '))


def to_dec(a):
    hxs = {s: i for i, s in enumerate(list('0123456789ABCDEF'))}
    return sum([int(hxs[s]) * 16 ** i for i, s in enumerate(a[::-1])])


def to_hex(num: int) -> str:
    dcs = {i: s for i, s in enumerate(list('0123456789ABCDEF'))}
    st = ''
    while num % 16 > 0:
        st += dcs[num % 16]
        num //= 16
    return st[::-1]


num_sum = to_dec(num_1) + to_dec(num_2)
print(f'Сумма ваших чисел = {to_hex(num_sum)}')

num_mult = to_dec(num_1) * to_dec(num_2)
print(f'Произведение ваших чисел = {to_hex(num_mult)}')
