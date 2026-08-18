def subsets(l,current=[]):
    if l==[]:
        print(current)
        return
    subsets(l[1:],current+[l[0]])
    subsets(l[1:],current)
    
l=[1,2,3]    
subsets(l)
    
        
        
    
    