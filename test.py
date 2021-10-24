N = 0

while True:
	R = N
	if R & 1 == 0: R //= 2
	else: R -= 1

	if R % 3 == 0: R //= 3
	else: R -= 1

	if R % 5 == 0: R //= 5
	else:	R -= 1

	if (R == 1):
		print(N)
	N += 1