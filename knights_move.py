x, y = map(lambda x: int(x), input('Введите коэфициэнты: (x y)\n').split(' '))

def generateDesk(initially, modified):
	desk = []
	for desk_x in range(1, 9):
		desk.append([])
		for desk_y in range(1, 9):
			if (desk_x == initially[0]) and (desk_y == initially[1]):
				desk[desk_x - 1].append('❌')
			elif (desk_x == modified[0]) and (desk_y == modified[1]):
				desk[desk_x - 1].append('❎')
			else:
				desk[desk_x - 1].append('⬛')

	return desk

variants = []
for moveX in range(-2, 3):
	for moveY in range(-2, 3):
		if not((abs(moveX) == abs(moveY)) or moveX == 0 or moveY == 0):
			#print([moveX, moveY], [moveX+x, moveY+y])
			if (0 < x + moveX and x + moveX < 9)  and (0 < y + moveY and y + moveY < 9):
				variants.append([moveX, moveY])

print('Возможнные варианты:')
for i, variant in enumerate(variants):
	print('№', i + 1, (variant))
	for line in generateDesk((x, y), (variant[0] + x, variant[1] + y)):
			print(''.join(line))

print('Ответ:', variants)