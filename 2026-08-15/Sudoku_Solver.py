board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
] 

def find_empty(board):
    for row in range (9):
        for col in range(9):
            if board[row][col] == 0:
                return (row,col)
                
def is_valid(board,row,col,num):
    for c in range(9):
        if board[row][c] == num:
            return False
            
    for r in range(9):
        if board[r][col] == num:
            return False
        
    start_row = (row//3) * 3
    start_col = (col//3) * 3
    for r in range(start_row,start_row+3):
        for c in range(start_col,start_col+3):
            if board[r][c]==num:
                return False
    return True

def print_board(board):
    for row in range(9):
        for col in range(9):
            print(board[row][col], end=" ")

            if col == 2 or col == 5:
                print("|", end=" ")

        print()

        if row == 2 or row == 5:
            print("------+-------+------")

def solve(board):
    empty=find_empty(board)
    if empty == None:
        return True
    
    row,col=empty
    
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col]=num
            if solve(board):
                return True
            board[row][col]=0
    return False

solve(board)
if solve(board):
    print("Solved!")
    print_board(board)
else:
    print("No solution")
    


        