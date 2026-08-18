def count_consonants(s):
    if s=="":
        return 0
    if s[0].lower() in "bcdfghjklmnpqrstvwxyz":
        return 1 + count_consonants(s[1:])
    return count_consonants(s[1:])

s="ABCCD" 
print(count_consonants(s))
        