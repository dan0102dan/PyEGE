# Для какого наибольшего целого числа А формула
 
# ((x ≤ 9) →(x ⋅ x ≤ A)) ⋀ ((y ⋅ y ≤ A) → (y ≤ 9))
 
# тождественно истинна, то есть принимает значение 1 при любых целых неотрицательных x и y?

def checker(A):
	for x in range(1000):
		for y in range(1000):
			if not( ((x <= 9) <= (x * x <= A)) and ((y * y <= A) <= (y <= 9))):
				return False
	return True

A = 1
while True:
	if checker(A):
		print(A)

	A += 1