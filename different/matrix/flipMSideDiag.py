from basic import *

n = 5
m = 5
otstup = len(str(n * m - 1))

def out(mes, color = ''):
    print(color + mes + '\033[0m', end='\n' if j == m - 1 else '|')


matrix = generator(n, m)
log(matrix)
print('-' * (m * otstup + m - 1))

for i in range(n):
    for j in range(m):
        if j != n - i - 1:
            out(f'{matrix[n-i-1][m-j-1]}', '\033[32m')
        else:
            out(matrix[i][j], '\033[35m' if j == n - i - 1 else '')