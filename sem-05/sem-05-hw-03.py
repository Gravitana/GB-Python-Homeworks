# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Функции FIND и COUNT юзать нельзя.

try:
    str_input = "ывбвоа рафш абв гурабвашгцуки цуроилгв рабшгра шуабвцкйуц"

    result = ' '.join(list(filter(lambda x: not ('абв' in x), str_input.split())))

    print(str_input)
    print(result)

except:
    print("Введены некоректные данные!")