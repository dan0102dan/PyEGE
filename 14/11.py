# Укажите наименьшее основание системы счисления, в которой запись числа 50 трехзначна.

def convertToBase(num, base):
	bases = '0123456789ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

	result = ''
	while num > 0:
		result += bases[num % base]
		num //= base
	
	return result[::-1]

for base in range(2, 62):
	if len(convertToBase(50, base)) == 3:
		print(base)
		break