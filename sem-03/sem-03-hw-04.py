# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Нельзя использовать готовые функции.
# - 45 -> 101101

try:
    print("Перевод в двоичную систему")

    dec_n = int(input("Введите целое положительное число: "))
    if dec_n < 0:
        dec_n = -dec_n

    print(dec_n, end=" => ")

    bin_n = []
    while True:
        digit = dec_n % 2
        dec_n = dec_n // 2
        bin_n.insert(0, str(digit))
        if dec_n == 0:
            break

    print("".join(bin_n))

except:
    print("Введены некоректные данные!")
