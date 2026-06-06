# Declare a blank 3x3 multidimensional list space matrix layout  
board = [  
    [".", ".", "."],  
    [".", ".", "."],  
    [".", ".", "."]  
]

def print_board():  
    for row in board:  
        print(" ".join(row))

# Simulate placing characters onto targeted board intersections  
board[0][0] = "X"  
board[1][1] = "O"  
print_board()
