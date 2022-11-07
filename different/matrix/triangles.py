from basic import *

n = 10
m = 10
otstup = len(str(n * m - 1))

def out(mes, color = ''):
    print(color + mes + '\033[0m', end='\n' if j == m - 1 else '|')


matrix = generator(n, m)
log(matrix)
print('-' * (m * otstup + m - 1))

print('up:')
for i in range(n):
    for j in range(m):
        if j < n - i - 1 and j > i:
            out(f'{matrix[i][j]}', '\033[32m')
        else:
            out('-' * otstup, '\033[35m' if j in [i, n - i - 1] else '')
print('left:')
for i in range(n):
    for j in range(m):
        if j < n - i - 1 and j < i:
            out(f'{matrix[i][j]}', '\033[32m')
        else:
            out('-' * otstup, '\033[35m' if j in [i, n - i - 1] else '')
print('down:')
for i in range(n):
    for j in range(m):
        if j > n - i - 1 and j < i:
            out(f'{matrix[i][j]}', '\033[32m')
        else:
            out('-' * otstup, '\033[35m' if j in [i, n - i - 1] else '')
print('right:')
for i in range(n):
    for j in range(m):
        if j > n - i - 1 and j > i:
            out(f'{matrix[i][j]}', '\033[32m')
        else:
            out('-' * otstup, '\033[35m' if j in [i, n - i - 1] else '')