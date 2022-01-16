# Вася составляет 7-буквенные коды из букв Н, О, Б, Е, Л, И, Й. Каждую букву нужно использовать ровно 1 раз, при этом код не может начинаться с буквы Й и не может содержать сочетания ИЙО. Сколько различных кодов может составить Вася?

letters = 'НОБЕЛИЙ'
words = []

for a in letters:
	for b in letters:
		for c in letters:
			for d in letters:
				for e in letters:
					for f in letters:
						for g in letters:
							word = a+b+c+d+e+f+g
							if (a != 'Й') and ('ИЙО' not in word) and (word.count('Н') <= 1) and all(x <= 1 for x in map(lambda letter: word.count(letter), letters)):
								words.append(word)

print(len(words))