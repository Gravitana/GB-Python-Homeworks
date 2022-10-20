# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import randint, uniform


def get_fractional_part(number, accuracy):
    return round(number % 1, accuracy)


try:
    ACCURACY = 2  # точность вычислений

    count = randint(5, 9)
    numbers = [round(uniform(0, 99), ACCURACY) for _ in range(count)]
    count_num = len(numbers)

    max_value = min_value = get_fractional_part(numbers[0], ACCURACY)

    print("Разница между максимальным и минимальным значением дробной части элементов")
    print(numbers, end=" => ")

    for n in numbers:
        fractional_part = get_fractional_part(n, ACCURACY)
        if fractional_part > max_value: max_value = fractional_part
        if fractional_part < min_value: min_value = fractional_part

    print(max_value, "-", min_value, "=", max_value - min_value)

except:
    print("Введены некоректные данные!")
