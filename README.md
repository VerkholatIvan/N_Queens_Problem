# N_Queens_Problem
![queens](https://github.com/VerkholatIvan/N_Queens_Problem/assets/123458146/be40b7f6-cff6-485a-8f63-22e6b247a1a3)

### The given problem is called the N-Queens problem. The main idea is to place all of the queen’s figures on a chessboard the size of 8 x 8 in that places, where they could not eat each other, so the figures must not be aligned vertically, horizontally, or diagonally. 
### The algorithm works by placing the queens on each row, one at a time. Before placing a figure, the machine checks if the place matches the given conditions, so it looks in all of the directions and decides whether to put the queen or not. If the place is safe, the figure is placed and then it is continuous, but if it is not, then the algorithm backtracks to the previous row and tries a different position. Finally, when each row had a queen on it a valid solution was found.
### The code is based on the Python programming language, and it consists of 4 functions. The two first ones, “safe_place” and “set_queen”, check if the place is safe in all directions and then set the figure if conditions are met, respectively. The “solution_ouput” function initializes the board, and if a solution is found, it calls the “print_board” method, which replaces 1 and 0 to ‘Q’ and ‘.’, respectively, to make the output more readable.
### All comments explaining the code are provided 
