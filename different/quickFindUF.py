def validPath(n: int, edges: [[int]], source: int, destination: int) -> bool:
	parent = [i for i in range(n)]
	size = [1] * n

	def root(i: int) -> int:
		while i != parent[i]:
			i = parent[i]
		return i
	
	for edge in edges:
		rootP = root(edge[0])
		rootQ = root(edge[1])

		if rootP == rootQ:
			continue
		
		if (size[rootP] < size[rootQ]):
			parent[rootP] = rootQ
			size[rootQ] += size[rootP]
		else:
			parent[rootQ] = rootP
			size[rootP] += size[rootQ]
	
	return root(source) == root(destination)

print(
validPath(n = 10, edges = [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]], source = 5, destination = 9)
)