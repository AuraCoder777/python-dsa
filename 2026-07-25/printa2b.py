def a2b(a,b):
    if a > b:
        return 
    print(a)
    a2b(a+1,b)
a2b(5,10)