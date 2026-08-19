#Print numbers from n to 1 ~ Countdown
def countdown(n):
    if n == 0:              # Base Case
        print("GO!")
        return

    print(n)
    countdown(n - 1)        # Recursive Case

countdown(5)
