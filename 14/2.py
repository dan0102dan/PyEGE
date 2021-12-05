# Укажите, сколько всего раз встречается цифра 2 в записи чисел 10, 11, 12, …, 17 в системе счисления с основанием 5.

def convertToBase(num, base):
	bases = '0123456789ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

	result = ''
	while num > 0:
		result += bases[num % base]
		num //= base
	
	return result[::-1]

result = 0
for x in range(10, 18):
	result += convertToBase(x, 5).count('2')
print(result)