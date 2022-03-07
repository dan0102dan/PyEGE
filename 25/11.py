# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [120115; 120200], число, имеющее максимальное количество различных натуральных делителей, если таких чисел несколько — найдите максимальное из них. Выведите на экран количество делителей такого числа и само число.
# Например, в диапазоне [80; 90] максимальное количество различных натуральных делителей имеет число 90, поэтому для этого диапазона вывод на экране должна содержать следующие значения:
# 12 90

def findDivs(num):
	result = []
	for x in range(1, int(num ** 0.5 + 1)):
		if num % x == 0:
			result.append(x)
			result.append(num // x)
	return sorted(result)

maxX = 0
maxDivsCount = []

for x in range(120115, 120200 + 1):
	divs = findDivs(x)
	if len(divs) >= len(maxDivsCount):
		maxDivsCount = divs
		maxX = x
print(len(maxDivsCount), maxX)