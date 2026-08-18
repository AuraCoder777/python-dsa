def combinations(arr, k, current=[]):
    if len(current)==k:
        print(current)
        return
    
    if len(arr) == 0:
        return
    
    combinations(arr[1:],k,current+[arr[0]])
    combinations(arr[1:],k,current)
combinations([1,2,3],2)    
    