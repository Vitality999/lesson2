# Задание
#     Написать функцию ask_user() чтобы с помощью input() спрашивать пользователя “Как дела?”, пока он не ответит “Хорошо”
#     При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”

ask = input('Как дела?\n')
#
#Первый пункт задания
# def ask_user(ask):
#     while True:
#         if ask != 'Хорошо':
#             ask = input('Как дела?\n')
#         elif ask == 'Хорошо':
#             break
# ask_user(ask)

#Второй пункт задания
def ask_user(ask):
    while True:
        if ask != 'Пока':
            ask = input('Как дела?\n')
        elif ask == 'Пока':
            break


def get_answer(ask):
    ask_user(ask)

get_answer(ask)