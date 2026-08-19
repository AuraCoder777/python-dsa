#Print numbers from 1 to n
def print_1_to_n(n):
    if n == 0:         
        return

    print_1_to_n(n-1)   
    print(n)            

print_1_to_n(5)

