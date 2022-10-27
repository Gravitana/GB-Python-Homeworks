# Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
from random import *


def bot_move(max):
    sweets = randint(1, max)
    print("Я взял", sweets)
    return sweets


def man_move(max):
    while True:
        c = int(input("Сколько конфет возьмёшь? "))
        if 0 < c <= max:
            return c
        elif c > max:
            print(f"Сейчас можно взять не более {max} конфет")
        else:
            print("Нужно взять хотя бы одну конфету")


try:
    sweets_all = 100
    max_portion = 28
    # sweets_all = 2021

    print("Привет! Я – бот. Давай сыграем.")
    print("На столе лежит 2021 конфета. Будем брать их по очереди")
    print(f"За один ход можно забрать не более чем {max_portion} конфет.")
    print("Все конфеты оппонента достаются сделавшему последний ход.")
    print()

    is_bot_move = choice([True, False])

    if is_bot_move:
        print("Я хожу первым.")
    else:
        print("Твой ход.")

    while sweets_all > 0:
        if sweets_all > max_portion:
            sweets_max = max_portion
        else:
            sweets_max = sweets_all

        if is_bot_move:
            sweets = bot_move(sweets_max)
        else:
            sweets = man_move(sweets_max)

        sweets_all -= sweets
        print("На столе осталось", sweets_all)
        is_bot_move = not is_bot_move

    if is_bot_move:
        print("Удача на твоей стороне. Все конфеты твои!")
    else:
        print("Ура! Я выиграл!")

except:
    print("Введены некоректные данные!")
