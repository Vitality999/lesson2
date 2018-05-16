# Возраст
#
#     Попросить пользователя ввести возраст.
#     По возрасту определить, чем он должен заниматься: учиться в детском саду, школе, ВУЗе или работать.
#     Вывести занятие на экран.

age = int (input ('Сколько вам полных лет? '))
kid = list (range (1, 7))
child = list (range (6, 19))
young = list (range (18, 23))

def check_age (age):
    if age in kid:
        print('Вам пора в детский сад')

    elif age in child:
        print('Вам пора в школу')

    elif age in young:
        print('Вам пора в ВУЗ')

    elif age <= 0:
        print('Введен неверный возраст')

    elif age >= 65:
        print('Пора на пенсию')

    else:
        print('Вам пора на работу')

check_age(age)