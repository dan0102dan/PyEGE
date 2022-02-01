import math

def solveQquation(a, b, c):
	if a == 0 and b == 0:
		return 'infinity'
	elif a == 0:
		return -c/b
	else:
		D = b**2 - 4*a*c
		if (D < 0):
			return 'no solutions'
		else:
			if (D == 0):
				return -b/2*a
			else:
				return (-b+math.sqrt(D)) / (2*a), (-b-math.sqrt(D)) / (2*a)

try:
	try:
		assert solveQquation(0, 0, 0) == 'infinity'
		assert solveQquation(2, 5, 3) == (-1, -1.5)
		print('Функция проверена')
	except:
		print('Функция неисправна')
	a, b, c = map(lambda x: int(x), input('Введите коэфициэнты:\n').split(' '))

	print(solveQquation(a, b, c))
except:
	print('Не удалось преобразовать числа')