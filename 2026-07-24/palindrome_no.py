num=121
temp=121
rev=0
while temp>0:
    digit=temp%10
    temp=temp//10
    rev=rev*10 + digit

if rev==num:
    print("YES")
else:
    print("NO")
    