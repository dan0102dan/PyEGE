# https://inf-ege.sdamgia.ru/problem?id=16818

def f(letter):
	if letter == 'А':
		return 1

	if letter == 'Б':
		return sum([f(l) for l in 'А'])

	if letter == 'Г':
		return sum([f(l) for l in 'А'])

	if letter == 'Д':
		return sum([f(l) for l in 'Б'])

	if letter == 'Е':
		return sum([f(l) for l in 'Д'])

	if letter == 'Ж':
		return sum([f(l) for l in 'Д'])

	if letter == 'И':
		return sum([f(l) for l in 'ГЕ'])

	if letter == 'К':
		return sum([f(l) for l in 'ЖДЕИ'])

	if letter == 'Л':
		return sum([f(l) for l in 'К'])

	if letter == 'М':
		return sum([f(l) for l in 'К'])
	
	if letter == 'Н':
		return sum([f(l) for l in 'ЛМК'])

print(f('Н'))