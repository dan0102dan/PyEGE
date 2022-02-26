# Системный администратор раз в неделю создаёт архив пользовательских файлов. Однако объём диска, куда он помещает архив, может быть меньше, чем суммарный объём архивируемых файлов. Известно, какой объём занимает файл каждого пользователя.
# По заданной информации об объёме файлов пользователей и свободном объёме на архивном диске определите максимальное число пользователей, чьи файлы можно сохранить в архиве, а также максимальный размер имеющегося файла, который может быть сохранён в архиве, при условии, что сохранены файлы максимально возможного числа пользователей.
# Входные данные.
# Задание 26
# В первой строке входного файла находятся два числа: S — размер свободного места на диске (натуральное число, не превышающее 10 000) и N — количество пользователей (натуральное число, не превышающее 5000). В следующих N строках находятся значения объёмов файлов каждого пользователя (все числа натуральные, не превышающие 100), каждое в отдельной строке.
# Запишите в ответе два числа: сначала наибольшее число пользователей, чьи файлы могут быть помещены в архив, затем максимальный размер имеющегося файла, который может быть сохранён в архиве, при условии, что сохранены файлы максимально возможного числа пользователей.
# Пример входного файла:
# 100 4
# 80
# 30
# 50
# 40
# При таких исходных данных можно сохранить файлы максимум двух пользователей. Возможные объёмы этих двух файлов 30 и 40, 30 и 50 или 40 и 50. Наибольший объём файла из перечисленных пар — 50, поэтому ответ для приведённого примера:
# 2 50

with open('27881.txt') as f:
	S, N = map(int, f.readline().split())
	arr = [int(f.readline()) for i in range(N)]

	result = []

	for x in sorted(arr):
		if sum(result) + x <= S:
			result.append(x)
		elif sum(result) - result[-1] + x <= S:
			result.remove(result[-1])
			result.append(x)
		else:
			break

	print(len(result), result[-1])