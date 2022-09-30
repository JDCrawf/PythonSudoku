grid = [[1,2,3,4,5,6,7,8,9],
		[4,5,6,7,8,9,1,2,3],
		[7,8,9,1,2,3,4,5,6],
		[2,3,1,5,6,4,8,9,7],
		[5,6,4,8,9,7,2,3,1],
		[8,9,7,2,3,1,5,6,4],
		[3,1,2,6,4,5,9,7,8],
		[1,4,5,9,7,8,3,1,2],
		[9,7,8,3,1,2,6,4,5]]

# parses through sudoku grid checking for invalid lines/grids
# first checks horizontally, then vertically, then by 3x3
def SudokuCheck(grid):
	for i in range(9):
		for j in range(9):
			temp = abs(grid[i][j])
			# horizontal check
			for k in range(9-j):
				if (temp == abs(grid[i][j+k]) and k!=0):
					grid[i][j] = -1 * abs(grid[i][j])
					grid[i][j+k] = -1 * abs(grid[i][j])
			# vertical check
			for k in range(9-i):
				if (temp == abs(grid[i+k][j]) and k!=0):
					grid[i][j] = -1 * abs(grid[i][j])
					grid[i+k][j] = -1 * abs(grid[i][j])
			# 3x3 check
			igrid = (int)(i/3)
			jgrid = (int)(j/3)
			for ig in range(igrid*3,igrid*3+3):
				for jg in range(jgrid*3, jgrid*3+3):
					if (temp == abs(grid[ig][jg]) and (i != ig and j != jg)):
						grid[ig][jg] = -1 * abs(grid[i][j])
						grid[i][j] = -1 * abs(grid[i][j])

# Prints out sudoku board
# invalid lines have problems highlighted in red
def SudokuPrint(grid):
	SudokuCheck(grid)
	for i in range(9):
		for j in range(9):
			if grid[i][j] < 0:
				print('\033[91m' + str(abs(grid[i][j])) + '\033[0m', end = '')
			else:
				print(grid[i][j], end = '')
			if j != 8:
				if (j+1) % 3 == 0:
					print(' | ', end = '')
				else:
					print(', ', end = '')
			else:
				print()
		if i != 8:
			if (i+1) % 3 == 0:
				print('-----------------------------')


SudokuPrint(grid)