board = [[0 for x in range(0, 8)] for y in range(0, 8)]
count = 0
def possible(n, row, col):

    for r in range(row-1, -1, -1):
        if board[r][col] == 1:
            return False

    for r, c in zip(range(row - 1, -1, -1), range(col-1, -1,-1)):

        if board[r][c] == 1:
            return False

    for r, c in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[r][c] == 1:
            return False

    return True

def queenHelper(n, row):
    if row == n:
        global count
        count = count + 1
        return

    for col in range(0, n):
        if possible(n, row, col):
            board[row][col] = 1
            queenHelper(n, row+1)
            board[row][col] = 0
    return

def nQueen(n):
    queenHelper(n, 0)
    print(count)



nQueen(8)