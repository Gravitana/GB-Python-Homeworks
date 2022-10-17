# Напишите программу, которая принимает на вход N, и координаты двух точек
# и находит расстояние между ними в N-мерном пространстве.

try:
    n = int(input("Введите количество измерений: "))

    a = []
    b = []

    for i in range(n):
        a.append(float(input("Введите {0}-ю координату точки A: ".format(i+1))))

    for i in range(n):
        b.append(float(input("Введите {0}-ю координату точки B: ".format(i+1))))

    summa = 0

    for i in range(n):
        summa += (b[i] - a[i])**2

    result = summa**0.5

    print("Расстояние между точками:%5.2f" % result)

except:
    print("Введены некоректные данные!")
