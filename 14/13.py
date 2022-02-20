# Укажите наименьшее основание системы счисления, в которой запись десятичного числа 30 имеет ровно три значащих разряда.

def convertToBase(num, base):
	bases = '0123456789ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

	result = ''
	while num > 0:
		result += bases[num % base]
		num //= base
	
	return result[::-1]

for base in range(2, 62):
	res = convertToBase(30, base)
	if len(res) == 3:
		print(base)
		break