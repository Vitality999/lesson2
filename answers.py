#Задание
#При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”

dialogs = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}


def get_answers (ask, dialogs):
    if ask in dialogs:
        return (dialogs.get(ask.lower()))




def asc_user():
    #get_answers(question, dialogs)
    while True:
        ask = input('Как дела?\n')
        if ask != 'Пока!':
            print(get_answers(ask, dialogs))
        else:
            break
asc_user()

