curs_pos_x = 0
curs_pos_y = 0
win_state = False
good_grid =	[[1,2,3,4,5,6,7,8,9],
			[4,5,6,7,8,9,1,2,3],
			[7,8,9,1,2,3,4,5,6],
			[2,3,1,5,6,4,8,9,7],
			[5,6,4,8,9,7,2,3,1],
			[8,9,7,2,3,1,5,6,4],
			[3,1,2,6,4,5,9,7,8],
			[6,4,5,9,7,8,3,1,2],
			[9,7,8,3,1,2,6,4,5]]

bad_grid =	[[1,2,3,4,5,6,7,8,9],
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
def SudokuCheck(_grid):
	for i in range(9):
		for j in range(9):
			temp = abs(_grid[i][j])
			# horizontal check
			for k in range(9-j):
				if (temp == abs(_grid[i][j+k]) and k!=0):
					_grid[i][j] = -1 * abs(_grid[i][j])
					_grid[i][j+k] = -1 * abs(_grid[i][j])
			# vertical check
			for k in range(9-i):
				if (temp == abs(_grid[i+k][j]) and k!=0):
					_grid[i][j] = -1 * abs(_grid[i][j])
					_grid[i+k][j] = -1 * abs(_grid[i][j])
			# 3x3 check
			igrid = (int)(i/3)
			jgrid = (int)(j/3)
			for ig in range(igrid*3,igrid*3+3):
				for jg in range(jgrid*3, jgrid*3+3):
					if (temp == abs(_grid[ig][jg]) and (i != ig and j != jg)):
						_grid[ig][jg] = -1 * abs(_grid[i][j])
						_grid[i][j] = -1 * abs(_grid[i][j])

# Prints out sudoku board
# invalid lines have issues highlighted in red
def SudokuPrint(_grid):
	SudokuCheck(_grid)
	global curs_pos_x, curs_pos_y
	for i in range(9):
		for j in range(9):
			curr = str(abs(_grid[i][j]))
			# if position is invalid change font to red
			# Sudoku check makes invalid entries negative their entered number
			if _grid[i][j] < 0:
				curr = '\033[91m' + curr + '\033[0m'
			if (curs_pos_x == i) and (curs_pos_y == j):
				curr = '\033[7m' + curr + '\033[0m'
			print(curr, end = '')

			# print grid borders to group into 3X3 grids
			if j != 8:
				if (j+1) % 3 == 0:
					print(' | ', end = '')
				else:
					print(', ', end = '')
			else:
				print()
		if i != 8:
			if (i+1) % 3 == 0:
				print('--------+---------+--------')
	print('')

#SudokuPrint(good_grid)
SudokuPrint(bad_grid, curs_pos_x, curs_pos_y)