def odd(n):
    if n == 0 :
        return
    
    odd(n-1)
    
    if n % 2 != 0 :
        print(n)
    
odd(10)
    