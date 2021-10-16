# Тимофей составляет 5-буквенные коды из букв Т, И, М, О, Ф, Е, Й. Буква Т должна входить в код не менее одного раза, а буква Й — не более одного раза. Сколько различных кодов может составить Тимофей?

letters = 'ТИМОФЕЙ'
words = []

for a in letters:
	for b in letters:
		for c in letters:
			for d in letters:
				for e in letters:
					word = a+b+c+d+e
					if (word.count('Й') <= 1) and (word.count('Т') >= 1):
						words.append(word)
print(len(words))