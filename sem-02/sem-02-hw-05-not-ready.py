# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z .
# Но теперь количество предикатов не три, а генерируется случайным образом от 5 до 25,
# сами значения предикатов случайные, проверяем это утверждение 100 раз,
# с помощью модуля time выводим на экран, сколько времени отработала программа.

from random import randint
import time


def fn_or(a, b):
    return a or b


def fn_and(a, b):
    return (not a) and (not b)


try:
    startTime = time.time()

    count = randint(5, 25)

    pred = {}

    pred.clear()

    for i in range(3):
        for p in [True, False]:
            pred[i] = int(p)

    print(pred)


    # if not (x or y or z) == (not x) and (not y) and (not z):
    #     print('x = ', x, ', y = ', y, ', z = ', z, sep='')

    # for x in [True, False]:
    #     for y in [True, False]:
    #         for z in [True, False]:
    #             if not (x or y or z) == (not x) and (not y) and (not z):
    #                 print('x = ', x, ', y = ', y, ', z = ', z, sep='')

    endTime = time.time()
    totalTime = endTime - startTime

    print("Время работы программы: ", totalTime)
except:
    print("Введены некоректные данные!")
