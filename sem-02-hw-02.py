# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

try:
    n = int(input("Введите целое число: "))

    lst = []
    a = 1
    for i in range(1, n + 1):
        a *= i
        lst.append(a)

    print(lst)

except:
    print("Введены некоректные данные!")
