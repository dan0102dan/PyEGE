# Сколько существует различных символьных последовательностей длины 5 в четырёхбуквенном алфавите {A, C, G, T}, которые содержат ровно две буквы A?
letters = 'ACGT'
words = []

for a in letters:
	for b in letters:
		for c in letters:
			for d in letters:
				for e in letters:
					word = a+b+c+d+e
					if word.count('A') == 2:
						words.append(word)
print(len(words))