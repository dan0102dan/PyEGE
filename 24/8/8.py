# Определите длину наибольшей убывающей подпоследовательности.

with open('24.txt') as f:
	s = f.readline().strip()

	res, cur = 0, 1
	for i in range(len(s) - 1):
		if s[i] > s[i + 1]:
			cur += 1
			res = max(cur, res)
		else:
			cur = 1

	print(res)