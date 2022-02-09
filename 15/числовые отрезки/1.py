# На числовой прямой даны два отрезка: P = [5, 30] и Q = [14, 23]. Укажите наибольшую возможную длину промежутка A, для которого формула
# ((x ∈ P) ≡ (x ∈ Q)) → ¬(x ∈ A)
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х.

P = range(5, 30 + 1)
Q = range(14, 23 + 1)

max_len = 0
for start in range(1, 100):
	for end in range(start + 1, 100 + 1):
		A = range(start, end)
		if (all(((x in P) == (x in Q)) <= (not(x in A)) for x in range(10000))):
			max_len = max(max_len, end - start)

print(max_len)