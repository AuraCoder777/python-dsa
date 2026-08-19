#Digital Multiplication of a number
def recursive_digit_multiply(n,prod=1):
    if n==0:
        if prod<10:
            return prod
        return recursive_digit_multiply(prod)
    return recursive_digit_multiply(n//10,prod*n%10)

print(recursive_digit_multiply(42))
    