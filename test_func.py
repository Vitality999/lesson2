
def nds_calc ():
    global  price, vat
    price = 100
    vat_rate = 18
    vat = price / 100 * vat_rate
    price_no_vat = price - vat
    return  price_no_vat
print (nds_calc())



def get_summ(one, two, delimeter=' '):
    return (str(one) + str(delimeter) + str(two)).upper()
print (get_summ('Hello', 'world'))