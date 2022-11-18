# Создайте программу для игры в "Крестики-нолики"
DOT_EMPTY = '•'
DOT_HUMAN = 'X'
DOT_AI = 'O'
game_map_size = 3  # 5
game_map = []


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


try:
    init_game_map()
    print('Игра "Крестики-Нолики"')
    print_game_map()







except:
    print("Введены некоректные данные!")
