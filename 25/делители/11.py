# пояснение: https://inf-ege.sdamgia.ru/problem?id=33527

# Найдите все натуральные числа, принадлежащие отрезку
# [101 000 000; 102 000 000], у которых ровно три различных чётных делителя. В ответе перечислите найденные числа в порядке возрастания.

for x in range(101000000, 102000000 + 1, 2):
	dels = set([x])

	for d1 in range(2, int(x ** 0.5 + 1)):
		d2 = x // d1
		if x % d1 == 0:
			if d1 % 2 == 0:
				dels.add(d1)
			if d2 % 2 == 0:
				dels.add(d2)
		if len(dels) > 3:
			break
	if len(dels) == 3:
		print(x)