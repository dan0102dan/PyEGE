# Текстовый файл состоит не более чем из 1 200 000 символов X, Y, и Z. Определите максимальное количество идущих подряд символов, среди которых нет подстроки XZZY. Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

with open('24.txt') as f:
	line = f.readline().strip()
	line = line.split('XZZY')

	maxLength = 0
	for i in range(len(line)):
		curLength = len(line[i])
		
		if (i == 0) or (i == len(line) - 1):
			maxLength = max(curLength + 3, maxLength) # прибавляем 3, так как можно добавить ZZY (если 0) и XZZ (если конец)
		else:
			maxLength = max(curLength + 6, maxLength) # прибавляем 6, так как можно добавить и ZZY, и XZZ

	print(maxLength)