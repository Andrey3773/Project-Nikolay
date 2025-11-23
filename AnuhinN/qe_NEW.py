flag = True
def check_correct(word):
    n_word = word.strip().replace(",", ".")
    for j in n_word:
        if j not in '0123456789.-':
            print('строка содержит недопустимые символы')
            return 0, False
    return float(n_word), True

while flag:
    n  = input('введите Enter для неограниченного числа квадратных уравнений или число квадратных уравнений')
    if n == '':
        cntr2 = 0
        while True:
            cntr2 += 1
            print(f'уравнение номер {cntr2}')
            while True:
                input_a = input('коэффициент a: ')
                a, flag3 = check_correct(input_a)
                if flag3:
                    break
                else:
                    print('Введите число корректно')
            while True:
                input_b = input('коэффициент b: ')
                b, flag3 = check_correct(input_b)
                if flag3:
                    break
                else:
                    print('Введите число корректно')
            while True:
                input_c = input('коэффициент c: ')
                c, flag3 = check_correct(input_c)
                if flag3:
                    break
                else:
                    print('Введите число корректно')
            d = (b ** 2) - (4 * a * c)
            if a == 0:
                print(f'уравнение имеет единственный корень: {-c / b}')
            elif b == 0:
                print(f'уравнение имеет два корня: x1 = {(-c / a) ** 0.5} и x2 = {-((-c / a) ** 0.5)}')
            elif c == 0:
                print(f'Уравнение имеет два корня: x1 = 0 и x2 = {-b / a}')
            elif d == 0:
                print('уравнение имеет единственный корень:', (-b + d ** 0.5) / (2 * a))
            elif d >= 0:
                print('Уравнение имеет два корня:', 'x1 =', (-b + d ** 0.5) / (2 * a), 'x2 =',
                      (-b - d ** 0.5) / (2 * a))
            elif d < 0:
                print('Уравнение не имеет корней')
            else:
                print('Ошибка')

            ask = input('Если хотите продолжить нажмите Enter, или любую другую клавишу для остановки')
            if ask != '':
                flag = False
                break

    elif n.isdigit():
        cntr = int(n)
        for i in range(cntr):
            print(f'Уравнение номер {i+1} из {cntr}')
            while True:
                input_a = input('коэффициент a: ')
                a, flag3 = check_correct(input_a)
                if flag3:
                    break
                else:
                    print('Введите число корректно')
            while True:
                input_b = input('коэффициент b: ')
                b, flag3 = check_correct(input_b)
                if flag3:
                    break
                else:
                    print('Введите число корректно')
            while True:
                input_c = input('коэффициент c: ')
                c, flag3 = check_correct(input_c)
                if flag3:
                    break
                else:
                    print('Введите число корректно')

            d = (b ** 2) - (4 * a * c)
            if a == 0:
                print(f'уравнение имеет единственный корень: {-c / b}')
            elif b == 0:
                print(f'уравнение имеет два корня: x1 = {(-c / a) ** 0.5} и x2 = {-((-c / a) ** 0.5)}')
            elif c == 0:
                print(f'Уравнение имеет два корня: x1 = 0 и x2 = {-b / a}')
            elif d == 0:
                print('уравнение имеет единственный корень:', (-b + d ** 0.5) / (2 * a))
            elif d >= 0:
                print('Уравнение имеет два корня:', 'x1 =', (-b + d ** 0.5) / (2 * a), 'x2 =',
                      (-b - d ** 0.5) / (2 * a))
            elif d < 0:
                print('Уравнение не имеет корней')
            else:
                print('Ошибка')

        flag = False
    else:
        print('повторите попытку')