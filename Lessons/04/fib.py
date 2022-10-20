# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

try:
    n = int(input("Введите число: "))

    # fib2 = [0, 1]
    # fib1 = [0, 1]

    fib = [0, 1]

    for i in range(1, n):
        summa2 = fib[i - 1] - fib[i]
        summa1 = fib[i] + fib[i - 1]
        fib.insert(summa2)
        # fib.append(summa1)

    # for i in range(1, n):
    #     summa = fib2[i-1] - fib2[i]
    #     fib2.append(summa)
    #
    # fib2 = list(reversed(fib2))
    #
    # for i in range(1, n):
    #     summa = fib1[i] + fib1[i-1]
    #     fib1.append(summa)
    #
    # fib1.remove(0)








    # print(fib2 + fib1)
    print(fib)

except:
    print("Введены некоректные данные!")
