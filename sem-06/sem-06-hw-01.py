# Создайте программу для игры в "Крестики-нолики"
DOT_EMPTY = '•'
DOT_HUMAN = 'X'
DOT_BOT = 'O'
game_map_size = 3  # 5
game_map = []
last_turn_of_human = []


def init_game_map():
    global game_map
    game_map = [[DOT_EMPTY] * game_map_size for _ in range(game_map_size)]


def print_game_map():
    global game_map
    print(' ', end=' ')
    for i in range(0, game_map_size):
        print(i, end=' ')
    print()
    for i in range(0, game_map_size):
        print(i, end=' ')
        for j in range(0, game_map_size):
            print(game_map[i][j], end=' ')
        print()


def check_turn(turn):
    result = (-1 < turn[0] < game_map_size) and (-1 < turn[1] < game_map_size)
    if not result:
        print("Ошибка! Неверно задана строка или столбец.")
        return False
    result = game_map[turn[0]][turn[1]] == DOT_EMPTY
    if not result:
        print("Ошибка! Ячейка уже занята.")
        return False
    return True


def turn_of_human():
    row_number = int(input("Введите номер строки: "))
    col_number = int(input("Введите номер столбца: "))
    return [row_number, col_number]


try:
    max_turns = game_map_size * game_map_size
    turns_count = 1

    init_game_map()
    print('Игра "Крестики-Нолики"')
    print('Ваш ход')
    print_game_map()

    while True:
        # global last_turn_of_human
        print("Ход", turns_count, "из", max_turns)
        turn_is_valid = False
        while not turn_is_valid:
            turn = turn_of_human()
            turn_is_valid = check_turn(turn)

        last_turn_of_human = turn
        game_map[turn[0]][turn[1]] = DOT_HUMAN
        print_game_map()

        if turns_count >= max_turns:
            break
        else:
            turns_count += 1

        # Далее пока ходит человек вместо бота

        print("Ход", turns_count, "из", max_turns)
        turn_is_valid = False
        while not turn_is_valid:
            turn = turn_of_human()
            turn_is_valid = check_turn(turn)

        last_turn_of_human = turn
        game_map[turn[0]][turn[1]] = DOT_BOT
        print_game_map()

        if turns_count >= max_turns:
            break
        else:
            turns_count += 1

    print("Игра окончена")

except:
    print("Введены некоректные данные!")
