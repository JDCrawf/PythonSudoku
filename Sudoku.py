grid = [[1,2,3,4,5,6,7,8,9],
		[4,5,6,7,8,9,1,2,3],
		[7,8,9,1,2,3,4,5,6],
		[2,3,1,5,6,4,8,9,7],
		[5,6,4,8,9,7,2,3,1],
		[8,9,7,2,3,1,5,6,4],
		[3,1,2,6,4,5,9,7,8],
		[6,4,5,9,7,8,3,1,2],
		[9,7,8,3,1,2,6,4,5],]

for i in range(9):
	for j in range(9):
		temp = grid[i][j]
		# horizontal check
		for k in range(9-j):
			if (temp == grid[i][j+k] and k!=0):
				grid[i][j+k] = -1
		# vertical check
		for k in range(9-i):
			if (temp == grid[i+k][j] and k!=0):
				grid[i+k][j] = -1
		# 3x3 check

for i in range(9):
	print(grid[i])
