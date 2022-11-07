def generator(n, m):
    matrix = []
    for i in range(n):
        matrix.append([str(i * m + j).zfill(len(str(n * m - 1))) for j in range(m)])
    return matrix
def log(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            print('\033[31m' + f'{matrix[i][j]}' + '\033[0m', end='\n' if j == m - 1 else '|')