c = 'calc, 2+3 ='
x = c.split(', ')

y = (x[1].replace('=', ''))
if '+' in y:
    print(y.replace('+', ' ').split())
