def mul(a,b):
    if b==0:
        return
    mul(a,b-1)
    print(f"{a} x {b} = {a*b}")
mul(5,10)