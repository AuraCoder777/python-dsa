#Recursive Binary Search of a number
def search(l,target):
    if l==[]:
        return False
        
    middle=len(l)//2
    
    if target == l[middle]:
        return True
    elif target < l[middle]:
        return search(l[:middle],target)
    elif target > l[middle]:
        return search(l[middle+1:],target)   
    else:
        return False
    
    
l=[2,4,6,8,10,12]
target=6
print(search(l,target)) 