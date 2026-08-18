def print_1_to_n(n):
    if n == 0:          # Base Case
        return

    print_1_to_n(n-1)   # Recursive Call
    print(n)            # Work after recursion

print_1_to_n(5)

#HEAD RECURSION