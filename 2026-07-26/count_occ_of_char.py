def count_occ(s,char):
    if s=="":
        return 0
    if s[0].lower() == char:
        return 1 + count_occ(s[1:],char)
    return count_occ(s[1:],char)

s="hala madrid"
char="a"
print(count_occ(s,char))