# Значение выражения 2 · 216^6 + 3 · 36^9 − 432 записали в системе счисления с основанием 6. Сколько цифр 5 содержится в этой записи?

def convertTo6Base(num):
	res = ''

	while num > 0:
		res += str(num % 6)
		num //= 6
	
	return res[::-1]

print(convertTo6Base(2 * 216 ** 6 + 3 * 36 ** 9 - 432).count('5'))