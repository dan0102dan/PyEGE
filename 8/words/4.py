# Андрей составляет 7-буквенные коды из букв А, Н, Д, Р, Е, Й. Буквы А и Й должны встречаться в коде ровно по одному разу, при этом буква Й не может стоять на первом месте. Остальные допустимые буквы могут встречаться произвольное количество раз или не встречаться совсем. Сколько различных кодов может составить Андрей?

letters = 'АНДРЕЙ'
words = []

for a in letters[:-1]:
	for b in letters:
		for c in letters:
			for d in letters:
				for e in letters:
					for f in letters:
						for j in letters:
							word = a+b+c+d+e+f+j
							if (word.count('А') == 1) and (word.count('Й') == 1):
								words.append(word)
print(len(words))