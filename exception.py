ask = input('Как дела?\n')

def ask_user(ask):
    while True:
        if ask != 'Хорошо':
            ask = input('Как дела?\n')
        elif ask == 'Хорошо':
            break


try:
    ask_user(ask)
except KeyboardInterrupt:
    print('Пока')

