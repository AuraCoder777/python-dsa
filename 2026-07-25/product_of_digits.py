def prod_of_digits(n):
    if n == 0:
        return 1
    return n%10 * prod_of_digits(n//10)
print(prod_of_digits(123))