def sumseq(arr,k,current=[]):
    if len(arr)==0:
        if sum(current)==k:
            print(current)
        return
    
    sumseq(arr[1:],k,current+[arr[0]])
    sumseq(arr[1:],k,current)
sumseq([1,2,3,4,5,6,7,8,9,10],11)