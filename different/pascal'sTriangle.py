def generate(numRows: int) -> [[int]]:
	triangle = [[0] * (i + 1) for i in range(numRows)]
	for row in triangle:
		row[0], row[-1] = 1, 1
			
	for i in range(2, numRows):
		for j in range(1, i):
			triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
		
	return triangle

print(generate(5))