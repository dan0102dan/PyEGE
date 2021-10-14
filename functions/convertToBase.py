def convertToBase(num, base):
	bases = list('0123456789ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')

	result = [0]
	for i in range(1, num + 1):
		for el in range(0, len(result)):
			if result[el] + 1 < base:
				result[el] += 1
				break
			else:
				result[el] = 0
				if el + 1 == len(result):
					result.append(1)
	return ''.join(map(lambda i: str(bases[i]), reversed(result)))

print(
	convertToBase(int(input('Введите число: ')), int(input('Введите основание числа: ')))
)