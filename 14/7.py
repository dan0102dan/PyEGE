# Запишите натуральное число, десятичная запись которого состоит из двух цифр, шестнадцатеричная запись заканчивается цифрой B, а пятеричная — цифрой 3.

def convertToBase(num, base):
	bases = '0123456789ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

	result = ''
	while num > 0:
		result += bases[num % base]
		num //= base
	
	return result[::-1]

for x in range(10, 100):
	if convertToBase(x, 16)[-1] == 'B' and convertToBase(x, 5)[-1] == '3':
		print(x)