from basic import *

n = 5
otstup = len(str(n ** 2 - 1))

def out(mes, color = ''):
    print(color + mes + '\033[0m', end='\n' if j == m - 1 else '|')

matrix = generator(n, n)
log(matrix)
print('-' * (n * otstup + n - 1))

for j in range(n):
    for i in range(n - 1, -1, -1):
        print(matrix[i][j], end=' ')
    print()