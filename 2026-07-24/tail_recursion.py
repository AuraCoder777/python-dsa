def countdown(n):
    if n == 0:              # Base Case
        print("GO!")
        return

    print(n)
    countdown(n - 1)        # Recursive Case

countdown(5)

#TAIL RECURSION