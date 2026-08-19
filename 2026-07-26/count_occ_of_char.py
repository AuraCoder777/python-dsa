#Count occurrence of a character in a string
def count_occ(s,char):
    if s=="":
        return 0
    if s[0].lower() == char:
        return 1 + count_occ(s[1:],char)
    return count_occ(s[1:],char)

s="Hala Madrid"
char="a"
print(count_occ(s,char))