#Square of a number
def sq(n):
    if n==0:
        return
    sq(n-1)
    print(n*n)
sq(10)