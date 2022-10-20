# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint

try:
    count = randint(5, 10)
    numbers = [randint(1, 9) for _ in range(count)]
    count_num = len(numbers)
    summa = 0

    print(numbers)

    for i in range(count_num):
        if i % 2 != 0:
            summa += numbers[i]

    print("Сумма элементов на нечётных позициях:", summa)

except:
    print("Введены некоректные данные!")