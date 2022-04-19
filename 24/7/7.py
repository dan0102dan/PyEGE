# Найдите длину самой длинной подцепочки, состоящей из символов C.

with open('24.txt') as f:
	line = f.readline()

	c = 'C'
	while c in line:
		c += 'C'
	print(len(c) - 1)