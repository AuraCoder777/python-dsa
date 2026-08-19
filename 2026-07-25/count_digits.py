#Count number of digits
def count(n):
    if n==0:
        return 0
    return 1+ count(n//10)
print(count(23114))