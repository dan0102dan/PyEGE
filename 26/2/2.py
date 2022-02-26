# В текстовом файле записан набор натуральных чисел, не превышающих 109. Гарантируется, что все числа различны. Необходимо определить, сколько в наборе таких пар чётных чисел, что их среднее арифметическое тоже присутствует в файле, и чему равно наибольшее из средних арифметических таких пар.
# Входные данные.
# Задание 26
# Первая строка входного файла содержит целое число N — общее количество чисел в наборе. Каждая из следующих N строк содержит одно число.
# В ответе запишите два целых числа: сначала количество пар, затем наибольшее среднее арифметическое.
# Пример входного файла:
# 6
# 3
# 8
# 14
# 11
# 2
# 17
# В данном случае есть две подходящие пары: 8 и 14 (среднее арифметическое 11), 14 и 2 (среднее арифметическое 8).
# В ответе надо записать числа 2 и 11.

with open('26.txt') as f:
	n = int(f.readline())
	chet, nechet = [], set()

	for i in range(n):
		num = int(f.readline())
		if num & 1 == 0:
			chet.append(num)
		else:
			nechet.add(num)

	result = []
	chet1 = set(chet)

	for n1 in range(0, len(chet) - 1):
		for n2 in range(n1 + 1, len(chet)):
			sr = (chet[n1] + chet[n2]) // 2
			if sr in chet1 or sr in nechet:
				result.append(sr)
				
	print(len(result), max(result))