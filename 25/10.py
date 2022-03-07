# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [201455; 201470], числа, имеющие ровно 4 различных натуральных делителя. Выведите эти четыре делителя для каждого найденного числа в порядке возрастания.
 
def findDivs(num):
	result = []
	for x in range(1, int(num ** 0.5 + 1)):
		if num % x == 0:
			result.append(x)
			result.append(num // x)
	return sorted(result)

for x in range(201455, 201470 + 1):
	divs = findDivs(x)
	if len(divs) == 4:
		print(divs)