# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [210 235; 210 300], числа, имеющие ровно четыре различных натуральных делителя, не считая единицы и самого числа. Для каждого найденного числа запишите эти четыре делителя в четыре соседних столбца на экране с новой строки. Делители в строке должны следовать в порядке возрастания.
# Например, в диапазоне [10; 16] ровно четыре различных натуральных делителя имеет число 12, поэтому для этого диапазона вывод на экране должна содержать следующие значения:
# 2 3 4 6

def getDivs(num):
	divs = []
	for x in range(1, num + 1):
		if (num % x == 0):
			if ((x != 1) and (x != num)):
				divs.append(x)
	return divs

result = []
for x in range(210235, 210300 + 1):
	divs = getDivs(x)
	if (len(divs) == 4):
		result.append(divs)

for arr in result:
	print(sorted(arr))