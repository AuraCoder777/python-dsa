def case_permutations(s,current=""):
    if len(s)==0:
        print(current)
        return
    case_permutations(s[1:],current+s[0])
    case_permutations(s[1:],current+s[0].upper())
    
case_permutations("ab")
    