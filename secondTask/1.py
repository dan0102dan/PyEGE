for x in range(2):
	for y in range(2):
		for z in range(2):
			for w in range(2):
				if ((x and w) or (w and z)) == ((not(z) or y) and (not(y) or x)):
					print(y,z,w,x)