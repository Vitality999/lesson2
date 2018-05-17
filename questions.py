# Задание
#     Написать функцию ask_user() чтобы с помощью input() спрашивать пользователя “Как дела?”, пока он не ответит “Хорошо”


ask = input('Как дела?\n')


def ask_user(ask):
    while True:
        if ask != 'Хорошо':
            ask = input('Как дела?\n')
        elif ask == 'Хорошо':
            break
ask_user(ask)


