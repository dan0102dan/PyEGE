# Определить, каким по счёту символом от начала файла окажется 10000-я открывающая скобка «(».

with open('24.txt') as f:
	s = f.readline().strip()
 
	point = 0

	for i in range(len(s)):
		if s[i] == '(':
			point += 1

			if point == 10000:
				print(i + 1)