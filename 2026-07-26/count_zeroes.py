#Count occurrence of zeroes in a number
def count_zeroes(n):
    if n == 0:
        return 0
    if n%10==0:
        return 1 + count_zeroes(n//10)
    return count_zeroes(n//10)
print(count_zeroes(100460843890))
    
