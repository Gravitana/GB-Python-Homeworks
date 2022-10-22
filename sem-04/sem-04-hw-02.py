# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

try:
    numbers = [randint(1, 9) for _ in range(10)]
    temp_list = []
    result = []

    for n in numbers:
        if not (n in temp_list):
            temp_list.append(n)
            result.append(n)
        elif n in result:
            result.remove(n)

    print("Исходный список", numbers)
    print("Неповторяющиеся элементы", result)

except:
    print("Введены некоректные данные!")