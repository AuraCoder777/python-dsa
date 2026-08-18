def digital_root(n,s=0):
    if n==0:
        if s<10:
            return s
        return digital_root(s)
            
        
    return digital_root(n//10,s+n%10)
     
    

print(digital_root(38))

    