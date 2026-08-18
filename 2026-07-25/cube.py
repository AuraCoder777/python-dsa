def cube(n):
    if n==0:
        return
    cube(n-1)
    print(n**3)
cube(10)