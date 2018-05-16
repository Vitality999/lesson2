# Цикл
#
#     Создать список из десяти целых чисел.
#     Вывести на экран каждое число, увеличенное на 1.

li = list(range(0,10))

for i in li:
    print(i + 1, end = ', ')
    i+=1


# Цикл
#
#     Ввести с клавиатуры строку.
#     Вывести эту же строку вертикально: по одному символу на строку консоли.

str = input('\nВведите строку\n')

for j in str:
    print(j)


# Оценки
#
# Создать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.

user = input('Введите класс из предлагаемых вариантов: 1a, 1b, 1c, чтобы узнать средний балл по школе\n')



school = [
{'class':'1a', 'scores':[1,1,2,3,3,4,5,5]},
{'class':'1b', 'scores':[2,2,2,3,3,4]},
{'class':'1c','scores':[5,5,5,4,3,4,5]}
]

class_sum = 0
class_len = 0

def mean_class(user):
	for clas in school:
		# print(clas)
		if clas['class'] == user:
			# print(clas['class'])
			x1 = sum(clas.get('scores'))/len(clas.get('scores'))
			print('Средний балл 1а класса =',round(x1,2), 'балла')
		elif clas['class'] == user:
			# print(clas['class'])
			x2 = sum(clas.get('scores')) / len(clas.get('scores'))
			print('Средний балл 1b класса =',round(x2,2), 'балла')
		elif clas['class'] == user:
			# print(clas['class'])
			x3 = sum(clas.get('scores')) / len(clas.get('scores'))
			print('Средний балл 1c класса =', round(x3, 2), 'балла')

mean_class(user)

def mean_school(user, class_sum, class_len):
    for pupils in school:
        x = sum(pupils.get('scores'))
        y = len(pupils.get('scores'))
        class_sum += x
        class_len += y
        z = class_sum / class_len
    print('Средний балл по всей школе: ', round(z, 2))

mean_school(user, class_sum, class_len)

