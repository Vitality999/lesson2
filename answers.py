question =  (input('Введите приветствие '))
dialogs = [{"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"},
        {'1': 'один', '2': 'два', '3': 'три'} ]

def get_answewrs (question, dialogs):
    #print(dialogs)
    for dialog in dialogs:
        if question in dialogs:
            print(dialog.get(question.lower()))
        else:
            print('Такого ключа нет')

print(get_answewrs(question, dialogs))
