n=4
row=1

for col in range(n):
    for i in range(n):
        print()
        for j in range(n):
            if i==row and j==col:
                print("Q",end=" ")
            else:
                print(".",end=" ")
    print("\n")