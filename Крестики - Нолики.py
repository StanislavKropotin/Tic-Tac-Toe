def start():
    pl_name = input("Как Вас зовут? Для пропуска нажмите Enter: ")
    if len(pl_name) > 0:
        print(" ---------------------------------------------------------     ")
        print("     Добро пожаловать в Крестики - Нолики", pl_name, "!")
        print(" ---------------------------------------------------------     ")
        print("Формат ввода: X - строка  ------->")
        print("              Y - столбец |")
        print("                          |")
        print("                          |")
        print("                          V")
    else:
        print("     -----------------------------------------     ")
        print("   Добро пожаловать в Крестики - Нолики - Игрок ! ")
        print("     -----------------------------------------     ")
        print("Формат ввода: X - строка  ------->")
        print("              Y - столбец |")
        print("                          |")
        print("                          |")
        print("                          V")
start()
field = [["  "] * 3 for i in range(3)]
def show():
    print(f"  | 0 | 1 | 2 |")
    print("----------------")
    print(f"|0| {field[0][0]}| {field[0][1]}| {field[0][2]}|")
    print("----------------")
    print(f"|1| {field[1][0]}| {field[1][1]}| {field[1][2]}|")
    print("----------------")
    print(f"|2| {field[2][0]}| {field[2][1]}| {field[2][2]}|")
    print("----------------")
