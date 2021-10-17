def d(n, m):
	return n % m == 0

def checker(A):
	for x in range(1, 1000000):
		if not((not(d(x, A))) <= (d(x, 6) <= (not(d(x, 4))))):
			return False
	return True

A = 1
while True:
	if checker(A):
		print(A)

	A += 1