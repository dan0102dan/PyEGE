with open('24.txt') as f:
    s = f.readline().strip()

res = cur = 0
for i in range(len(s) - 1):
    if s[i:i+2] in ['AB', 'CB']:
        for j in range(i, len(s) - 1, 2):
            if s[j:j+2] in ['AB', 'CB']:
                cur += 1
                res = max(res, cur)
            else:
                cur = 0
                break
    else:
        cur = 0

print(res)