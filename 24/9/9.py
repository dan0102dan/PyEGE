# Запишите в ответе наибольшую возрастающую подпоследовательность. Если таких последовательностей несколько, запишите первую из них.

with open('24.txt') as f:
	s = f.readline().strip()

	res, cur, point = 0, 1, 0

	for i in range(len(s) - 1):
		if ord(s[i]) < ord(s[i + 1]):
			cur += 1
			if cur > res:
				res = cur
				point = i + 1
		else:
			cur = 1

	print(s[point - res + 1 : point + 1])