 # Приветствие игроков и правила игры:
def greetings():
    print('Добро пожаловать     ')
    print('в игру крестики-нолики')
    print('------------------------')
    print('Необходимо вводить "X" "O"')


# работает
def show():
    print('  | 0 | 1 | 2 |')
    print('---------------')
    for i, row in enumerate(field):
        row_str = f"{i} | {' | '.join(row)} |"
        print(row_str)
        print('---------------')
    print()


# Работает
def ask():
    while True:
        conds = input('Ваш ход: ').split()
        if len(conds) != 2:
            print('Введите координаты!')
            continue
        x, y = conds

        if not (x.isdigit()) or not (y.isdigit()):
            print('Введите числа!')
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print('Координаты вне диапазона!')
            continue

        if field[x][y] != ' ':
            print('Клетка занята!')
            continue
        return x, y


# проверка на выгрыш работает
def chek_win():
    for i in range(3):
        symbol = []
        for j in range(3):
            symbol.append(field[i][j])
        if symbol == ['X', 'X', 'X']:
            print('Выиграл крестик')
            return True
    for i in range(3):
        symbol = []
        for j in range(3):
            symbol.append(field[j][i])
        if symbol == ['X', 'X', 'X']:
            print('Выиграл крестик')
            return True
    symbol = []
    for i in range(3):
        symbol.append(field[i][i])
    if symbol == ['X', 'X', 'X']:
        print('Выиграл крестик')
        return True
    symbol = []
    for i in range(3):
        symbol.append(field[i][2 - i])
    if symbol == ['X', 'X', 'X']:
        print('Выиграл нолик')
        return True

    for i in range(3):
        symbol = []
        for j in range(3):
            symbol.append(field[i][j])
        if symbol == ['O', 'O', 'O']:
            print('Выиграл нолик')
            return True
    for i in range(3):
        symbol = []
        for j in range(3):
            symbol.append(field[j][i])
        if symbol == ['O', 'O', 'O']:
            print('Выиграл нолик')
            return True
    symbol = []
    for i in range(3):
        symbol.append(field[i][i])
    if symbol == ['O', 'O', 'O']:
        print('Выиграл нолик')
        return True
    symbol = []
    for i in range(3):
        symbol.append(field[i][2 - i])
    if symbol == ['O', 'O', 'O']:
        print('Выиграл нолик')
        return True

    return False


#  Игровой цикл
greetings()
field = [[' '] * 3 for i in range(3)]
count = 0
num = 0
start = input('Чтобы запустить игру, нажмите клавишу Enter')


while True:
    count += 1
    show()
    if count % 2 == 1:
        print('Ходит крестик')
    else:
        print('Ходит нолик')

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = 'O'

    if chek_win():
        print(input('Для завершения нажмите клавишу Enter'))
        break

    if count == 9:
        print('Ничья')
        print(input('Для завершения нажмите клавишу Enter'))
        break
