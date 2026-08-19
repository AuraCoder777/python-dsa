#Reverse a string
def rev_str(s):
    if s=="":
        return ""
    return rev_str(s[1:]) + s[0]

print(rev_str("CAR"))