#Largest number in a list
def maximum(a,max=0):
    if a==[]:
        return max
    if a[0]>=max:
        max= a[0]
    return maximum(a[1::],max)
        
    
print(maximum([8,5,4,3,2]))
        
#______________________________________

def maximum(a):
    if len(a) == 1:
        return a[0]

    max_rest = maximum(a[1:])

    if a[0] > max_rest:
        return a[0]

    return max_rest


print(maximum([1, 2, 3, 4, 5]))
print(maximum([-5, -2, -10, -1]))