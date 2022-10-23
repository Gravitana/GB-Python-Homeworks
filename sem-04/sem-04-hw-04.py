# Найдите корни квадратного уравнения, уравнение вводит через строку пользователь.
# Например, 6*x^2+5*x+6=0 .
# Само собой, уравнение может и не иметь решения. Предусмотреть все варианты, сделать обработку исключений.
import re


try:
    equation = input("Введите квадратное уравнение: ")
    # equation = "32*x^2+6=0"
    # equation = "x^2-8*x+12=0"
    # equation = "x^2+9*x=0"
    # equation = "x^2-16=0"
    # equation = "-8 * x^2+5*  x+ 6 =  0"

    equation_str = equation.replace(' ', '').replace('*', '').replace('^', '').replace('=0', '')
    pattern = '[+-]'
    equation_parts = re.split(pattern, equation_str)
    equation_parts = list(map(lambda part: str(part).split('x'), equation_parts))
    if equation_parts[0] == ['']:
        equation_parts.pop(0)

    equation_signs = re.findall(pattern, equation_str)
    if len(equation_signs) < len(equation_parts):
        equation_signs.insert(0, '+')

    a = b = c = 0

    # print(equation_str)
    # print('equation_signs', equation_signs)
    # print('equation_parts', equation_parts)

    for i in range(len(equation_parts)):
        part_i = equation_parts[i]
        if part_i[0] == '':
            num = 1
        else:
            num = int(part_i[0])

        if equation_signs[i] == '-':
            num = -num

        if len(part_i) == 1:
            c = num
        elif part_i[1] == '':
            b = num
        else:
            a = num

    # print(f'a={a}, b={b}, c={c}')

    d = b ** 2 - 4 * a * c

    if d < 0:
        print("Корней нет")
    elif d == 0:
        x = -(b / (2 * a))
        print("Единственный корень:", x)
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print("Корни уравнения:%5.2f %5.2f" % (x1, x2))

except:
    print("Введены некоректные данные!")
