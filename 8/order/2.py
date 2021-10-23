# Все 5-буквенные слова, составленные из букв А, О, У, записаны в алфавитном порядке. Вот начало списка:
# 1. ААААА
# 2. ААААО
# 3. ААААУ
# 4. АААОА
#    ...
# Укажите номер первого слова, которое начинается с буквы У.

letters = 'АОУ'
words = []

for a in letters:
	for b in letters:
		for c in letters:
			for d in letters:
				for e in letters:
					word = a+b+c+d+e
					words.append(word)
					if word[0] == 'У':
						print(len(words))