# Сколько слов длины 5, начинающихся с гласной буквы, можно составить из букв Е, Г, Э? Каждая буква может входить в слово несколько раз.

letters = 'ЕЭГ'
words = []

for a in letters[:2]:
	for b in letters:
		for c in letters:
			for d in letters:
				for e in letters:
					words.append(a+b+c+d+e)
print(len(words))