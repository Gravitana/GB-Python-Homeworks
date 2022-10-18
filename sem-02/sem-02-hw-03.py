# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
# Нельзя юзать find или count.

def search_count(haystack, needle):
    limit = len(haystack) - len(needle) + 1

    if limit <= 0:
        return 0

    count = 0

    for first in range(limit):
        last = first + len(needle)
        str_i = haystack[first:last]

        if needle == str_i:
            count += 1

    return count


try:
    h = input("Введите строку, в которой будем искать: ")
    n = input("Введите строку, которую нужно найти: ")

    print(search_count(h, n))

except:
    print("Введены некоректные данные!")
