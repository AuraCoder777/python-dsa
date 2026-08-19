#Count number of characters in a string
def count_char(s):
    if s=="":
        return 0
    return 1 + count_char(s[1:])

print(count_char("REAL MADRID"))