maze = [
    [1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 1]
]

path=[]
            
def is_safe(maze, row, col):
    if row < 0 or row >= len(maze):
        return False

    if col < 0 or col >= len(maze[0]):
        return False
    
    if maze[row][col] == 0:
        return False

    return True

def solve(maze, row, col):
    if not is_safe(maze, row, col):
        return False

    path.append((row, col))

    if row == len(maze)-1 and col == len(maze)-1:
        return True

    if solve(maze, row+1, col):
        return True

    if solve(maze, row, col+1):
        return True

    path.pop()

    return False

if solve(maze, 0, 0):
    print("Path:", path)
else:
    print("No path")

        
        
    
        
            