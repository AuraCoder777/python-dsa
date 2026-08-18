def pow(x,n):
    if n == 0:
        return 1
    return x* pow(x,n-1)

print(pow(2, 5))

#-----------------------------------
x=2
ans=1
n=5
while n>0:
    ans=ans*x
    n=n-1
print(ans)
    