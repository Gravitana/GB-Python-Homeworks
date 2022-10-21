# Даны два многочлена. Задача - сформировать их сумму.
#
# например, 5*x^3 + 2*x^2 + 6 и 7*x^2+6*x+3 , Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9
# ??????, _x^3 + 2*x^2 + 6

def remove_space(s):
    return s.strip()


try:
    str1 = "5*x^3 + 2*x^2 + 6".lower()
    str2 = "7*x^2+6*x+3".lower()

    list1 = str1.split('+')
    list2 = str2.split('+')

    list1 = list(map(remove_space, list1))
    list2 = list(map(remove_space, list2))

    dict1 = {}
    dict2 = {}

    # ['5*x^3', '2*x^2', '6'] ['7*x^2', '6*x', '3']

    for i in range(len(list1)):
        value = str(list1[i]).split("^")
        degree = value[1]
        value = str(list1[i]).split("*")
        # number = list1[0]
        # dict1[degree] = number

        print(degree, value)




    print(list1, list2)


# str1='5*x^3 + 2*x^2 + 6'
# str2='7*x^2+6*x+3'
#
# # str2=input("Введите первый многочлен  вида A*x^2+B*x+C=0 ")
# dict= {}
# def x (strin):
#     dict_f={}
#     for i in range(len(strin)-1):
#         if strin[i]=='x':
#             if strin[i+1]=='^':
#                 tmp=int(strin[i+2])
#                 if strin[i-1]=='*':
#                     koef=int(strin[i-2])
#                     dict_f[tmp] = koef
#                 else:
#                     koef=1
#                     dict_f[tmp] = koef
#
#     return dict_f
#
# dict =x (str1)
# print(dict)







except:
    print("Введены некоректные данные!")