with open('27-A.txt') as f:
	N = int(f.readline())

	summa = 0
	minxNeChetRazn = 0
	countChet, countNeChet = 0, 0

	for i in range(N):
		n1, n2 = map(int, f.readline().split())
		curMin = min(n1, n2)

		for x in [n1, n2]:
			if x & 1 == 0:
				countChet += 1
			else:
				countNeChet += 1
		
		
		summa += curMin

		if curMin & 1 == 1:
			minxNeChetRazn = min(abs(n1 - n2), minxNeChetRazn)


	if countNeChet > countChet:
		if summa & 1 == 1:
			print(summa)
		else:
			print(summa - minxNeChetRazn)
	else:
		if summa & 1 == 0:
			print(summa)
		else:
			print(summa - minxNeChetRazn)