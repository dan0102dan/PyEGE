# Для какого наименьшего целого числа А формула
#   ((x ≤ 13) → (x⋅x < A)) ∧ ((y⋅y ≤ A) → (y < 14))
# тождественно истинна (то есть принимает значение 1 при любых целых неотрицательных значениях переменных x и y)?

def checker(A):
	for x in range(1000):
		for y in range(1000):
			if not(((x <= 13) <= (x*x < A)) and ((y*y <= A) <= (y < 14))):
				return False
	return True

A = -10000000
while True:
	if checker(A):
		print(A)
	A += 1