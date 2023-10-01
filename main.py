def is_cell_occupied(field, cell):
    if field[cell]:
        return True
    return False


def player_to_name(current_player):
    if current_player == 1:
        return 'крестики'
    else:
        return 'нолики'


def converted_list_to_field(lst: list):
    for el in range(len(lst)):
        if lst[el] == 0:
            lst[el] = ' '
        elif lst[el] == 1:
            lst[el] = 'X'
        elif lst[el] == 2:
            lst[el] = 'O'
    return lst


def output(lst: list, do_reference=True):# вывод поля в консоль
    indetation = 10
    reference = range(1, 10)
    lst = converted_list_to_field(lst.copy())
    if do_reference:
        field = '   |   |                |   |   \n'\
                ' {0} | {1} | {2}            {9} | {10} | {11} \n' \
                '   |   |                |   |   \n' \
                '---+---+---          ---+---+---\n' \
                '   |   |                |   |   \n' \
                ' {3} | {4} | {5}            {12} | {13} | {14} \n' \
                '   |   |                |   |   \n' \
                '---+---+---          ---+---+---\n' \
                '   |   |                |   |   \n' \
                ' {6} | {7} | {8}            {15} | {16} | {17} \n' \
                '   |   |                |   |   '.format(*lst, *reference)
    else:
        field = '   |   |   \n' \
                ' {0} | {1} | {2} \n' \
                '   |   |   \n' \
                '---+---+---\n' \
                '   |   |   \n' \
                ' {3} | {4} | {5} \n' \
                '   |   |   \n' \
                '---+---+---\n' \
                '   |   |   \n' \
                ' {6} | {7} | {8}\n' \
                '   |   |   '.format(*lst)
    return field


def is_draw(field):
    if 0 not in field:
        return True
    return False


def is_win(field):
    # горизонтали
    if field[0] == field[1] == field[2] and field[0] != 0:
        return field[0]
    elif field[3] == field[4] == field[5] and field[3] != 0:
        return field[3]
    elif field[6] == field[7] == field[8] and field[6] != 0:
        return field[6]
    # вертикали
    elif field[0] == field[3] == field[6] and field[0] != 0:
        return field[0]
    elif field[1] == field[4] == field[7] and field[1] != 0:
        return field[1]
    elif field[2] == field[5] == field[8] and field[2] != 0:
        return field[2]
    # диагонали
    elif field[0] == field[4] == field[8] and field[0] != 0:
        return field[0]
    elif field[2] == field[4] == field[6] and field[2] != 0:
        return field[2]
    return False


# Пустое поле = 0, Крестики = 1, Нолики = 2
def game():
    field = [0, 0, 0,
             0, 0, 0,
             0, 0, 0]  # не использовал двумерные массивы, чтоб избежать циклов в циклах
    print('Игра началась')
    print('Справка: для выбора поля используйте цифры от 1 до 9:')
    print(output(field))
    print('Для хода нужно вписать цифру и нажать Enter')

    while True: # не использовал условие тут, так как хотел реализовать вывод ошибки
        print('Кто будет ходить первым?')
        current_player = input('Крестики: "1", Нолики: "2"\n')
        if current_player == '1' or current_player == '2':
            break
        else:
            print("Ошибка. Введите только 1, или только 2. Не используйте пробелы")
    print()

    current_player = int(current_player)

    while (not is_draw(field)) and (not is_win(field)):
        while True:
            print('Ходят {}:'.format(player_to_name(current_player)))
            print(output(field))
            move = input('Введите свой ход: ')
            if move.isnumeric(): # введено ли число
                move = int(move)
                if move in range(1, 10): # введена ли цифра
                    if not field[move - 1]: # занята ли клетка
                        break
                    else:
                        print('Ошибка. Поле занято. Используйте другое поле.')
                else:
                    print("Ошибка. Введите цифру от 1 до 9. Не используйте пробелы")
            else:
                print("Ошибка. Введите цифру от 1 до 9. Не используйте пробелы")

        field[move - 1] = current_player

        if current_player == 1:
            current_player = 2
        else:
            current_player = 1

    print(output(field))

    winner = is_win(field)

    if winner:
        print('Победили {}!!!'.format(player_to_name(winner)))
    else:
        print('Перед нами ничья!!!')


game()