show()
def game():
    num = 0
    while True:
        x_x = int(input("Ходит крестик:Введите значение X - от 0 до 2: "))
        y_x = int(input("Ходит крестик:Введите значение Y - от 0 до 2: "))
        while x_x > 2 or y_x > 2:
            print("Клетки с таким значением нет!")
            show()
            x_x = int(input("Ходит крестик:Введите значение X - от 0 до 2: "))
            y_x = int(input("Ходит крестик:Введите значение Y - от 0 до 2: "))
            show()
        while x_x == 0 and y_x == 0 and field[0][0] != "  ":
            print("Клетка занята!")
            show()
            x_x = int(input("Ходит крестик:Введите значение X - от 0 до 2: "))
            y_x = int(input("Ходит крестик:Введите значение Y - от 0 до 2: "))
            show()
            while x_x > 2 or y_x > 2:
                print("Клетки с таким значением нет!")
                show()
                x_x = int(input("Ходит крестик:Введите значение X - от 0 до 2: "))
                y_x = int(input("Ходит крестик:Введите значение Y - от 0 до 2: "))
                show()
        while x_x == 0 and y_x == 1 and field[1][0] != "  ":
            print("Клетка занята!")
            show()
            x_x = int(input("Ходит крестик:Введите значение X - от 0 до 2: "))
            y_x = int(input("Ходит крестик:Введите значение Y - от 0 до 2: "))
            show()
            while x_x > 2 or y_x > 2:
                print("Клетки с таким значением нет!")
                show()
                x_x = int(input("Ходит крестик:Введите значение X - от 0 до 2: "))
                y_x = int(input("Ходит крестик:Введите значение Y - от 0 до 2: "))
                show()
        while x_x == 0 and y_x == 2 and field[2][0] != "  ":
            print("Клетка занята!")
            show()
            x_x = int(input("Ходит крестик:Введите значение X - от 0 до 2: "))
            y_x = int(input("Ходит крестик:Введите значение Y - от 0 до 2: "))
            show()
            while x_x > 2 or y_x > 2:
                print("Клетки с таким значением нет!")
                show()
                x_x = int(input("Ходит крестик:Введите значение X - от 0 до 2: "))
                y_x = int(input("Ходит крестик:Введите значение Y - от 0 до 2: "))
                show()
        while x_x == 1 and y_x == 0 and field[0][1] != "  ":
            print("Клетка занята!")
            show()
            x_x = int(input("Ходит крестик:Введите значение X - от 0 до 2: "))
            y_x = int(input("Ходит крестик:Введите значение Y - от 0 до 2: "))
            show()
            while x_x > 2 or y_x > 2:
                print("Клетки с таким значением нет!")
                show()
                x_x = int(input("Ходит крестик:Введите значение X - от 0 до 2: "))
                y_x = int(input("Ходит крестик:Введите значение Y - от 0 до 2: "))
                show()
        while x_x == 1 and y_x == 1 and field[1][1] != "  ":
            print("Клетка занята!")
            show()
            x_x = int(input("Ходит крестик:Введите значение X - от 0 до 2: "))
            y_x = int(input("Ходит крестик:Введите значение Y - от 0 до 2: "))
            show()
            while x_x > 2 or y_x > 2:
                print("Клетки с таким значением нет!")
                show()
                x_x = int(input("Ходит крестик:Введите значение X - от 0 до 2: "))
                y_x = int(input("Ходит крестик:Введите значение Y - от 0 до 2: "))
                show()
        while x_x == 1 and y_x == 2 and field[2][1] != "  ":
            print("Клетка занята!")
            show()
            x_x = int(input("Ходит крестик:Введите значение X - от 0 до 2: "))
            y_x = int(input("Ходит крестик:Введите значение Y - от 0 до 2: "))
            show()
            while x_x > 2 or y_x > 2:
                print("Клетки с таким значением нет!")
                show()
                x_x = int(input("Ходит крестик:Введите значение X - от 0 до 2: "))
                y_x = int(input("Ходит крестик:Введите значение Y - от 0 до 2: "))
                show()
        while x_x == 2 and y_x == 0 and field[0][2] != "  ":
            print("Клетка занята!")
            show()
            x_x = int(input("Ходит крестик:Введите значение X - от 0 до 2: "))
            y_x = int(input("Ходит крестик:Введите значение Y - от 0 до 2: "))
            show()
            while x_x > 2 or y_x > 2:
                print("Клетки с таким значением нет!")
                show()
                x_x = int(input("Ходит крестик:Введите значение X - от 0 до 2: "))
                y_x = int(input("Ходит крестик:Введите значение Y - от 0 до 2: "))
                show()
        while x_x == 2 and y_x == 1 and field[1][2] != "  ":
            print("Клетка занята!")
            show()
            x_x = int(input("Ходит крестик:Введите значение X - от 0 до 2: "))
            y_x = int(input("Ходит крестик:Введите значение Y - от 0 до 2: "))
            show()
            while x_x > 2 or y_x > 2:
                print("Клетки с таким значением нет!")
                show()
                x_x = int(input("Ходит крестик:Введите значение X - от 0 до 2: "))
                y_x = int(input("Ходит крестик:Введите значение Y - от 0 до 2: "))
                show()
        while x_x == 2 and y_x == 2 and field[2][2] != "  ":
            print("Клетка занята!")
            show()
            x_x = int(input("Ходит крестик:Введите значение X - от 0 до 2: "))
            y_x = int(input("Ходит крестик:Введите значение Y - от 0 до 2: "))
            show()
            while x_x > 2 or y_x > 2:
                print("Клетки с таким значением нет!")
                show()
                x_x = int(input("Ходит крестик:Введите значение X - от 0 до 2: "))
                y_x = int(input("Ходит крестик:Введите значение Y - от 0 до 2: "))
                show()
        while x_x == 0 and y_x == 0 and field[0][0] != "  ":
            print("Клетка занята!")
            show()
            x_x = int(input("Ходит крестик:Введите значение X - от 0 до 2: "))
            y_x = int(input("Ходит крестик:Введите значение Y - от 0 до 2: "))
            show()
        if x_x == 0 and y_x == 0 and field[0][0] == "  ":
            field[0][0] = "X "
        while x_x == 0 and y_x == 1 and field[1][0] != "  ":
            print("Клетка занята!")
            show()
            x_x = int(input("Ходит крестик:Введите значение X - от 0 до 2: "))
            y_x = int(input("Ходит крестик:Введите значение Y - от 0 до 2: "))
            show()
        if x_x == 0 and y_x == 1 and field[1][0] == "  ":
            field[1][0] = "X "
        while x_x == 0 and y_x == 2 and field[2][0] != "  ":
            print("Клетка занята!")
            show()
            x_x = int(input("Ходит крестик:Введите значение X - от 0 до 2: "))
            y_x = int(input("Ходит крестик:Введите значение Y - от 0 до 2: "))
            show()
        if x_x == 0 and y_x == 2 and field[2][0] == "  ":
            field[2][0] = "X "
        while x_x == 1 and y_x == 0 and field[0][1] != "  ":
            print("Клетка занята!")
            show()
            x_x = int(input("Ходит крестик:Введите значение X - от 0 до 2: "))
            y_x = int(input("Ходит крестик:Введите значение Y - от 0 до 2: "))
            show()
        if x_x == 1 and y_x == 0 and field[0][1] == "  ":
            field[0][1] = "X "
        if x_x == 1 and y_x == 1 and field[1][1] == "  ":
            field[1][1] = "X "
        if x_x == 1 and y_x == 2 and field[2][1] == "  ":
            field[2][1] = "X "
        if x_x == 2 and y_x == 0 and field[0][2] == "  ":
            field[0][2] = "X "
        if x_x == 2 and y_x == 1 and field[1][2] == "  ":
            field[1][2] = "X "
        if x_x == 2 and y_x == 2 and field[2][2] == "  ":
            field[2][2] = "X "
        if field[0][0] == "X " and field[0][1] == "X " and field[0][2] == "X ":
            print("Победил Крестик!Игра Окончена!")
            show()
            break
        if field[0][0] == "X " and field[1][0] == "X " and field[2][0] == "X ":
            print("Победил Крестик!Игра Окончена!")
            show()
            break
        if field[0][1] == "X " and field[1][1] == "X " and field[2][1] == "X ":
            print("Победил Крестик!Игра Окончена!")
            show()
            break
        if field[0][2] == "X " and field[1][2] == "X " and field[2][2] == "X ":
            print("Победил Крестик!Игра Окончена!")
            show()
            break
        if field[1][0] == "X " and field[1][1] == "X " and field[1][2] == "X ":
            print("Победил Крестик!Игра Окончена!")
            show()
            break
        if field[2][0] == "X " and field[2][1] == "X " and field[2][2] == "X ":
            print("Победил Крестик!Игра Окончена!")
            show()
            break
        if field[0][0] == "X " and field[1][1] == "X " and field[2][2] == "X ":
            print("Победил Крестик!Игра Окончена!")
            show()
            break
        if field[0][2] == "X " and field[1][1] == "X " and field[2][0] == "X ":
            print("Победил Крестик!Игра Окончена!")
            show()
            break
        num += 0.9
        if num >= 4.5:
            print("Ничья!")
            show()
            break
        show()
        x_0 = int(input("Ходит нолик:Введите значение X - от 0 до 2: "))
        y_0 = int(input("Ходит нолик:Введите значение Y - от 0 до 2: "))
        while x_0 > 2 or y_0 > 2:
            print("Клетки с таким значением нет!")
            show()
            x_0 = int(input("Ходит нолик:Введите значение X - от 0 до 2: "))
            y_0 = int(input("Ходит нолик:Введите значение Y - от 0 до 2: "))
            show()
        while x_0 == 0 and y_0 == 0 and field[0][0] != "  ":
            print("Клетка занята!")
            show()
            x_0 = int(input("Ходит нолик:Введите значение X - от 0 до 2: "))
            y_0 = int(input("Ходит нолик:Введите значение Y - от 0 до 2: "))
            show()
            while x_0 > 2 or y_0 > 2:
                print("Клетки с таким значением нет!")
                show()
                x_0 = int(input("Ходит нолик:Введите значение X - от 0 до 2: "))
                y_0 = int(input("Ходит нолик:Введите значение Y - от 0 до 2: "))
                show()
        while x_0 == 0 and y_0 == 1 and field[1][0] != "  ":
            print("Клетка занята!")
            show()
            x_0 = int(input("Ходит нолик:Введите значение X - от 0 до 2: "))
            y_0 = int(input("Ходит нолик:Введите значение Y - от 0 до 2: "))
            show()
            while x_0 > 2 or y_0 > 2:
                print("Клетки с таким значением нет!")
                show()
                x_0 = int(input("Ходит нолик:Введите значение X - от 0 до 2: "))
                y_0 = int(input("Ходит нолик:Введите значение Y - от 0 до 2: "))
                show()
        while x_0 == 0 and y_0 == 2 and field[2][0] != "  ":
            print("Клетка занята!")
            show()
            x_0 = int(input("Ходит нолик:Введите значение X - от 0 до 2: "))
            y_0 = int(input("Ходит нолик:Введите значение Y - от 0 до 2: "))
            show()
            while x_0 > 2 or y_0 > 2:
                print("Клетки с таким значением нет!")
                show()
                x_0 = int(input("Ходит нолик:Введите значение X - от 0 до 2: "))
                y_0 = int(input("Ходит нолик:Введите значение Y - от 0 до 2: "))
                show()
        while x_0 == 1 and y_0 == 0 and field[0][1] != "  ":
            print("Клетка занята!")
            show()
            x_0 = int(input("Ходит нолик:Введите значение X - от 0 до 2: "))
            y_0 = int(input("Ходит нолик:Введите значение Y - от 0 до 2: "))
            show()
            while x_0 > 2 or y_0 > 2:
                print("Клетки с таким значением нет!")
                show()
                x_0 = int(input("Ходит нолик:Введите значение X - от 0 до 2: "))
                y_0 = int(input("Ходит нолик:Введите значение Y - от 0 до 2: "))
                show()
        while x_0 == 1 and y_0 == 1 and field[1][1] != "  ":
            print("Клетка занята!")
            show()
            x_0 = int(input("Ходит нолик:Введите значение X - от 0 до 2: "))
            y_0 = int(input("Ходит нолик:Введите значение Y - от 0 до 2: "))
            show()
            while x_0 > 2 or y_0 > 2:
                print("Клетки с таким значением нет!")
                show()
                x_0 = int(input("Ходит нолик:Введите значение X - от 0 до 2: "))
                y_0 = int(input("Ходит нолик:Введите значение Y - от 0 до 2: "))
                show()
        while x_0 == 1 and y_0 == 2 and field[2][1] != "  ":
            print("Клетка занята!")
            show()
            x_0 = int(input("Ходит нолик:Введите значение X - от 0 до 2: "))
            y_0 = int(input("Ходит нолик:Введите значение Y - от 0 до 2: "))
            show()
            while x_0 > 2 or y_0 > 2:
                print("Клетки с таким значением нет!")
                show()
                x_0 = int(input("Ходит нолик:Введите значение X - от 0 до 2: "))
                y_0 = int(input("Ходит нолик:Введите значение Y - от 0 до 2: "))
                show()
        while x_0 == 2 and y_0 == 0 and field[0][2] != "  ":
            print("Клетка занята!")
            show()
            x_0 = int(input("Ходит нолик:Введите значение X - от 0 до 2: "))
            y_0 = int(input("Ходит нолик:Введите значение Y - от 0 до 2: "))
            show()
            while x_0 > 2 or y_0 > 2:
                print("Клетки с таким значением нет!")
                show()
                x_0 = int(input("Ходит нолик:Введите значение X - от 0 до 2: "))
                y_0 = int(input("Ходит нолик:Введите значение Y - от 0 до 2: "))
                show()
        while x_0 == 2 and y_0 == 1 and field[1][2] != "  ":
            print("Клетка занята!")
            show()
            x_0 = int(input("Ходит нолик:Введите значение X - от 0 до 2: "))
            y_0 = int(input("Ходит нолик:Введите значение Y - от 0 до 2: "))
            show()
            while x_0 > 2 or y_0 > 2:
                print("Клетки с таким значением нет!")
                show()
                x_0 = int(input("Ходит нолик:Введите значение X - от 0 до 2: "))
                y_0 = int(input("Ходит нолик:Введите значение Y - от 0 до 2: "))
                show()
        while x_0 == 2 and y_0 == 2 and field[2][2] != "  ":
            print("Клетка занята!")
            show()
            x_0 = int(input("Ходит нолик:Введите значение X - от 0 до 2: "))
            y_0 = int(input("Ходит нолик:Введите значение Y - от 0 до 2: "))
            show()
            while x_0 > 2 or y_0 > 2:
                print("Клетки с таким значением нет!")
                show()
                x_0 = int(input("Ходит нолик:Введите значение X - от 0 до 2: "))
                y_0 = int(input("Ходит нолик:Введите значение Y - от 0 до 2: "))
                show()
        if x_0 == 0 and y_0 == 0 and field[0][0] == "  ":
            field[0][0] = "0 "
        if x_0 == 0 and y_0 == 1 and field[1][0] == "  ":
            field[1][0] = "0 "
        if x_0 == 0 and y_0 == 2 and field[2][0] == "  ":
            field[2][0] = "0 "
        if x_0 == 1 and y_0 == 0 and field[0][1] == "  ":
            field[0][1] = "0 "
        if x_0 == 1 and y_0 == 1 and field[1][1] == "  ":
            field[1][1] = "0 "
        if x_0 == 1 and y_0 == 2 and field[2][1] == "  ":
            field[2][1] = "0 "
        if x_0 == 2 and y_0 == 0 and field[0][2] == "  ":
            field[0][2] = "0 "
        if x_0 == 2 and y_0 == 1 and field[1][2] == "  ":
            field[1][2] = "0 "
        if x_0 == 2 and y_0 == 2 and field[2][2] == "  ":
            field[2][2] = "0 "
        if field[0][0] == "0 " and field[0][1] == "0 " and field[0][2] == "0 ":
            print("Победил Нолик!Игра Окончена!")
            show()
            break
        if field[0][0] == "0 " and field[1][0] == "0 " and field[2][0] == "0 ":
            print("Победил Нолик!Игра Окончена!")
            show()
            break
        if field[0][1] == "0 " and field[1][1] == "0 " and field[2][1] == "0 ":
            print("Победил Нолик!Игра Окончена!")
            show()
            break
        if field[0][2] == "0 " and field[1][2] == "0 " and field[2][2] == "0 ":
            print("Победил Нолик!Игра Окончена!")
            show()
            break
        if field[1][0] == "0 " and field[1][1] == "0 " and field[1][2] == "0 ":
            print("Победил Нолик!Игра Окончена!")
            show()
            break
        if field[2][0] == "0 " and field[2][1] == "0 " and field[2][2] == "0 ":
            print("Победил Нолик!Игра Окончена!")
            show()
            break
        if field[0][0] == "0 " and field[1][1] == "0 " and field[2][2] == "0 ":
            print("Победил Нолик!Игра Окончена!")
            show()
            break
        if field[0][2] == "0 " and field[1][1] == "0 " and field[2][0] == "0 ":
            print("Победил Нолик!Игра Окончена!")
            show()
            break
        if num >= 4.5:
            print("Ничья!")
            show()
            break
        show()
game()


































