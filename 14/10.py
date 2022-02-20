# Значение выражения 2 · 216^6 + 3 · 36^9 − 432 записали в системе счисления с основанием 6. Сколько цифр 5 содержится в этой записи?

def convertToBase(num, base):
	bases = '0123456789'

	result = ''
	while num > 0:
		result += bases[num % base]
		num //= base
	
	return result[::-1]

res = 2 * 216 ** 6 + 3 * 36**9 - 432
print(convertToBase(res, 6).count('5'))