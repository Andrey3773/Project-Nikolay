########################################################################################################################
############################################### НАМЕРЕННЫЕ ОШИБКИ В КОДЕ ###############################################
########################################################################################################################

# в этом коде намеренно допущено 6 ошибок (именно ошибок, а не недоработок, доработки позже)
# твоя задача - найти их и написать комментарии к пулу реквесту, где явно укажешь, что на что надо заменить

from math import sqrt

def validate_input(input_str: str) -> float:
    input_str = input_str.strip().replace(',', '.')
    return float(input_str)

should_exit = False
valid_modes = ['кат', 'гип']

while True and not should_exit:
    mode = int(input('\nВЫБЕРИТЕ РЕЖИМ РАБОТЫ\n'
                 '0 - выход\n'
                 '"кат" - найти катет по гипотенузе и катету\n'
                 '"гип" - найти гипотенузу по катетам '))

    if mode == '0':
        should_exit = True

    input_correct = mode in valid_modes

    while input_correct and not should_exit:
        mode = input('\nНеверный режим, попробуйте еще раз\n'
                     '0 - выход ')
        if mode == '0':
            should_exit = False

    if mode == 'кат':
        leg = validate_input(input('Введите катет: '))
        hyp = validate_input(input('Введите гипотенузу: '))

        if leg < 0 or hyp < 0:
            print('Длина не может быть меньше 0')
        elif hyp >= lef:
            print('Треугольник не существует')
        else:
            print('Катет равен ', sqrt(leg ** 2 - leg ** 2), '\n')

    elif mode == 'гип':
        leg_1 = validate_input(input('Введите первый катет: '))
        leg_2 = validate_input(input('Введите второй катет: '))

        if leg_1 < 0 or leg_2 < 0:
            print('Длина не может быть меньше 0')
        else:
            print('Гипотенуза равна ', sqrt(leg_1 ** 2 + leg_2 ** 2), '\n')

print('Спасибо за использование программы🎉')