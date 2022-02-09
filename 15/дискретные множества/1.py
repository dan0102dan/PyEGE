# Элементами множеств А, P, Q являются натуральные числа, причём P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}, Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}. Известно, что выражение
# ( (x ∈ A) → (x ∈ P) ) ∧ ( (x ∈ Q) → ¬(x ∈ A) )
# истинно (то есть принимает значение 1) при любом значении переменной х. Определите наибольшее возможное количество элементов в множестве A.

from itertools import chain, combinations


def powerset(iterable):
	s = list(iterable)
	return chain.from_iterable(combinations(s, r) for r in range(1, len(s) + 1))

P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}

def F(x, A):
	return ((x in A) <= (x in P)) and ((x in Q) <= (x not in A))  

max_len = 0
for A in powerset(P | Q):
	if all(F(x, A) for x in range(1000)):
		max_len = max(max_len, len(A))

print(max_len)
