# To adjust the size of the board change the "N" variable on line 49

# Checks whether the location is safe
def safe_place(board, row, column, N):
    # check if there is any queen in the same column
    for i in range(row):
        if board[i][column]:
            return False
    # check if there is any queen in the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)): # zip command combine both of the range functions. Exmaple how the program will see this line: chessboard[range(row, -1, -1][range(column, -1, -1] = chessboard[row][column]
        if board[i][j]:
            return False
    # check if there is any queen in the upper right diagonal
    for i, j in zip(range(row, -1, -1), range(column, N)):
        if board[i][j]:
            return False
    return True


# Setting the figures on the board
def set_queen(board, row, N):
    if row == N:
        return True # All queens have been placed

    for col in range(N):
        if safe_place(board, row, col, N):
            board[row][col] = 1 # place the queen
            if set_queen(board, row + 1, N):
                return True # found a solution
            board[row][col] = 0 # backtrack
    return False # no solution found

# Board creation and putting 1 (Queen or True)) and 0 (Empty or False)
def solution_output(N):
    board = [[0 for _ in range(N)] for _ in range(N)] # initialize the board with the size of N x N
    if set_queen(board, 0, N):
        # print the solution
        print_board(board)
    else:
        print("No solution exists")

# function to replace 1 and 0 with 'Q' and '.', respectively
def print_board(board):
    for row in board:
        print(' '.join(['Q' if empty else '.' for empty in row])) # Place 'Q' if empty (True), else place '.' if it is (False)


# output section
N = 8
# N = int(input("Enter the size of the chessboard: \n>> ")) ## entering the size of the board for debugging
solution_output(N)
