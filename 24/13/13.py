# Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт. Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
# В строках, содержащих менее 25 букв A, нужно определить и вывести максимальное расстояние между одинаковыми буквами в одной строке.
# Пример. Исходный файл:
# GIGA
# GABLAB
# NOTEBOOK
# AGAAA
# В этом примере во всех строках меньше 25 букв A. Самое большое расстояние между одинаковыми буквами – в третьей строке между буквами O, расположенными в строке на 2-й и 7-й позициях. В ответе для данного примера нужно вывести число 5.
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

with open('inf_26_04_21_24.txt') as f:
	s = list(map(lambda x: x.strip(), f.readlines()))
	res = 0
	
	for line in s:
		if line.count('A') < 25:
			distance = {}
			for i in range(len(line) - 1):
				current = line[i]
				for j in range(i + 1, len(line)):
					if current == line[j]:
						if current not in distance:
							distance[current] = j - i
						else:
							distance[current] = max(j - i, distance[current])

			res = max(sorted(distance.values(), reverse=True)[0], res)
	print(res)