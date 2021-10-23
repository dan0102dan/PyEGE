# Все 5-буквенные слова, составленные из букв А, К, Р, У, записаны в ал-фавитном порядке. Вот начало списка:
# 1. ААААА
# 2. ААААК
# 3. ААААР
# 4. ААААУ
# 5. АААКА
#    ...
# Запишите слово, которое стоит на 150-м месте от начала списка.

letters = 'АКРУ'
words = []

for a in letters:
	for b in letters:
		for c in letters:
			for d in letters:
				for e in letters:
					word = a+b+c+d+e
					words.append(word)
print(words[149])