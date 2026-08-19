#Print even numbers from N to 1 
def even(n):                               
    if n == 0:
        return
    
    even(n-1)
    
    if n % 2 == 0 :
        print(n)
        
even(10)   
    