n = 4
queens = []


def is_safe(row,col):
    for r,c in queens:
        if c==col:
            return False
        if abs(r-row)==abs(c-col):
            return False
    return True

def print_board():
    for i in range(n):
        for j in range(n):
            if (i, j) in queens:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print("\n")
        


def solve(row):
    if row == n:
        print_board()
        return

    for col in range(n):
        if is_safe(row,col):

            queens.append((row, col))

            solve(row + 1)

            queens.pop()

solve(0)