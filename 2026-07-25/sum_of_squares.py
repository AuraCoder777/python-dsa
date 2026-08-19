#Sum of squares from n to 1
def sum_of_squares(n):
    if n == 0:
        return 0
    return n**2 + sum_of_squares(n - 1)

print(sum_of_squares(5))