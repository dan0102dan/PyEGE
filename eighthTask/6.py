# Света составляет 5-буквенные коды из букв С, В, Е, Т, А. Буквы в коде могут повторяться, использовать все буквы не обязательно, но букву С нужно использовать хотя бы один раз. Сколько различных кодов может составить Света?

letters = 'СВЕТА'
words = []

for a in letters:
	for b in letters:
		for c in letters:
			for d in letters:
				for e in letters:
					word = a+b+c+d+e
					if word.count('С') >= 1:
						words.append(word)
print(len(words))