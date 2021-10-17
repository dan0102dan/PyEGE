# Сколько существует целых значений числа A, при которых формула
 
# ((x < 5) → (x2 < A)) /\ ((y2 ≤ A) → (y ≤ 5))
 
# тождественно истинна при любых целых неотрицательных x и y?

def checker(A):
	for x in range(1000):
		for y in range(1000):
			if not(((x < 5) <= (x**2 < A)) and ((y**2 <= A) <= (y <= 5))):
				return False
	return True

result = []
A = 1
while True:
	if checker(A):
		result.append(A)
		print(len(result))
	A += 1