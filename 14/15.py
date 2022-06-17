# Укажите наименьшее основание системы счисления, в которой запись числа 50 трехзначна.

def convertToBase(num, base):
    bases = '0123456789ABCDEFGJKLMNOPQRSTUVWXYZ'
    res = ''

    while num > 0:
        res += bases[num % base]
        num //= base

    return res[::-1]

for base in range(2, 34):
    if len(convertToBase(50, base)) == 3:
        print(base)
        break