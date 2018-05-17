import ephem
import datetime

solar = [{'planet':'Меркурий'},{'planet':'Венера'}, {'planet':'Земля'}, {'planet':'Марс'},{'planet': 'Юпитер'},
         {'planet':'Сатурн'}, {'planet':'Нептун'}, {'planet':'Плутон'}, {'planet':'Луна' }]


sysdate = datetime.datetime.now()

def question():
    while True:
        planets = input('Введите название планеты с большой буквы, для выхода введите:"Выход"\n')
        if planets != 'Выход':
            print(solar_system(solar, planets))
        else:
            break


def solar_system(solar, planets):
    for objects in solar:
        if objects['planet'] == planets:
            if planets == 'Марс':
                mars = ephem.Mars(sysdate)
                return (ephem.constellation(mars))
            elif planets == 'Юпитер':
                jupiter = ephem.Jupiter(sysdate)
                return (ephem.constellation(jupiter))
            elif planets == 'Луна':
                moon = ephem.Moon(sysdate)
                return (ephem.constellation(moon))
            elif planets == 'Сатурн':
                saturn = ephem.Saturn(sysdate)
                return (ephem.constellation(saturn))

question()






