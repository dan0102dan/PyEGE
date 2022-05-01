s = 'BADAABADADA'
etr = ['BA', 'DA']
maxim, cur = 0, 0
i = 0
while i <= len(s) - 1:
	if s[i:i+2] in etr:
		for j in range(i, len(s) - 1, 2):
			if s[j:j+2] in etr:
				cur += 1
				if cur > maxim:
					maxim = cur
			else:
				i = j - 2
				cur = 0
				break
	else:
		cur = 0
	i += 1
print(maxim)