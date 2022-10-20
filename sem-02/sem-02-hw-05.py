# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z .
# Но теперь количество предикатов не три, а генерируется случайным образом от 5 до 25,
# сами значения предикатов случайные, проверяем это утверждение 100 раз,
# с помощью модуля time выводим на экран, сколько времени отработала программа.

from random import *
import time

try:
    startTime = time.time()

    pred = [True, False]

    for counter in range(100):
        count = randint(5, 25)
        predicates = [choice(pred) for _ in range(count)]

        print(predicates, end=" => ")

        part_or = False
        part_and = True

        for i in range(count):
            part_or = part_or or predicates[i]
            part_and = part_and and (not predicates[i])

        print(not part_or == part_and)

    endTime = time.time()
    totalTime = endTime - startTime

    print("Время работы программы: ", totalTime)
except:
    print("Введены некоректные данные!")
