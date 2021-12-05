# Укажите через запятую в порядке возрастания все десятичные натуральные числа, не превосходящие 17, запись которых в троичной системе счисления оканчивается на две одинаковые цифры.

def convertToBase(num, base):
	bases = '0123456789'

	result = ''
	while num > 0:
		result += bases[num % base]
		num //= base
	
	return result[::-1]

result = []
for x in range(1, 18):
	convertedX = convertToBase(x, 3)

	if (len(convertedX) > 1) and (convertedX[-1] == convertedX[-2]):
		result.append(str(x))

print(', '.join(result))