# Для какого наименьшего целого неотрицательного числа A выражение
# (2m + 3n > 43) ∨ (m < A) ∨ (n ≤ A)
# тождественно истинно при любых целых неотрицательных m и n?

def checker(A):
	for m in range(1000):
		for n in range(1000):
			if not(((2 * m + 3 * n) > 43) or (m < A) or (n <= A)):
				return False
	return True

A = 0
while True:
	if checker(A):
		print(A)
		break
	A += 1