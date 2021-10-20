def d(n, v):
	return n % v == 0

numbers = []
for x in range(200000, 400000):
	if d(x, 7) and (not(d(x, 13))) and (not(d(x, 29))) and (not(d(x, 43))) and (not(d(x, 101))):
		numbers.append(x)
		# print(x)
print(str(len(numbers)) + str(min(numbers)*100000))