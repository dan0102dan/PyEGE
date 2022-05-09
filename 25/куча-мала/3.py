# Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
# - символ «?» означает ровно одну произвольную цифру;
# - символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
# Среди натуральных чисел, больших 2352000, найдите числа, все простые делители которых, выписанные без пробелов по возрастанию, образуют число, соответствующее маске «10*29». Например, число 234566 имеет 3 простых делителя: 2, 17, 6899, они образуют число 2176899, которое соответствует маске «21*9». В ответе укажите первые 5 найденных чисел в порядке возрастания, справа от каждого числа запишите его наибольший простой делитель.

def mask(num):
	s = str(num)
	if s[:2] == '10' and s[-2:] == '29':
		return True
	return False

def isPrime(num):
	return all(num % x != 0 for x in range(2, int(num ** 0.5 + 1)))

def primeDels(num):
	res = set()
	for d1 in range(2, int(num ** 0.5 + 1)):
		d2 = num // d1
		if num % d1 == 0:
			if isPrime(d1):
				res.add(d1)
			if isPrime(d2):
				res.add(d2)
	return sorted(res)

res = 0
x = 2352001
while res < 5:
	divs = primeDels(x)
	if mask(''.join(map(str, divs))):
		res += 1
		print(x, max(divs))
	x += 1