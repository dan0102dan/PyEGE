# Сколько существует шестизначных чисел, делящихся на 5, в которых каждая цифра может встречаться только один раз, при этом никакие две чётные и две нечётные цифры не стоят рядом.

figures = '0123456789'
numbers = []

def isAllOne(num: str):
	for x in figures:
		if sum([i == x for i in num]) > 1:
			return False
	return True

def checkParity(num: str):
	if (all([int(num[x]) & 1 == 0 and int(num[x+1]) & 1 == 1 for x in range(0, len(num)-1, 2)])) or (all([int(num[x]) & 1 == 1 and int(num[x+1]) & 1 == 0 for x in range(0, len(num)-1, 2)])):
		return True
	return False

def checkDivisibility(divisible: int, divider: int):
	if divisible % divider == 0:
		return True
	return False

for a in figures[1:]:
	for b in figures:
		for c in figures:
			for d in figures:
				for e in figures:
					for f in figures:
						num = a+b+c+d+e+f
						if isAllOne(num) and checkParity(num) and checkDivisibility(int(num), 5):
							numbers.append(num)
print(len(numbers))