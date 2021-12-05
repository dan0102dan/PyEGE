# Укажите через запятую в порядке возрастания все десятичные числа, не превосходящие 30, запись которых в системе счисления с основанием 5 начинается на 3?

def convertToBase(num, base):
	bases = '0123456789'

	result = ''
	while num > 0:
		result += bases[num % base]
		num //= base
	
	return result[::-1]

result = []
for x in range(1, 31):
	if convertToBase(x, 5)[0] == '3':
		result.append(x)
print(len(result))
