# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def is_prime_number(checked_number):
    is_prime = True
    for cn in range(2, checked_number):
        if checked_number % cn == 0:
            is_prime = False
            break
    return is_prime

try:
    number = int(input("Введите целое число: "))
    prime_numbers = [2]
    multipliers = []
    n = number
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0 and is_prime_number(i):
                multipliers.append(i)
                n = n // i
                break
    print(multipliers)

except:
    print("Введены некоректные данные!")