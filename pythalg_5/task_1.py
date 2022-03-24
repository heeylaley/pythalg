# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
# предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple
from statistics import mean


def med_income_quant(a):
    val_list = []

    for comp in a:
        val_list.append(comp.profit)

    med_profit = mean(val_list)
    print(f'Средняя прибыль = {med_profit}')

    for comp in a:
        if comp.profit > med_profit:
            print(f'У компании "{comp.name}" прибыль выше средней')
        elif comp.profit == med_profit:
            print(f'У компании "{comp.name}" средняя прибыль')
        else:
            print(f'У компании "{comp.name}" прибыль ниже средней')


Company = namedtuple('Company', 'name, profit')
companies = []

n = int(input('Введите количество предприятий: '))

for el in range(1, n + 1):
    company = Company(input('Название компании: '), int(input('Прибыль компании: ')))
    companies.append(company)

print('-' * 50)
med_income_quant(companies)
