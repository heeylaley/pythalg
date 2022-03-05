# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)

a = int(input('Введите 1 число: '))
b = int(input('Введите 2 число: '))
c = int(input('Введите 3 число: '))

if a > c:
    if a > b:
        if b > c:
            print(b)
        else:
            print(c)
    else:
        print(a)
elif a > b:
    print(a)
elif b > c:
    print(c)
else:
    print(b)

# короткий вариант (но тут прогон нескольких условий сразу)
if b < a < c or c < a < b:
    print(a)
elif a < b < c or c < b < a:
    print(b)
else:
    print(c)
