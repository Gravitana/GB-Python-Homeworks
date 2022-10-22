# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
#
# *Пример:*
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint


def create_part(coef_i, k_i):
    if k_i == 0:
        x_str = ''
    elif k_i == 1:
        x_str = 'x'
    else:
        x_str = f'x^{k_i}'

    if coef_i == 0:
        return ''
    elif coef_i == 1:
        return x_str
    elif not x_str:
        return f'{coef_i}'
    else:
        return f'{coef_i}*' + x_str


try:
    k = randint(2, 10)
    coefficients = [randint(0, 100) for _ in range(k + 1)]

    # k = 5
    # coefficients = [2, 1, 0, 21, 1, 99]

    result_list = []
    for i in range(k + 1):
        part = create_part(coefficients[i], k - i)
        if part:
            result_list.append(part)

    result_str = ' + '.join(result_list) + ' = 0'

    print(result_str)

    with open('polynomial.txt', "w") as result_file:
        result_file.write(result_str)

except:
    print("Введены некоректные данные!")
