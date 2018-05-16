# Сравнение строк
#
#     Написать функцию, которая принимает на вход две строки.
#     Если строки одинаковые, возвращает 1.
#     Если строки разные и первая длиннее, возвращает 2.
#     Если строки разные и вторая строка 'learn', возвращает 3.

str1 = input('Введите первую строку\n')
str2 = input('Введите вторую строку\n')


def comparison_len (str1, str2):
    if len(str1) == len(str2):
        print(1)
    elif len(str1) > len(str2):
        print(2)
    elif len(str1) != len(str2) and str2 in 'learn':
        print(3)
    else:
        print('Попробуйте заново')

comparison_len(str1,str2)