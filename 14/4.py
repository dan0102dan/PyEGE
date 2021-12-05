# В системе счисления с некоторым основанием десятичное число 18 записывается в виде 30. Укажите это основание.

def convertToBase(num, base):
	bases = '0123456789'

	result = ''
	while num > 0:
		result += bases[num % base]
		num //= base
	
	return result[::-1]

for base in range(2, 10):
	if convertToBase(18, base) == '30':
		print(base)