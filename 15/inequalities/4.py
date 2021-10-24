# Сколько существует целых значений А, при которых формула
#   ((x ≤ 5) → (x⋅x < A)) ∧ ((y⋅y ≤ A) → (y ≤ 8))
# тождественно истинна (то есть принимает значение 1 при любых целых неотрицательных значениях переменных x и y)?

def checker(A):
	for x in range(1000):
		for y in range(1000):
			if not(((x <= 5) <= (x*x < A)) and ((y*y <= A) <= (y <= 8))):
				return False
	return True

result = []
A = 1
while True:
	if checker(A):
		result.append(A)
		print(len(result))

	A += 1