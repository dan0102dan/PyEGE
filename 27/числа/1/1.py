with open('27-A_2.txt') as f:
	n = int(f.readline())
	arr = [int(f.readline()) for i in range(n)]

	R = 0

	for i in range(len(arr) - 1):
		for j in range(i + 1, len(arr)):
			curR = arr[i] * arr[j]
			if (curR % 14 == 0):
				R = max(curR, R)

	print(R)

with open('27-B_2.txt') as f:
	n = int(f.readline())
	
	maxValue, maxDivTwo, maxDivSeven, maxDivFourteen = 0, 0, 0, 0

	for i in range(n):
		x = int(f.readline())

		if x % 2 == 0:
			maxDivTwo = max(x, maxDivTwo)
		elif x % 7 == 0:
			maxDivSeven = max(x, maxDivSeven)
		if x % 14 == 0:
			maxDivFourteen = max(x, maxDivFourteen)
		else:
			maxValue = max(x, maxValue)
	
	print(max(maxValue * maxDivFourteen, maxDivTwo * maxDivSeven))