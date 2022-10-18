# Задайте двумерный массив из целых чисел.
# Количество строк и столбцов задается с клавиатуры.
# Отсортировать элементы по возрастанию слева направо и сверху вниз.

# Например, задан массив:
# 1 4 7 2
# 5 9 10 3
#
# После сортировки
# 1 2 3 4
# 5 7 9 10

try:
    columns = int(input("Введите количество столбцов массива: "))
    lines = int(input("Введите количество строк массива: "))

    arr = []


    for s in range(lines):
        for c in range(columns):
            arr.append(int(input("Введите целое число: ")))

# проверяю, что ввелось
    i = 0
    for s in range(lines):
        for c in range(columns):
            if c == columns - 1:
                end_str = '\n'
            else:
                end_str = ''

            print(arr[i], sep=' ', end=end_str)
            i += 1

# сортировка
    arr.sort()
    print('----------------------------')

# проверяю, что получилось
    i = 0
    for s in range(lines):
        for c in range(columns):
            if c == columns - 1:
                end_str = '\n'
            else:
                end_str = ''

            print(arr[i], sep=' ', end=end_str)
            i += 1

except:
    print("Введены некоректные данные!")
