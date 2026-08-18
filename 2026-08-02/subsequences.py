def subseq(s,current=""):
    if s=="":
        print(current)
        return
    subseq(s[1:],current+s[0])
    subseq(s[1:],current)
    
subseq("ABC")