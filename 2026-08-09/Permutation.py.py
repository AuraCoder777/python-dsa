#Permutation of a string
def permu(s, current=""):
    if len(s) == 0:
        print(current)
        return

    for i in range(len(s)):
        remaining = s[:i] + s[i+1:]
        permu(remaining, current + s[i])

permu("ABC")