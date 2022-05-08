with open("27a.txt") as f:
	N = int(f.readline())
	data = list(int(f.readline()) for i in range(N))

baki = {}
for i in range(N):
	n = i + 1
	baki[n] = 0
	for j in range(N):
		d = min(abs(i - j), N - abs(i - j))
		baki[n] += data[j] * d

print(sorted(baki.items(), key=lambda x: x[1])[0][0])