# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import math
from random import randint

try:
    count = randint(4, 7)
    numbers = [randint(1, 9) for _ in range(count)]
    count = len(numbers)
    limit = math.ceil(len(numbers) / 2)
    product_numbers = []

    print(numbers, end=" => ")

    for i in range(limit):
        a = numbers[i]
        b = numbers[-i-1]
        product_numbers.append(a * b)

    print(product_numbers)

except:
    print("Введены некоректные данные!")