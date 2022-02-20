# Укажите через запятую в порядке возрастания все десятичные числа, не превосходящие 30, запись которых в системе счисления с основанием 5 начинается на 3?

def convertToBase(num, base):
	bases = '0123456789ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

	result = ''
	while num > 0:
		result += bases[num % base]
		num //= base
	
	return result[::-1]

results = []
for x in range(1, 30 + 1):
	if convertToBase(x, 5)[0] == '3':
		results.append(x)
print(results)