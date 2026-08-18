def even(n):                               #Print all even numbers from N to 1 using recursion
    if n == 0:
        return
    
    even(n-1)
    
    if n % 2 == 0 :
        print(n)
        
even(10)   
    