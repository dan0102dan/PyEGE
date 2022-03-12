with open('27-A.txt') as f:
	n = int(f.readline())
	arr = [int(f.readline()) for i in range(n)]

	R = 0
	for i in range(len(arr) - 2):
		for j in range(i + 1, len(arr) - 1):
			for k in range(j + 1, len(arr)):
				curR = arr[i] + arr[j] + arr[k]

				if curR % 3 == 0:
					R = max(curR, R)
	print(R)

with open('27-B.txt') as f:
	n = int(f.readline())
	
	remainder0 = []
	remainder1 = []
	remainder2 = []

	for i in range(n):
		x = int(f.readline())
	
		if x % 3 == 0:
			remainder0.append(x)
		elif x % 3 == 1:
			remainder1.append(x)
		elif x % 3 == 2:
			remainder2.append(x)
			
	remainder0.sort(reverse=True)
	remainder1.sort(reverse=True)
	remainder2.sort(reverse=True)

	sum1 = sum(remainder0[0:3])
	sum2 = sum(remainder1[0:3])
	sum3 = sum(remainder1[0:3])
	sum4 = remainder0[0] + remainder1[0] + remainder2[0]

	print(max(sum1, sum2, sum3, sum4))