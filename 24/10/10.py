# Определить максимальное количество подряд идущих открывающих скобок «(» в этом файле.

with open('24.txt') as f:
	s = f.readline().strip()
 
	# 1
	br = '('
	while br in s:
		br += '('
	print(len(br) - 1)

	# 2
	res, cur = 0, 0
	for x in s:
		if x == '(':
			cur += 1
			res = max(res, cur)
		else:
			cur = 0
	print(res)