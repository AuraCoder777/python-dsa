num=0
count1=0
for digit in str(num):
    count1+=1
    
print(count1)

#____________________________________

if num == 0:
    count = 1
else:
    count = 0
    while num > 0:
        num //= 10
        count += 1

print(count)