# Значение выражения 343^5 + 7^3 − 1 − X записали в системе счисления с основанием 7, при этом в записи оказалось 12 цифр 6. При каком минимальном целом положительном X это возможно?

def convertToBase(num, base):
	bases = '0123456789'

	result = ''
	while num > 0:
		result += bases[num % base]
		num //= base
	
	return result[::-1]

x = 0
while True:
	res = 343 ** 5 + 7 ** 3 - 1 - x
	if convertToBase(res, 7).count('6') == 12:
		print(x)
		break
	x += 1