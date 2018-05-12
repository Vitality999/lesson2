#списки

# mylist = ['Антон', 'Женя', 'Виталик', 'Сергей', 'Настя', 'Марина']
# print (mylist);
#
# print (len (mylist)); #длина списка
#
# print ((mylist[2:4])); # срез [x:y]
#
#
# x = list (range(2,8))
# x.append ('Python')
# print(x.index (6))
# print (x)
# print (x[2:4])
# print (len(x))
#
# x.remove('Python')
# print (x)

y = {'name' :'Виталик', 'age': 25, 'have_airplane': False}
y['city']= 'Moscow'
print (y['name'])

del y['have_airplane'] # удаление ключа из словаря


print (y.get('country'))

weather = {'city': 'Москва', 'temperature': 20, 'wind':'Восточный'}
print (weather['city'])
print ('temperature' in weather)
weather['temperature'] = 25
print (weather['temperature'])
print (len(weather))
print ('country' in weather)
weather ['date'] = '27.05.2017'
print(weather)

list2 = []
list2.extend ([{'temperature':10}, {'temperature1':20}, {'temperature3':30}])
print (list2)