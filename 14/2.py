# Укажите, сколько всего раз встречается цифра 2 в записи чисел 10, 11, 12, …, 17 в системе счисления с основанием 5.

def convertToBase(num, base):
	bases = list('0123456789ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') # записал цифры в разных основаниях

	result = [0]
	for i in range(abs(num)): # запускаем цикл, который выполнится num раз
		for el in range(len(result)): # перебираем наш промежуточный результат, чтобы добавить к каждому разряду единицу
			if result[el] + 1 < base: # прибавляем единицу, если это не будет превышать заданное основание
				result[el] += 1
				break # остоналиваем, потому что нам больше не нужно ничего добавлять
			else:
				result[el] = 0 # обнуляем текущий разряд и идём дальше
				if el + 1 == len(result): # если это был последний разряд, то добавляем новый
					result.append(1)
	return ('' if num >= 0 else '-') + ''.join(map(lambda x: str(bases[x]), reversed(result)))

result = 0

for x in range(10, 18):
	result += convertToBase(x, 5).count('2')
print(result)