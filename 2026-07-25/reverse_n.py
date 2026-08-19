#Reverse a number
def rev(n,a):
    b=a-1
    if b == 0:                                     # a=1
        return n
    return n%10 * 10**(b) + rev(n//10 ,b)
print(rev(421,3))

#_____________________________________________
def rev(n, result=0):
    if n == 0:
        return result

    return rev(n // 10, result * 10 + n % 10)

print(rev(421))