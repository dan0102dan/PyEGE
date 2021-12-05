# Укажите наименьшее целое значение А, при котором выражение
#   (y + 4x < A) ∨ (x + 4y > 120) ∨ (5x - 2y > 50)
# истинно для любых целых положительных значений x и y.

def checker(A):
	for x in range(10000):
		for y in range(10000):
			if not(((y + 4*x) < A) or ((x + 4*y) > 120) or ((5*x - 2*y) > 50)):
				return False
	return True

A = -1000000

while True:
	if checker(A):
		print(A)
	A += 1