# В системе счисления с основанием N запись числа 93₁₀ оканчивается на 2 и содержит не менее трёх цифр. Чему равно число N?

def convertToBase(num, base):
	bases = '0123456789ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

	result = ''
	while num > 0:
		result += bases[num % base]
		num //= base
	
	return result[::-1]

for N in range(3, 62):
	res = convertToBase(93, N)
	if res[-1] == '2' and len(res) <= 3:
		print(N)
		break