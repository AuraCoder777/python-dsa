#Count 
def search(l,n):
    if l == []:
        return "Not Found"
    
    if l[0] == n:
        return "Found"
    
    return search(l[1:],n)

l=[7,8,9]
n=7
print(search(l,n))


    