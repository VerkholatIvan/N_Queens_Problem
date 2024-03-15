# The given problem is called the N-Queens problem. The main idea is to place all of the queen’s figures on a chessboard the size of 8 x 8 in that places, 
# where they could not eat each other, so the figures must not be aligned vertically, horizontally, or diagonally. 

# The algorithm works by placing the queens on each row, one at a time. Before placing a figure, the machine checks if the place matches the given conditions, 
# so it looks in all of the directions and decides whether to put the queen or not. If the place is safe, the figure is placed and then it is continuous, 
# but if it is not, then the algorithm backtracks to the previous row and tries a different position. Finally, when each row has a queen on it a valid solution was found.

# The code is based on the Python programming language, and it consists of 4 functions. The two first ones, “safe_place” and “set_queen”, are checking if the place is safe 
# in all directions and then set the figure if conditions are met, respectively. The “solution_ouput” function initializes the board , and if a solution was found, 
# it calls the “print_board” method, which replace 1 and 0 to ‘Q’ and ‘.’, respectively, to make the output more readable.


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
        return True # all queens have been placed

    for col in range(N):
        if safe_place(board, row, col, N):
            board[row][col] = 1 # place the queen
            if set_queen(board, row + 1, N):
                return True # found a solution
            board[row][col] = 0 # backtrack
    return False # no solution found

# Board cretation and putting 1 (Queen or True)) and 0 (Empty or False)
def solution_output(N):
    board = [[0 for _ in range(N)] for _ in range(N)] # initialize the board with the size of N x N
    if set_queen(board, 0, N):
        # print the solution
        print_board(board)
    else:
        print("No solution exists")

# function to replace 1 and 0 to 'Q' and '.', respectively
def print_board(board):
    for row in board:
        print(' '.join(['Q' if empty else '.' for empty in row])) # Place 'Q' if empty (True), else place '.' if it is (False)


# output section
N = 8
# N = int(input("Enter the size of the chessboard: \n>> ")) ## entering the size of the board for debugging
solution_output(N)