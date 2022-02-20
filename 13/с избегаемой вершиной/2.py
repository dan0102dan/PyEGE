# https://inf-ege.sdamgia.ru/problem?id=16891

def f(letter):
	if letter == 'А':
		return 1

	if letter == 'Б':
		return sum([f(l) for l in 'А'])

	if letter == 'Г':
		return sum([f(l) for l in 'АВ'])

	if letter == 'В':
		return sum([f(l) for l in 'АБ'])

	if letter == 'Д':
		return sum([f(l) for l in 'БВ'])

	if letter == 'Ж':
		return sum([f(l) for l in 'Д'])

	if letter == 'И':
		return sum([f(l) for l in 'ГВ'])

	if letter == 'К':
		return sum([f(l) for l in 'ЖДИ'])

	if letter == 'Л':
		return sum([f(l) for l in 'К'])

	if letter == 'М':
		return sum([f(l) for l in 'К'])
	
	if letter == 'Н':
		return sum([f(l) for l in 'ЛМК'])

print(f('Н'))