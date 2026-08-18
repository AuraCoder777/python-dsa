def rev(n,result=0):
    if n == 0:
        return result
    result = result*10 + n%10
    return rev(n//10,result)

def check_palindrome(n):
    if rev(n) == n:
        print("TRUE")
    else:
        print("FALSE")
        
check_palindrome(123321)
    
    
    
    