def is_sorted(l):
    if len(l)==1:
        return True
    if l[0] > l[1]:
         return False
    return is_sorted(l[1:])
        
l=[5,6,7]
print(is_sorted(l))
    
    
    
