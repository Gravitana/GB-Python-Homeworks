# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры),
# причем чтоб количество элементов было четное. Вывести на экран красивенько таблицей.
# Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно переместился на другое место
# и выполнить это за m*n / 2 итераций.
# То есть если массив три на четыре, то надо выполнить не более 6 итераций.
# И далее в конце опять вывести на экран как таблицу.

from random import *


def get_random_position(positions):
    position = choice(positions)
    return position


def print_numbers(arr, cols, rows):
    for row in range(rows):
        start_pos = row * cols
        end_pos = row * cols + cols
        print(arr[start_pos:end_pos])


try:
    count_col = int(input("Введите количество столбцов массива: "))

    if count_col % 2 != 0:
        count_row = int(input("Введите чётное количество строк массива: "))
    else:
        count_row = int(input("Введите количество строк массива: "))

    count = count_col * count_row
    free_positions = list(range(count))

    numbers = [randint(1, 99) for _ in range(count)]
    print_numbers(numbers, count_col, count_row)

    iterations = 0
    while len(free_positions) > 0:
        current_pos = get_random_position(free_positions)  # выбираем позицию, с которой будем забирать
        current_number = numbers[current_pos]  # забираем значение из массива
        free_positions.remove(current_pos)  # удаляем позицию из списка свободных
        new_pos = get_random_position(free_positions)  # выбираем новое место
        free_positions.remove(new_pos)  # удаляем позицию из списка свободных
        numbers[current_pos] = numbers[new_pos]
        numbers[new_pos] = current_number
        iterations += 1

    print("Массив перемешан. Кол-во итераций:", iterations)
    print_numbers(numbers, count_col, count_row)

except:
    print("Введены некоректные данные!")
