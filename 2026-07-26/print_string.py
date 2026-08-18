def print_str(s):
    if s=="":
        return 
    print(s[0])
    print_str(s[1:])

print(print_str("CAT")) 


    
    
    