# Иван составляет 5-буквенные коды из букв И, В, А, Н. Буквы в коде могут повторяться, использовать все буквы не обязательно, но букву И нужно использовать хотя бы один раз. Сколько различных кодов может составить Иван?

letters = 'ИВАН'
words = []

for i in letters:
	for x in letters:
		for y in letters:
			for z in letters:
				for p in letters:
					words.append(i+x+y+z+p)

print(sum('И' in word for word in words))