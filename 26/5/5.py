# Предприятие производит оптовую закупку некоторых изделий A и B, на которую выделена определённая сумма денег. У поставщика есть в наличии партии этих изделий различных модификаций по различной цене. На выделенные деньги необходимо приобрести как можно больше изделий B независимо от модификации. Если у поставщика закончатся изделия B, то на оставшиеся деньги необходимо приобрести как можно больше изделий A. Известны выделенная для закупки сумма, а также количество и цена различных модификаций данных изделий у поставщика. Необходимо определить, сколько будет закуплено изделий A и какая сумма останется неиспользованной.
# Входные данные.
# Задание 26
# Первая строка входного файла содержит два целых числа: N — общее количество партий изделий у поставщика и M — сумма выделенных на закупку денег (в рублях). Каждая из следующих N строк описывает одну партию и содержит два целых числа (цена одного изделия в рублях и количество изделий в партии) и один символ (латинская буква A или B), определяющий тип изделия. Все данные в строках входного файла отделены одним пробелом.
# В ответе запишите два целых числа: сначала количество закупленных изделий типа A, затем оставшуюся неиспользованной сумму денег.
# Пример входного файла:
# 4 1000
# 30 8 A
# 50 12 B
# 40 14 A
# 20 10 B
# В данном случае сначала нужно купить изделия B: 10 изделий по 20 рублей и 12 изделий по 50 рублей. На это будет потрачено 800 рублей. На оставшиеся 200 рублей можно купить 6 изделий A по 30 рублей. Таким образом, всего будет куплено 6 изделий A и останется 20 рублей. В ответе надо записать числа 6 и 20.

with open('26.txt') as f:
	N, M = map(int, f.readline().split())
	izdA, izdB = [], []

	for i in range(N):
		st = f.readline().split()
		if (st[2] == 'A'):
			izdA.append(list(map(int, st[:2])))
		else:
			izdB.append(list(map(int, st[:2])))

	izdA.sort(key=lambda arr: arr[0])
	izdB.sort(key=lambda arr: arr[0])

	for b in izdB:
		cost = b[0]
		for x in range(1, b[1] + 1):
			if M - cost >= 0:
				M -= cost
			else:
				break
	countA = 0
	for a in izdA:
		cost = a[0]
		for x in range(1, a[1] + 1):
			if M - cost >= 0:
				countA += 1
				M -= cost
			else:
				break
				
	print(countA, M)