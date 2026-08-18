def sum_of_digits(n,a):
    if n == 0:
        return 0
    return num%10 + rev(num//10 ,a-1)
print(rev(123,3))