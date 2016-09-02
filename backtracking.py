def verify_board(board, line, pos):
	for i in range(0, line):
		if board[i][pos] == 1:
			return False

	for i in range(line + 1, 8):
		if board[i][pos] == 1:
			return False

	for i in range(0, pos):
		if board[line][i] == 1:
			return False

	for i in range(pos + 1, 8):
		if board[line][i] == 1:
			return False

	diag = [(line + x, pos + x) for x in range(-min(line, pos), 8 - max(line, pos)) if x != 0]
	diag2 = [(line + x, pos - x) for x in range(-max(line, pos), min(line, pos) + 1) if x != 0 and line + x >= 0 and line + x < 8 and pos - x >= 0 and pos - x < 8]
	diag.extend(diag2)
	for x, y in diag:
		if board[x][y] == 1:
			return False

	return True

def place_queens(board, line):
	if line >= 8:
		print("Got at line 8")
		return True

	for pos in range(0, 8):
		board[line][pos] = 1
		if verify_board(board, line, pos) and place_queens(board, line + 1):
			return True

		board[line][pos] = 0

	return False

if __name__ == '__main__':
	board = [[0 for i in range(8)] for j in range(8)]
	if not place_queens(board, 0):
		print("What the hell")

	for line in board:
		print(line)
