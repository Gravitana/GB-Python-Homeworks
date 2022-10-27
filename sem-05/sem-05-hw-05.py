# Дан список чисел. Создайте список, в который попадают числа,
# описывающие максимальную сплошную возрастающую последовательность. Порядок элементов менять нельзя.
# *Пример:*
#
# [1, 5, 2, 3, 4, 6, 1, 7] =>  [1, 7]
# [1, 5, 3, 4,  1, 7] =>  [3, 5]

start_number = 0


def find_list(cur_list):
    global start_number

    new_list = []
    max_num = max(cur_list)
    next_start = max_num

    for k in range(start_number, max_num + 1):
        if k in cur_list:
            new_list.append(k)
        else:
            next_start = k + 1
            break

    start_number = next_start

    if len(new_list) > 1:
        return new_list

    return []


try:
    print(flush=True)

    # list_of_numbers = [1, 5, 4, 1, 7]
    # list_of_numbers = [1, 5, 4, 2, 1, 7]
    # list_of_numbers = [1, 5, 3, 4, 2, 1, 7, 8]
    list_of_numbers = [1, 5, 4, 8, 1, 9, 3]

    print(list_of_numbers)

    start_number = min(list_of_numbers)
    max_number = max(list_of_numbers)
    result = []

    while start_number < max_number:
        current_list = find_list(list_of_numbers)
        if len(result) < len(current_list):
            result = current_list

    result = [result[0], result[-1]]

    print(result)

except:
    print("Введены некоректные данные!")
